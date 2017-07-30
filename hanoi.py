#!/usr/bin/env python
# Towers of hanoi.
import os
import time
import sys
import optparse


def solve_hanoi(n, tower):
    if n == 0:
        return
    else:
        if options.debug: print
        if options.debug: print
        if options.debug: print "###### SOLVING FOR ", n, " ###################"
        solve_hanoi(n-1, tower)
        tower.move_disc(n-1)
        tower.display()
        solve_hanoi(n-1, tower)

class Tower:
    def __init__(self):
        self.size = int(options.size)
        self.timestep = options.timestep
        self.silent = options.silent
        self.compact = options.compact
        self.moves = 0
        self.towers = { 0: [], 1: [], 2: [] }
        for i in range (self.size-1, -1, -1):
            self.towers[0].append(i)
    
    def move_disc(self, disc_number):
        if options.debug: print "###### MOVING DISK ", disc_number, " ###################"
        for t in range(0,3):
            if disc_number in self.towers[t]:
                if options.debug: print "###### Tower, Piece: ", t, disc_number
                if disc_number == 0:
                    if options.debug:  print "popping piece ", disc_number, " from tower ", t
                    self.towers[t].pop()
                    if options.debug: print "towers: ", self.towers
                    if options.debug: print "putting piece ", disc_number, " on tower", (t+1)%3
                    self.towers[(t+1)%3].append(disc_number)
                    if options.debug: print "towers: ", self.towers
                    break
                else:
                    if options.debug: print "popping piece ", disc_number, " from tower ", t
                    self.towers[t].pop()
                    if len(self.towers[(t+1)%3]) == 0 or self.towers[(t+1)%3][-1] > disc_number:
                        if options.debug: print "putting piece ", disc_number, " on tower", (t+1)%3
                        self.towers[(t+1)%3].append(disc_number)
                        if options.debug: print "towers: ", self.towers
                    else:
                        if options.debug: print "putting piece ", disc_number, " on tower", (t+2)%3
                        self.towers[(t+2)%3].append(disc_number)
                        if options.debug: print "towers: ", self.towers
                    break
        if self.timestep:
            time.sleep(self.timestep)
        self.moves += 1


    def display(self):
        if not self.silent:
            if self.compact:
                self.__compact_print()
            else:
                self.__pretty_print()

    def __pretty_print(self):
        if not options.debug:
            os.system('clear')
        print "#### CURRENT TOWERS ####"
        for t in self.towers:
            print self.towers[t]
        print "move: ", self.moves
        print "########################"
        if self.timestep and options.debug:
            print "sleeping....ZZzzzz..", self.timestep

    def __compact_print(self):
        print "towers: ", self.towers, "moves: ", self.moves



parser = optparse.OptionParser()
parser.add_option('-n', '--number', help='number of discs in the tower', type='int', dest='size', default=5)
parser.add_option('-d', '--debug', help='adds debug output', dest='debug', default=False, action='store_true')
parser.add_option('-s', '--silent', help='only print the resulting tower config', dest='silent', default=False, action='store_true')
parser.add_option('-c', '--compact', help='print compact output, othwerwise "animated"', dest='compact', default=False, action='store_true')
parser.add_option('--stats', help='print statistics about the solve', dest='stats', default=False, action='store_true')
parser.add_option('-t', '--timestep', help='adds timestepping in seconds. can use float for subseconds',
        dest='timestep', metavar='TIMESTEP', type='float')
(options, args) = parser.parse_args()

size = int(options.size)

tower = Tower()
if options.stats:
    start_time = time.clock()
    solve_hanoi(options.size, tower)
    running_time = time.clock() - start_time
    print "Number of discs: ", options.size
    print "Running time was: ", running_time
    print "Total number of moves: ", 2**options.size - 1, " (2^" + str(options.size) + "-1)"
    print "Number of moves/second: ", (2**options.size - 1)/running_time
else:
    solve_hanoi(options.size, tower)
    print "## FINAL CONFIG ##"
tower.display()
