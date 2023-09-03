import argparse

def say_hello(name="Mario Lerma"):
print("Hello ", name, "!")

parser = argparse.ArgumentParser(description='Say hello.')
parser.add_argument('--name', type=str, required=False,
metavar='name', help='your name', default='World')
args = parser.parse_args()
say_hello(args.name)
