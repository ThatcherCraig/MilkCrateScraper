input = open("alltickers.txt", "r")
tickernames = []
Lines = input.readlines()
for line in Lines:
    tickerinfo = line.strip().split()
    if(len(tickerinfo) > 1):
        tickernames.append(tickerinfo[0])
input.close()
print(tickernames)
