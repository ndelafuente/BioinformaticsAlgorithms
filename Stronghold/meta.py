import sys

args = sys.argv[1:]

problems = [int(arg) for arg in args]

for n in problems:
    print(f"Problem {n} Output: ")
    __import__(f'p{n}')
    print()
    