#!/bin/python

import dubizzle


if __name__ == '__main__':
	results = dubizzle.search(country='uae', city='dubai', section='motors', num_results=100)
	dir(results)