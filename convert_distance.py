
import argparse
import operator
import functools


def convert_to_mile(distance):
    """convert a distance from miles to km ot km to miles."""
    print(f"{distance} km in miles is {distance / 1.6}")


def convert_to_kilometer(distance):
    """convert a distance from miles to km ot km to miles."""
    print(f"{distance} miles in km is {distance * 1.6}")


parser = argparse.ArgumentParser(description='Convert a distance from kilometers to miles or miles to kilometers.')

parser.add_argument("distance",  # positional args use just the name of the argument
                    help="Input the distance",
                    # nargs='1',  # how many times we expect the arg to be specified, + means x >= 1
                    type=float)

parser.add_argument('-c', '--conversion',  # the option
                    help="Define which distance measure (`mile` or `km`) you want to convert to.",
                    choices=['mile', 'km'],
                    default='km')  # if no option, default on addition

# parse the CL options, and get result back into the opts object
opts = parser.parse_args()

if opts.conversion == "mile":
    convert_to_mile(opts.distance)

if opts.conversion == "km":
    convert_to_kilometer(opts.distance)

# perform the expected operation on the numbers set, print result
operation = getattr(operator, opts.operation)
print(functools.reduce(operation, opts.number))
