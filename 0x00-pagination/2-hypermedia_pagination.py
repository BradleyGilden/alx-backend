#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 25-01-2024
"""
import csv
import math
from typing import List, Dict, Union
index_range = __import__('0-simple_helper_function').index_range
HyperDict = Dict[str, Union[int, List[List], None]]


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns csv content in the form of nested lists
        depending on the page indexes
        """
        assert (type(page) is int and type(page_size) is int)
        assert (page > 0 and page_size > 0)

        # get the index range
        index = index_range(page, page_size)
        # get the csv data
        data = self.dataset()
        return data[index[0]: index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> HyperDict:
        """
            takes same args as get_page, but provides hypermedia descriptions
            about the page query as a dictionary
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
