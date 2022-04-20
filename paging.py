# CSC3002F OS Assignment 1
# Keeran Bezuidenhout
# BZDKEE001

from asyncio import futures
import sys
import random
import queue

empty_frame = " "
cli_num_pages = "-np"
cli_num_frames = "-nf"
cli_page_val_range = "-pvr"
cli_pages = "-p"

def FIFO (m_size, pages):
	"First In First Out page replacement algorithm."

	faults = 0										# faults will be output
	frames = [empty_frame]*m_size					# 'empty' list that represents the frames
	page_q = queue.Queue()							# queue to keep track of insert order of pages

	for p in pages:
		if is_hit(p, frames):						# it's already in memory, move on to next page
			continue
		
		space = is_hit(empty_frame, frames)			# if there is an 'empty' slot in the list of frames


		page_q.put(p)								# did not hit so need to insert to memory and add to queue
		faults += 1

		if space:									# if there is an 'empty' slot it will just insert it
			frames[frames.index(empty_frame)] = p
			continue
		
		# page replacement
		frames[frames.index(page_q.get())] = p		# replace oldest page

	return faults

def LRU (m_size, pages):
	"Least Recently Used page replacement algorithm."

	faults = 0										# faults will be output
	frames = []										# empty list that represents the frames
	age = {}										# dict to keep track of how long a page stays in memory

	for p in pages:									
		for key in age:								# increase each page age
			age[key] += 1

		if is_hit(p, frames):						# it's already in memory, move on to next page
			age[p] = 0					
			continue
		
		faults += 1

		if len(frames) < m_size:					# if memory is not full just insert the page with an age of 0
			frames.append(p)
			age[p] = 0
			continue

		# find page to replace
		max_age = 0
		lrup = empty_frame

		for key, value in age.items():				# iterate through dict for page with highest age
			if value > max_age:
				max_age = value
				lrup = key
		
		# swap out oldest page for new page
		frames.remove(lrup)
		frames.append(p)
		del age[lrup]
		age[p] = 0

		
	return faults


def OPT (m_size, pages):
	"Optimal page replacement algorithm."
	
	faults = 0																# faults will be output
	frames = []																# empty list that represents the frames

	for p in range(len(pages)):									

		if is_hit(pages[p], frames):										# it's already in memory, move on to next page					
			continue
		
		faults += 1

		if len(frames) < m_size:											# if memory is not full just insert the page with an age of 0
			frames.append(pages[p])
			continue

		# find page to replace
		furthest = frames[0]												# default to FIFO if no suitable replacement

		future_pages = pages[p : len(pages)]								# slice a subset of the pages list to iterate through
		for f in frames:													
			if not (f in future_pages):										# if the page doesn't occur again choose it to replace
				furthest = f
				break

			if future_pages.index(f) > future_pages.index(furthest):		# if the first occurence of this page in the future list is the furthest
				furthest = f

		# swap out pages
		frames.remove(furthest)
		frames.append(pages[p])

	return faults


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
