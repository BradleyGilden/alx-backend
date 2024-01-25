#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 25-01-2024
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns index depending on page position and size"""
    return ((page - 1) * page_size, page * page_size)


if __name__ == '__main__':
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
