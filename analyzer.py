import csv
import sys
from collections import Counter


def read_failures(path):
    by_ip = Counter()
    by_user = Counter()
    with open(path) as log:
        for line in log:
            if "Failed password" not in line:
                continue
            words = line.split()
            if "from" in words:
                ip = words[words.index("from") + 1]
                by_ip[ip] += 1
            if "for" in words:
                pos = words.index("for") + 1
                if words[pos] == "invalid":
                    pos += 2
                by_user[words[pos]] += 1
    return by_ip, by_user


def print_report(title, counts):
    print(title)
    for name, total in counts.most_common():
        note = ""
        if total >= 3:
            note = "  <- review"
        print(name, total, note)
    print()


def save_csv(path, by_ip, by_user):
    with open(path, "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["type", "name", "failures"])
        for ip, total in by_ip.most_common():
            writer.writerow(["ip", ip, total])
        for user, total in by_user.most_common():
            writer.writerow(["user", user, total])


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile> [--csv output.csv]")
        return
    by_ip, by_user = read_failures(sys.argv[1])
    print_report("Failed logins by IP address", by_ip)
    print_report("Failed logins by username", by_user)
    if len(sys.argv) >= 4 and sys.argv[2] == "--csv":
        save_csv(sys.argv[3], by_ip, by_user)
        print("Saved results to", sys.argv[3])


if __name__ == "__main__":
    main()
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
