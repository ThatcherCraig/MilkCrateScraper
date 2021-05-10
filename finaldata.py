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
date = str(datetime.datetime.now())
netchange = []
for i in range(len(toptickers)):
    if(i == 5):
        break
    else:
        totalchange = float(closeprice[i]) - float(openprice[i])
        netchange.append(totalchange)
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
print(percentchange)
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
profanity = open('profanitycount.txt','r')
Lines = profanity.readlines()
profanitycount = []
for line in Lines:
    data = line.strip().split()
    profanitycount.append(int(data[0]))
cdata.close()
plt.figure(1)
plt.title('Total # of Daily Comments over time')
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
plt.figure(4)
plt.title('Total % change of Top 5 mentioned stocks')
plt.ylabel('% Change')
plt.xlabel('Most mentioned tickers from left to right')
plt.bar(toptickers,percentchange,width=1,edgecolor = "black",color="blue")
plt.savefig("tickerpricechanges.png")
plt.show()

markettime = ["9:30","4:00"]
plt.figure(5)
plt.title(toptickers[0] + "'s Change in Price Throughout Day")
plt.ylabel('Price')
plt.xlabel('Time')
ticker1data = [openprice[0],closeprice[0]]
if(closeprice[0] > openprice[0]):
    color = "green"
else:
    color = "red"
    plt.gca().invert_yaxis()
plt.plot(markettime,ticker1data,color=color)
plt.gcf().autofmt_xdate()
plt.savefig("ticker1.png")
plt.show()

plt.figure(6)
plt.title(toptickers[1] + "'s Change in Price Throughout Day")
plt.ylabel('Price')
plt.xlabel('Time')
ticker2data = [openprice[1],closeprice[1]]
if(closeprice[1] > openprice[1]):
    color = "green"
else:
    color = "red"
    plt.gca().invert_yaxis()
plt.plot(markettime,ticker2data,color=color)
plt.gcf().autofmt_xdate()
plt.savefig("ticker2.png")
plt.show()


plt.figure(7)
plt.title(toptickers[2] + "'s Change in Price Throughout Day")
plt.ylabel('Price')
plt.xlabel('Time')
ticker3data = [openprice[2],closeprice[2]]
if(closeprice[2] > openprice[2]):
    color = "green"
else:
    color = "red"
    plt.gca().invert_yaxis()
plt.plot(markettime,ticker3data,color=color)
plt.gcf().autofmt_xdate()
plt.savefig("ticker3.png")
plt.show()

plt.figure(8)
plt.title(toptickers[3] + "'s Change in Price Throughout Day")
plt.ylabel('Price')
plt.xlabel('Time')
ticker4data = [openprice[3],closeprice[3]]
if(closeprice[3] > openprice[3]):
    color = "green"
else:
    color = "red"
    plt.gca().invert_yaxis()
plt.plot(markettime,ticker4data,color=color)
plt.gcf().autofmt_xdate()
plt.savefig("ticker4.png")
plt.show()


plt.figure(9)
plt.title(toptickers[4] + "'s Change in Price Throughout Day")
plt.ylabel('Price')
plt.xlabel('Time')
ticker5data = [openprice[4],closeprice[4]]
if(closeprice[4] > openprice[4]):
    color = "green"
else:
    color = "red"
    plt.gca().invert_yaxis()
plt.plot(markettime,ticker5data,color=color)
plt.savefig("ticker5.png")
plt.show()



f = open('index.html','w')
html = """
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
</head>
<style>
body{
    background-color: rgb(60,79,118);
}
h1{
  text-align: center;
  font-size: 45px;
  color: white;
}
h2{
  color: blue;
  font-size: 35px;
}
h3{
  font-size:30px;
}
p{
  font-size: 20px;
}
text{
  font-size: 20px;
  text-align: center;
}
/* Set height of the grid so .sidenav can be 100% (adjust if needed) */
.row.content{
  height: 100%;
  margin-bottom: -20px;
}
.row.title{
  background-color: rgb(60,79,118);
  height: auto;
}
.row-height {
    height: auto;
}
.col-md-3{
  height: 100%;
  background-color: rgb(60,79,118);
}
.col-12{
  height: 100%;
  background-color: rgb(221,219,241);
}
.col-xs-12{
  height: auto;
  background-color: rgb(221,219,241);
}
img {
  align-items: center;
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 100%;
  height: auto;
}
button{
  background-color: rgb(221,219,241);
  color: rgb(60,79,118);
  font-size: 20px;
}
    /* On small screens, set height to 'auto' for sidenav and grid */

</style>
<script>
function aboutPage() {
  alert("This website updates daily at 4:02pm and displays the top 5 most mentioned stocks from the Daily Discussion thread of the wallstreetbets subreddit. This is accomplished by a python script that works in the background and uses PRAW, a python library made for scraping subreddits. The script parses through every comment in the daily discussion thread and cross references every word in each comment with every stock ticker that is listed on the NASDAQ stock exchange. After that the price of those 5 stocks is collected at market open and market close. The data is then graphed using matplotlib, a python library designed for graphing different data sets. The goal of this website is to track the overall growth of this subreddit and visualize the impact these discussions have on the stock market. Every day the total number of comments parsed through will be graphed to demonstrate the growth in popularity of this subreddit as a primary way of communicating about different stocks. Also, the net percent change of all 5 of the top mentioned stocks will be recorded and graphed daily and compared to a graph of the NASDAQ index\’s daily net percent change. Thus far, daily data from this subreddit has been collected and accurately displayed since 4/26/21. *as an added bonus wallstreetbets is well known for their significant use of expletives so I have added a counter that counts how many swears were used throughout all of the comments parsed through on that day.");
}
</script>
<body>


  <div class="container-fluid">
    <div class="row title">
    <h1> r/wallstreetbets Top 5 Most Discussed Stocks of the Day on """ + date[5:7] + "/" + date[8:10] + "/"  + date[0:4] + """: <br><br><button onclick="aboutPage()">Project Description</button></h1>
    </div>
    <div class="row content">
      <div class="hidden-sm hidden-xs col-md-3 col-lg-3 col-xl-3">
      </div>
      <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-6">
      <h2>1. """ + toptickers[0] + """</h2>
      <h5>""" + str(tickermentions[0]) + """ mentions in """ + str(comments) + """ comments</h5>
      <p>As of 9:15am """ + toptickers[0] + """ had """ + str(tickermentions[0]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[0] + """ was valued at: $""" + str(openprice[0]) + """ and at market close """ + toptickers[0] + """ was valued at: $""" + str(closeprice[0]) + """. The total change in price throughout the day was: $""" + str(round(netchange[0],2)) + """ this is a """ + str(round(percentchange[0],2)) + """% change in price throughout the day.
      </p>
      <img src='ticker1.png'>
      <br><br>
      <hr>
      <h2>2. """ + toptickers[1] + """</h2>
      <h5>""" + str(tickermentions[1]) + """ mentions in """ + str(comments) + """ comments</h5>
      <p>As of 9:15am """ + toptickers[1] + """ had """ + str(tickermentions[1]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[1] + """ was valued at: $""" + str(openprice[1]) + """ and at market close """ + toptickers[1] + """ was valued at: $""" + str(closeprice[1]) + """. The total change in price throughout the day was: $""" + str(round(netchange[1],2)) + """ this is a """ + str(round(percentchange[1],2)) + """% change in price throughout the day.
      </p>
      <img src='ticker2.png'>
      <br><br>
      <hr>
      <h2>3. """ + toptickers[2] + """</h2>
      <h5>""" + str(tickermentions[2]) + """ mentions in """ + str(comments) + """ comments</h5>
      <p>As of 9:15am """ + toptickers[2] + """ had """ + str(tickermentions[2]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[2] + """ was valued at: $""" + str(openprice[2]) + """ and at market close """ + toptickers[0] + """ was valued at: $""" + str(closeprice[2]) + """. The total change in price throughout the day was: $""" + str(round(netchange[2],2)) + """ this is a """ + str(round(percentchange[2],2)) + """% change in price throughout the day.
      </p>
      <img src='ticker3.png'>
      <br><br>
      <hr>
      <h2>4. """ + toptickers[3] + """</h2>
      <h5>""" + str(tickermentions[3]) + """ mentions in """ + str(comments) + """ comments</h5>
      <p>As of 9:15am """ + toptickers[3] + """ had """ + str(tickermentions[3]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[3] + """ was valued at: $""" + str(openprice[3]) + """ and at market close """ + toptickers[3] + """ was valued at: $""" + str(closeprice[3]) + """. The total change in price throughout the day was: $""" + str(round(netchange[3],2)) + """ this is a """ + str(round(percentchange[3],2)) + """% change in price throughout the day.
      </p>
      <img src='ticker4.png'>
      <br><br>
      <hr>
      <h2>5. """ + toptickers[4] + """</h2>
      <h5>""" + str(tickermentions[4]) + """ mentions in """ + str(comments) + """ comments</h5>
      <p>As of 9:15am """ + toptickers[4] + """ had """ + str(tickermentions[4]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[4] + """ was valued at: $""" + str(openprice[4]) + """ and at market close """ + toptickers[4] + """ was valued at: $""" + str(closeprice[4]) + """. The total change in price throughout the day was: $""" + str(round(netchange[4],2)) + """ this is a """ + str(round(percentchange[4],2)) + """% change in price throughout the day.
      </p>
      <img src='ticker5.png'>
      <br><br>
      <hr>
      <h2>Net change of 5 most mentioned stocks today:</h2>
      <img src='tickerpricechanges.png'>
      <h2>Data collected over time:</h2>
      <p>Total number of comments over time:</p>
      <img src='commentsgraph.png'>
      <p>Net change of daily 5 tickers compared to net change of NASDAQ stock exchange over time:</p>
      <img src='netchangegraph.png'>
      <img src='nasdaqchangegraph.png'>
      </div>
      <div class="hidden-sm hidden-xs col-md-3 col-lg-3 col-xl-3">
      </div>
      </div>
      </div>
</body>
</html>"""
f.write(html)
f.close()
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