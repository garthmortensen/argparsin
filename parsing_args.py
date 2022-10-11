import argparse
import operator
import functools

parser = argparse.ArgumentParser(description='Applies an operation to one or more numbers')

parser.add_argument("number",  # positional args use just the name of the argument
                    help="One or more numbers to perform an operation on.",
                    nargs='+',  # how many times we expect the arg to be specified, + means x >= 1
                    type=int)  # convert args to ints

parser.add_argument('-o', '--operation',  # the option
                    help="The operation to perform on numbers.",
                    choices=['add', 'sub', 'mul', 'div'],
                    default='add')  # if no option, default on addition

# best practice is prints only the result
# verbose is used to set logging detail level. This script does not contain logging functionality
parser.add_argument("-v", "--verbose",
                    action="store_true",
                    help="increase output verbosity")

# parse the CL options, and get result back into the opts object
opts = parser.parse_args()

# perform the expected operation on the numbers set, print result
operation = getattr(operator, opts.operation)
print(functools.reduce(operation, opts.number))
