import sys
from collections import Counter


def read_failures(path):
    counts = Counter()
    with open(path) as log:
        for line in log:
            if "Failed password" not in line:
                continue
            words = line.split()
            if "from" in words:
                ip = words[words.index("from") + 1]
                counts[ip] += 1
    return counts


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile>")
        return
    counts = read_failures(sys.argv[1])
    print("Failed logins by IP address")
    for ip, total in counts.most_common():
        note = ""
        if total >= 3:
            note = "  <- review"
        print(ip, total, note)


if __name__ == "__main__":
    main()
