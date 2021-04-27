import datetime
from yahoo_fin import stock_info as si
from matplotlib import pyplot as plt
import numpy as np
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
if(round(sum(netchange),2) >= 0):
    redgreen1 = "green"
else:
    redgreen1 = "red"
percentchange = []
for i in range(len(netchange)):
    percentchange.append(((float(closeprice[i]) - float(openprice[i])) / float(openprice[i])) * 100)
if(round(sum(percentchange),2) >= 0):
    redgreen2 = "green"
else:
    redgreen2 = "red"
cdata = open('commentdata.txt','r')
Lines = cdata.readlines()
commentdata = []
for line in Lines:
    data = line.strip().split()
    commentdata.append(float(data[0]))
cdata.close()
ddata = open('datedata.txt','r')
Lines = ddata.readlines()
datedata = []
for line in Lines:
    data = line.strip().split()
    prettydate = data[0]
    datedata.append(prettydate[5:7] + "/" + prettydate[8:10] + "/"  + prettydate[0:4])
ddata.close()
if(commentdata[len(commentdata)-1] >= commentdata[len(commentdata)-2]):
    redgreen3 = "green"
else:
    redgreen3 = "red"
netdata = open('netchangedata.txt','a+')
netdata.write(str(round(sum(percentchange),2)) + "\n")
netdata.close()
netchangedata = open('netchangedata.txt','r')
Lines = netchangedata.readlines()
percentchangedata = []
for line in Lines:
    data = line.strip().split()
    percentchangedata.append(float(data[0]))
netchangedata.close()

nasdaqdata = open('nasdaqdata.txt','r')
Lines = nasdaqdata.readlines()
nasdaqchangedata = []
for line in Lines:
    data = line.strip().split()
    nasdaqpercchange = ((float(data[1]) - float(data[0])) / float(data[0])) * 100
    nasdaqchangedata.append(nasdaqpercchange)
netchangedata.close()

plt.figure(1)
plt.title('Total # of Daily Comments')
plt.ylabel('# of Comments')
plt.xlabel('Date')
plt.bar(datedata,commentdata,width=1,edgecolor = "black",color=redgreen3)
plt.gcf().autofmt_xdate()
plt.savefig("commentsgraph.png")
plt.show()

plt.figure(2)
plt.title('Total % change of Top 5 Most Mentioned Stocks over time')
plt.ylabel('% Change')
plt.xlabel('Date')
negative_data = []
positive_data = []
for i in range(len(percentchangedata)):
    if(percentchangedata[i] > 0):
        positive_data.append(percentchangedata[i])
        negative_data.append(0)
    else:
        negative_data.append(percentchangedata[i])
        positive_data.append(0)
ax = plt.subplot(111)
ax.bar(datedata, negative_data,width=.85,edgecolor = "black",color='red')
ax.bar(datedata, positive_data,width=.85,edgecolor = "black",color='green')
plt.gcf().autofmt_xdate()
plt.savefig("netchangegraph.png")
plt.show()

plt.figure(3)
plt.title('Total % change of NASDAQ over time')
plt.ylabel('% Change')
plt.xlabel('Date')
negative_data = []
positive_data = []
for i in range(len(nasdaqchangedata)):
    if(nasdaqchangedata[i] > 0):
        positive_data.append(nasdaqchangedata[i])
        negative_data.append(0)
    else:
        negative_data.append(nasdaqchangedata[i])
        positive_data.append(0)
ax = plt.subplot(111)
ax.bar(datedata, negative_data,width=.85,edgecolor = "black",color='red')
ax.bar(datedata, positive_data,width=.85,edgecolor = "black",color='green')
plt.gcf().autofmt_xdate()
plt.savefig("nasdaqchangegraph.png")
plt.show()
f = open('index.html','w')
html = """<!DOCTYPE html>
<html>
<head></head>
<style>
h1{
  text-align: center;
  font-size: 45px;
}
h2{
  color: red;
  font-size: 35px;
}
h3{
  font-size:30px;
}
p{
  font-size: 20px;
}
text{
  font-size: 25px;
  text-align: center;
}
</style>
<body>
<h1> r/wallstreetbets Top 5 Most Discussed Stocks of the Day on """ + date[5:7] + "/" + date[8:10] + "/"  + date[0:4] + """:</h1>
<text>This website updates daily at 4:02pm and displays the top 5 most mentioned
stocks from the Daily Discussion thread of the wallstreetbets subreddit.
The goal of this website is to track the overall growth of this subreddit and
visualize the impact the dicussions have on the stock market.
Every day the total number of comments parsed through will be graphed to demonstrate
the growth in popularity of this subreddit as a primary way of communicating about
different stocks. Also, the net change in price of all 5 of the top mentioned
stocks will be recorded and graphed daily.</text>
<div id = "ticker1">
    <h2>1. """ + toptickers[0] + """</h2>
    <p>As of 9:15am """ + toptickers[0] + """ had """ + str(tickermentions[0]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[0] + """ was valued at: $""" + str(openprice[0]) + """ and at market close """ + toptickers[0] + """ was valued at: $""" + str(closeprice[0]) + """. The total change in price throughout the day was: $""" + str(round(netchange[0],2)) + """ this is a """ + str(round(percentchange[0],2)) + """% change in price throughout the day.</p>
</div>
<div id = "ticker2">
    <h2>2. """ + toptickers[1] + """</h2>
    <p>As of 9:15am """ + toptickers[1] + """ had """ + str(tickermentions[1]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[1] + """ was valued at: $""" + str(openprice[1]) + """ and at market close """ + toptickers[1] + """ was valued at: $""" + str(closeprice[1]) + """. The total change in price throughout the day was: $""" + str(round(netchange[1],2)) + """ this is a """ + str(round(percentchange[1],2)) + """% change in price throughout the day.</p>
</div>
<div id = "ticker3">
    <h2>3. """ + toptickers[2] + """</h2>
    <p>As of 9:15am """ + toptickers[2] + """ had """ + str(tickermentions[2]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[2] + """ was valued at: $""" + str(openprice[2]) + """ and at market close """ + toptickers[2] + """ was valued at: $""" + str(closeprice[2]) + """. The total change in price throughout the day was: $""" + str(round(netchange[2],2)) + """ this is a """ + str(round(percentchange[2],2)) + """% change in price throughout the day.</p>
</div>
<div id = "ticker4">
    <h2>4. """ + toptickers[3] + """</h2>
    <p>As of 9:15am """ + toptickers[3] + """ had """ + str(tickermentions[3]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[3] + """ was valued at: $""" + str(openprice[3]) + """ and at market close """ + toptickers[3] + """ was valued at: $""" + str(closeprice[3]) + """. The total change in price throughout the day was: $""" + str(round(netchange[3],2)) + """ this is a """ + str(round(percentchange[3],2)) + """% change in price throughout the day.</p>
</div>
<div id = "ticker5">
    <h2>5. """ + toptickers[4] + """</h2>
    <p>As of 9:15am """ + toptickers[4] + """ had """ + str(tickermentions[4]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[4] + """ was valued at: $""" + str(openprice[4]) + """ and at market close """ + toptickers[4] + """ was valued at: $""" + str(closeprice[4]) + """. The total change in price throughout the day was: $""" + str(round(netchange[4],2)) + """ this is a """ + str(round(percentchange[4],2)) + """% change in price throughout the day.</p>
</div>
<h3>Net profit of all 5 stocks: $<span style="color:""" + redgreen1 + """">""" + str(round(sum(netchange),2)) + """</span></h3>
<h3>Net percent change of all 5 stocks: <span style="color:""" + redgreen2 + """">""" + str(round(sum(percentchange),2)) + """%</span></h3>
<img src='commentsgraph.png'>
<img src='netchangegraph.png'>
<img src='nasdaqchangegraph.png'>
</body>
</html>"""
f.write(html)
f.close()
