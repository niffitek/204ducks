import sys
from math import exp
from calc import *


def check_input():
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("USAGE\n"
              "\t./204yams a\n"
              "\nDESCRIPTION\n"
              "\ta\tconstant")
        sys.exit(0)
    elif len(sys.argv) != 2:
        sys.exit(84)
    try:
        constant = float(sys.argv[1])
    except ValueError:
        sys.exit(84)
    if constant < 0 or constant > 2.5:
        sys.exit(84)
    return constant


def main():
    constant = check_input()
    print_average(constant)
    print("Time after which 50%% of the ducks are back: %dm %02ds" % get_time(time_on_percent(constant, 50)))
    print("Time after which 99%% of the ducks are back: %dm %02ds" % get_time(time_on_percent(constant, 99)))
    print("Percentage of ducks back after 1 minute: %.1f%%" % prob_after_time(constant, 1))
    print("Percentage of ducks back after 2 minutes: %.1f%%" % prob_after_time(constant, 2))
