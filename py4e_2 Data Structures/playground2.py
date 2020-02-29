# fname = input("Enter file name: ")
fname = ""
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

count = 0
emails = list()
adlines = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != "From": 
        continue
    count = count + 1
    emails.append(wds[1])

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
