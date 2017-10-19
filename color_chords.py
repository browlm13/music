# Color Chords

"""

 press q to quit
 press any other key for next chord

"""
import random

import cv2
import numpy as np

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

note_colors = {
	'A' : (124,26,117),
	'A#' : (162,37,134),
	'B' : (213,38,137),
	'C' : (245,28,42),
	'C#' : (237,72,45),
	'D' : (244,131,54),
	'D#' : (243,211,87),
	'E' : (244,243,93),
	'F' : (42,141,58),
	'F#' : (42,145,130),
	'G' : (31,29,124),
	'G#' : (69,28,121)
}

#reverse note_colors witten in wrong order!
for n in note_colors:
	first = note_colors[n][0]
	second = note_colors[n][1]
	third = note_colors[n][2]

	note_colors[n] = (third, second, first)

chord_types = ["Major", "Minor", "Diminished"]

intervals = {
	"Major" : (4,7),
	"Minor" : (3,7),
	"Diminished" : (3,6)
}

#scales = {
	
#}

cmajor_scale = [('C', 'Major'), ('D','Minor'), ('E','Minor'), ('F','Major'), ('G','Major'), ('A', 'Minor'), ('B','Diminished')]

def quit():
	global run
	run = False


def get_triad(root, intervals=(4,7)):

	root_index = notes.index(root)
	third = notes[(root_index + intervals[0]) % len(notes)]
	fifth = notes[(root_index + intervals[1]) % len(notes)]
	
	return (root, third, fifth)

def display_random_chord():

	#random from cmajor scale
	chord = random.choice(cmajor_scale)
	chord_root = chord[0]
	chord_type = chord[1]
	chord_interval = intervals[chord_type]

	chord_notes = get_triad(chord_root, chord_interval)
	chord_colors = [note_colors[note] for note in chord_notes]

	chord_name = chord_root + "-" + chord_type + " : " + str(chord_notes)


	#
	#	Display
	#

	width = 600
	height = 700

	# Create a black image
	img = np.zeros((height,width,3), np.uint8)

	for i, color in enumerate(chord_colors):
		xstart = i * int(width/3)
		xend = (i+1) * int(width/3)
		cv2.rectangle(img,(xstart,0),(xend,height),color,-1)	#negitive thickness to fill

	#display
	cv2.imshow(chord_name,img)
	c = cv2.waitKey(0)
	if 'q' == chr(c & 255):
		quit()
	cv2.destroyAllWindows()


"""
run program
"""

run = True
while run:
	display_random_chord()


