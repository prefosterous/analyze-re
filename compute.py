import sys

threshold = float(sys.argv[1])
limit = float(sys.argv[2])

total = 0.0
for line in sys.stdin:
    output = max(0.0, float(line) - threshold)
    print("{:.1f}".format(output))
    total += output

print(total)
