#!/usr/bin/env python
# Towers of hanoi.
import os
import time
import sys
import optparse


def solve_hanoi(n, timestep, silent, debug):
    try:
        tower
    except NameError:
        global tower
        tower = Tower(n)

    if n == 0:
        return
    else:
        if debug: print "###### SOLVING FOR ", n-1, " ###################"
        solve_hanoi(n-1, timestep, silent, debug)
        if debug: print "###### MOVING DISK ", n-1, " ###################"
        tower.move_disc(n-1, debug)
        if timestep:
            print "sleeping....ZZzzzz..", timestep
            time.sleep(timestep)
        if not silent:
            #os.system('clear')
            #tower.pretty_print()
            tower.compact_print()
        if debug: print "###### SOLVING FOR ", n-1, " ###################"
        solve_hanoi(n-1, timestep, silent, debug)

class Tower:
    def __init__(self, size):
        self.size = size
        self.moves = 0
        self.towers = { 0: [], 1: [], 2: [] }
        for i in range (self.size-1, -1, -1):
            self.towers[0].append(i)
    
    def move_disc(self, disc_number, debug):
        for t in range(0,3):
            if disc_number in self.towers[t]:
                if debug: print "###### Tower, Piece: ", t, disc_number
                if disc_number == 0:
                    if debug:  print "popping piece ", disc_number, " from tower ", t
                    self.towers[t].pop()
                    if debug: print "towers: ", self.towers
                    if debug: print "putting piece ", disc_number, " on tower", (t+1)%3
                    self.towers[(t+1)%3].append(disc_number)
                    if debug: print "towers: ", self.towers
                    break
                else:
                    if debug: print "popping piece ", disc_number, " from tower ", t
                    self.towers[t].pop()
                    if len(self.towers[(t+1)%3]) == 0 or self.towers[(t+1)%3][-1] > disc_number:
                        if debug: print "putting piece ", disc_number, " on tower", (t+1)%3
                        self.towers[(t+1)%3].append(disc_number)
                        if debug: print "towers: ", self.towers
                    else:
                        if debug: print "putting piece ", disc_number, " on tower", (t+2)%3
                        self.towers[(t+2)%3].append(disc_number)
                        if debug: print "towers: ", self.towers
                    break
        self.moves += 1

    def pretty_print(self):
        print "#### CURRENT TOWERS ####"
        for t in self.towers:
            print self.towers[t]
        print "move: ", self.moves
        print "########################"

    def compact_print(self):
        print "towers: ", self.towers, "moves: ", self.moves



parser = optparse.OptionParser()
parser.add_option('-n', '--number', help='number of discs in the tower', type='int', dest='size', default=5)
parser.add_option('-d', '--debug', help='adds debug output', dest='debug', default=False, action='store_true')
parser.add_option('-s', '--silent', help='only print the resulting tower config', dest='silent', default=False, action='store_true')
parser.add_option('-t', '--timestep', help='adds timestepping in seconds. can use float for subseconds',
        dest='timestep', metavar='TIMESTEP', type='float')
(options, args) = parser.parse_args()

solve_hanoi(options.size, options.timestep, options.silent, options.debug)
print "## FINAL CONFIG ##"
tower.compact_print()
