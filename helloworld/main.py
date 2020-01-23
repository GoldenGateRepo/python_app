#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""main.py: A console app, it prints hello world"""
import sys

def main(argv=None) -> None:
    """prints Hello, world
       Returns: None
    """

    if argv is None:
        argv = sys.argv
        
    print("Hello, world")

    return None

if __name__ == '__main__':
    #test
    main()
