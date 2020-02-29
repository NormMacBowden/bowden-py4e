fname = "mbox-short.txt"
fh = open(fname)

hours = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != "From": 
        continue
    hr = (wds[5].split(":"))[0]
    hours.append(hr)

hrcount = dict()
for h in hours:
    hrcount[h] = hrcount.get(h,0) + 1

sorthr = sorted([ (k,v) for k,v in hrcount.items()])

for i,f in sorthr:
    print(i,f)

a = [38,267,331,316,177,105,95,54,33,19,8,7]
print(sum(a))

"""
emailsDic = dict()
for email in emails:
        emailsDic[email] = emailsDic.get(email, 0) + 1

bigcount = None
bigword = None
for k,v in emailsDic.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigword = k

# print("There were", count, "lines in the file with From as the first word")
print(bigword, bigcount)
"""