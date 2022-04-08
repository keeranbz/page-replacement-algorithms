# CSC3002F OS Assignment 1
# Keeran Bezuidenhout
# BZDKEE001

import sys
import random
import queue

mem_size = random.randint(1, 7)
empty_frame = " "

def FIFO (size, pages):
	"FIFO page replacement algorithm."

	faults = 0
	frames = [empty_frame]*mem_size
	page_q = queue.Queue()

	for p in pages:
		hit = is_hit(p, frames)
		space = is_hit(empty_frame, frames)

		if hit:
			continue
		
		page_q.put(p)
		faults += 1

		if space:
			frames[frames.index(empty_frame)] = p
			continue
		
		frames[frames.index(page_q.get())] = p

	return faults

def LRU (size, pages):
	return 0

def OPT (size, pages):
	return 0


def is_hit (page, frames):
	"""Checks if the page is already in main memory."""
	
	if page in frames:
		return True
	return False

def gen_page_nums (size):
	"""Generates a list of random numbers from 0 - 9."""

	return [random.randint(0, 9) for i in range(size)]

def main():
	size = int(sys.argv[1])
	pages = gen_page_nums(size)
	
	print("Pages numbers: ", pages)
	print("Memory frames:", mem_size)
	
	print("FIFO", FIFO(size, pages), " page faults.")
	print("LRU", LRU(size, pages), " page faults.")
	print("OPT", OPT(size, pages), " page faults.")
	


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python paging.py[number of pages]")
	else:
		main()
