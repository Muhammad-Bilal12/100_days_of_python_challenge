import argparse

parser = argparse.ArgumentParser()

# Add Command Line arguments
parser.add_argument("url",help="Url of the file to download")
parser.add_argument("output",help="By which name do you want to save your file")

# Parse the arguments
args = parser.parse_args()

# use the arguments in your code


print(args.url)
print(args.output)
