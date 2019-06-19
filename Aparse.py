import argparse
import math

parser = argparse.ArgumentParser(description="Calculate Volume of a cylinder")
parser.add_argument('-r', '--radius', type = int, required=True,  help="Radius of cylinder")
parser.add_argument('-H', '--height', type = int, required=True,  help='Height of cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

# The parser can be called from the command line. Entering python, modulename.py -h brings up the help
# menu. This is titled with the description defined in argument parser.
# Add an argument by add_argument. Then '-x', '--name' introduces an argument 'name' that can be input
# From the command line by -x. Type must be specified since default is string. The required clause
# prevents the program from running unless the argument is specified. The help part adds the variable
# to the help screen under the associated title.

# Mutually exclusive commands can be added to the parser by add_mutually_exclusive group.
# action = 'store_true' makes false default value, making true if called from command line
# args = parser.parse_args() stores the values of the arguments in a variable that can be used by code.


def cylinder_volume(radius, height):
    vol = math.pi * (radius ** 2) * height
    return vol


if __name__ == '__main__':   # When a module is called from command line, it initiates the function main.
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:  # Note clauses must be mutually exclusive.
        print('The volume of a cylinder with radius %s and height %s is %s' % (args.radius, args.height, volume))
    else:
        print('The volume of the cylinder is %s' % volume)  # % Method simplifies concatenating strings, numbers.

# Verbose and quiet are common argparse variables, used to provide a lot or very little information.



