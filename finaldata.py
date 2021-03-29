import datetime
input = open("marketopen.txt", "r")
toptickers = []
tickermentions = []
openprice = []
Lines = input.readlines()
for line in Lines:
    data = line.strip().split()
    toptickers.append(data[0])
    tickermentions.append(data[1])
    comments = data[2]
    openprice.append(data[3])
input.close()
input2 = open("marketclose.txt", "r")
closeprice = []
Lines = input2.readlines()
for line in Lines:
    closedata = line.strip().split()
    closeprice.append(closedata[0])
input2.close()
output = open("finaldata.txt","a+")
date = str(datetime.datetime.now())
output.write("Taken from wallstreetbets subreddit Daily Discussion Thread on " + date[0:10] + "\n" + "\n")
netchange = []
for i in range(len(toptickers)):
    if(i == 5):
        break
    else:
        output.write(str(toptickers[i]) + " - " + str(tickermentions[i]) + " mentions in " + str(comments) + " comments." + "\n")
        totalchange = float(closeprice[i]) - float(openprice[i])
        netchange.append(totalchange)
        output.write(str(toptickers[i]) + "s price data on market open: $" + str(openprice[i]) + " and $" + str(closeprice[i]) + " on market close. Total Change: " + str(round(totalchange,2)) + "\n\n")
output.write("Total increase in top mentioned stocks: $" + str(round(sum(netchange),2)) + "\n")
output.write("------------------------------------------------------------------------------------------" + "\n")
output.close()


#email t&i about davidson domains
#sequel light database
