#!/usr/bin/env python
import os
import time
import sys
import optparse
# Towers of hanoi.

def solve_hanoi(n, timestep, debug=False):
    global counter
    if n == 0:
        #move_disk(0)
        return
    else:
        if debug: print "###### SOLVING FOR ", n-1, " ###################"
        solve_hanoi(n-1, timestep, debug)
        if debug: print "###### MOVING DISK ", n-1, " ###################"
        move_disk(n-1, debug)
        if timestep:
            print "sleeping....ZZzzzz..", timestep
            time.sleep(timestep)
        counter += 1
        os.system('clear')
        print "#### CURRENT TOWERS ####"
        for t in towers:
            print towers[t]
        print "move: ", counter
        print "########################"
        if debug: print "###### SOLVING FOR ", n-1, " ###################"
        solve_hanoi(n-1, timestep, debug)

def move_disk(n, debug=False):
    for t in range(0,3):
        if n in towers[t]:
            if debug: print "###### Tower, Piece: ", t, n
            if n == 0:
                if debug:  print "popping piece ", n, " from tower ", t
                towers[t].pop()
                if debug: print "towers: ", towers
                if debug: print "putting piece ", n, " on tower", (t+1)%3
                towers[(t+1)%3].append(n)
                if debug: print "towers: ", towers
                break
            else:
                if debug: print "popping piece ", n, " from tower ", t
                towers[t].pop()
                if len(towers[(t+1)%3]) == 0 or towers[(t+1)%3][-1] > n:
                    if debug: print "putting piece ", n, " on tower", (t+1)%3
                    towers[(t+1)%3].append(n)
                    if debug: print "towers: ", towers
                else:
                    if debug: print "putting piece ", n, " on tower", (t+2)%3
                    towers[(t+2)%3].append(n)
                    if debug: print "towers: ", towers
                break

parser = optparse.OptionParser()
parser.add_option('-n', '--number', help='number of discs in the tower', type='int', dest='size', default=5)
parser.add_option('-d', '--debug', help='adds debug output', dest='debug', default=False, action='store_true')
parser.add_option('-t', '--timestep', help='adds timestepping in seconds. can use float for subseconds',
        dest='timestep', metavar='TIMESTEP', type='float')
(options, args) = parser.parse_args()

#debug
print "options: ", options
print args

size = options.size
debug = options.debug
timestep = options.timestep
print size
print debug
print timestep
  
# generate towers:
towers = { 0: [], 1: [], 2: [] }
for i in range (size-1,-1,-1):
    towers[0].append(i)
counter = 0
solve_hanoi(size, timestep, debug)
print "## FINAL CONFIGURATION ##: ", towers
