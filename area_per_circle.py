#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: Sep. 21, 2022
# This program calculates and displays the area and perimeter of a
# circle with radius 16 mm.
import math


def main():
    print("For a circle that has a radius")
    print("of 16 mm:")
    print("")
    print("Area = {} mm^2".format(math.pi * 16**2))
    print("Perimeter = {} mm".format(2 * math.pi * 16))


if __name__ == "__main__":
    main()
