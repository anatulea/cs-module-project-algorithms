#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  for i in ['r','s', 'p']:
        for j in ['r','s', 'p']:
          print([i, j])

rock_paper_scissors(3)
# if __name__ == "__main__":
  # if len(sys.argv) > 1:
  #   num_plays = int(sys.argv[1])
  #   print(rock_paper_scissors(num_plays))
  # else:
  #   print('Usage: rps.py [num_plays]')