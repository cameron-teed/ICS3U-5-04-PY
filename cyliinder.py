#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Nov 2019
# This program calculates volume of a cylinder

import math


def volume_calculator(radius, height):
    # calculates the volume

    # process
    volume = math.pi * radius * radius * height
    return round(volume, 2)


def main():
    # This is asks for the user input

    # Welcomes user
    print("This program calculates the volume of a cylinder. ")

    while True:
        try:
            # input
            radius = float(input("What is the radius: "))
            height = float(input("What is the height: "))
            # runs volume_calculator()
            volume = volume_calculator(height=height, radius=radius)
            # output
            print("\nThe volume is " + str(volume) + " units cubed.")
            break

        except ValueError:
            print("Please put in integer.\n")


if __name__ == "__main__":
    main()
