#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        return consistent hypermedia data even while data may dynamically
        change due to deletions
        """
        largest_index = max(self.indexed_dataset().keys())
        assert type(index) is int
        assert index <= largest_index
        indexed_data = self.indexed_dataset()
        # original next index if no deletions occur
        next_index = index + page_size

        skip = 0
        data = []
        i = index
        while i < index + page_size + skip:
            if (indexed_data.get(i)):
                data.append(indexed_data[i])
            else:
                # increase searche range
                skip += 1
            i += 1
            next_index = i
            # if i steps over every possible boundary
            if (i > largest_index):
                next_index = None
                break

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
