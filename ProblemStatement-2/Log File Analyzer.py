import re
from collections import defaultdict, Counter

LOG_FILE = "path"

log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) \S+'
)

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

def analyze_log(log_file):
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()

    with open(log_file, 'r') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if parsed_line:
                ip_counter[parsed_line['ip']] += 1
                url_counter[parsed_line['url']] += 1
                status_counter[parsed_line['status']] += 1

    return ip_counter, url_counter, status_counter

def generate_report(ip_counter, url_counter, status_counter):
    print("Top 10 IP Addresses with the Most Requests:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count} requests")

    print("\nTop 10 Most Requested URLs:")
    for url, count in url_counter.most_common(10):
        print(f"{url}: {count} requests")

    print("\nNumber of 404 Errors:")
    print(f"404 errors: {status_counter['404']} occurrences")

def main():
    ip_counter, url_counter, status_counter = analyze_log(LOG_FILE)
    generate_report(ip_counter, url_counter, status_counter)

if __name__ == "__main__":
    main()
