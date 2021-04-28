import sys

try:
    threshold = float(sys.argv[1])
    limit = float(sys.argv[2])
except:
    sys.exit("Invalid command line arguments. This script requires two numeric arguments as input.")

total = 0.0

try:
    for line in sys.stdin:
        output = max(0.0, float(line) - threshold)
        if (total + output > limit):
            output = limit - total
        print("{:.1f}".format(output))
        total += output

    print("{:.1f}".format(total))

except:
    sys.exit("An error occurred while reading or processing the data. Make sure your input file is formatted correctly.")
