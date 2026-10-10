# Python Log Analyzer

A small Python script that reads an SSH authentication log and counts failed logins by IP address. Any address with three or more failures is flagged for review.

## Usage

```
python analyzer.py sample_auth.log
```

## Example output

```
Failed logins by IP address
203.0.113.45 3   <- review
198.51.100.7 2
192.0.2.10 1
203.0.113.99 1
```

## How it works

The script scans each line for "Failed password", pulls the IP address that follows the word "from", and tallies the totals with collections.Counter.

## Notes

The sample log uses reserved documentation IP addresses and contains no real data.

## Ideas for next steps

- Count failures per username
- Group attempts by hour
- Export the results to CSV
# python-log-analyzer
Small Python script that scans an authentication logand reports failed logins by IP address.
