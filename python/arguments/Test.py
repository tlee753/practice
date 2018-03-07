import argparse

parser = argparse.ArgumentParser(description="Test script help message")

parser.add_argument('--test', action='store_true', dest='variable', default=False)

options = parser.parse_args()

print(options.variable)
