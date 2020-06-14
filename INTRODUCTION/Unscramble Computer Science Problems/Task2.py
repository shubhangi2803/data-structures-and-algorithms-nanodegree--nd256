"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phtime={}
for call_log in calls:
    phtime[call_log[0]]=phtime.get(call_log[0],0)+int(call_log[3])
    phtime[call_log[1]]=phtime.get(call_log[1],0)+int(call_log[3])
maxtime=0
maxnum=None
for num in phtime:
    if phtime[num]>maxtime:
        maxtime=phtime[num]
        maxnum=num
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxnum,maxtime))
