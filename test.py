import time
import argparse

# Add command line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="Test parameter (optional)")
parser.add_argument("-r", "--required", help="Test parameter (required)")
args = parser.parse_args()

print("Args: " + str(args))

print("Starting test...")
i = 0
while(True):
	print("Cycle: " + str(i))
	i = i+1
	time.sleep(5)
