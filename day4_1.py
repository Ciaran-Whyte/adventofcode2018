import re

input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".splitlines()

log = {}
for line in input:
    timestamp, event = re.match(r'\[(.*)\](.*)', line).groups()
    log[timestamp] = event

for key in sorted(log):
    print "{0} -> {1}".format(key, log[key])

guard_sleep = {}

current_guard = None
for key in sorted(log):
    guard_start = re.search(r'\d+', log[key])
    if guard_start is None:
        
