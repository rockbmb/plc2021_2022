import re
import sys

for line in sys.stdin:
    if m := re.match(r'([^a]|a[^a]*a[^a]*)*$', line):
        print("Ok!")