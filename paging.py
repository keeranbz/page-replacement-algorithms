# CSC3002F OS Assignment 1
# Keeran Bezuidenhout
# BZDKEE001

import sys
import random
import queue

empty_frame = " "
cli_num_pages = "-np"
cli_num_frames = "-nf"
cli_page_val_range = "-pvr"
cli_pages = "-p"

def FIFO (m_size, pages):
	"FIFO page replacement algorithm."

	faults = 0										# faults will be output
	frames = [empty_frame]*m_size					# 'empty' list that represents the frames
	page_q = queue.Queue()							# queue to keep track of insert order of pages

	for p in pages:
		hit = is_hit(p, frames)						# if the page exists in the list of frames
		space = is_hit(empty_frame, frames)			# if there is an 'empty' slot in the list of frames

		if hit:										# it's already in memory, move on to next page
			continue
		
		page_q.put(p)								# did not hit so need to insert to memory and add to queue
		faults += 1

		if space:									# if there is an 'empty' slot it will just insert it
			frames[frames.index(empty_frame)] = p
			continue
		
		frames[frames.index(page_q.get())] = p		# replace oldest page

	return faults

def LRU (m_size, pages):
	return 0

def OPT (m_size, pages):
	return 0


def is_hit (page, frames):
	"""Checks if the page is already in main memory."""
	
	if page in frames:
		return True
	return False

def gen_list_rand_size (list_size, min, max):
	"""Generates a list of random numbers from min - max."""

	return [random.randint(min, max) for i in range(list_size)]

def main():
	# defaults for the number of pages and memory frames
	number_of_frames = random.randint(1, 7)
	number_of_pages = random.randint(1, 20)
	page_value_range = [1,9]																	# no negative numbers
	pages = []
	

	# parse cli input
	if cli_num_pages in sys.argv:																# if number of pages is specified
		number_of_pages = eval(sys.argv[sys.argv.index(cli_num_pages) + 1])
	
	if cli_num_frames in sys.argv:																# if number of frames is specified
		number_of_frames = eval(sys.argv[sys.argv.index(cli_num_frames) + 1])
	
	if cli_page_val_range in sys.argv:															# if the range of page values is specified
		page_value_range[0] = eval(sys.argv[sys.argv.index(cli_page_val_range) + 1])
		page_value_range[1] = eval(sys.argv[sys.argv.index(cli_page_val_range) + 2])

	if cli_pages in sys.argv:																	# if pages are manually specified
		for i in range(sys.argv.index(cli_pages) + 1, len(sys.argv)):
			if sys.argv[i].startswith("-"):
				break
			pages.append(eval(sys.argv[i]))
	else:
		pages = gen_list_rand_size(number_of_pages, page_value_range[0], page_value_range[1])	# randomly generate pages

	# display input data
	print("Pages: ", *pages)
	print("Memory frames:", number_of_frames)
	
	# run algorithms
	print("FIFO", FIFO(number_of_frames, pages), " page faults.")
	print("LRU", LRU(number_of_frames, pages), " page faults.")
	print("OPT", OPT(number_of_frames, pages), " page faults.")
	


if __name__ == "__main__":
	main()
