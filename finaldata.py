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
p{
  font-size: 20px;
}
text{
  font-size: 25px
  text-align: center;
}
</style>
<body>
<h1> r/wallstreetbets Top 5 Most Discussed Stocks of the Day:</h1>
<p>This website updates daily at 4:30pm and displays the top 5 most mentioned
stocks from the Daily Discussion thread of the wallstreetbets subreddit.
The goal of this website is to track the overall growth of this subreddit and
visualize the impact the dicussions on this subreddit have on the stock market.
Every day the total number of comments parsed through will be graphed to demonstrate
the growth in popularity of this subreddit as a primary way of communicating about
different stocks. Also, the net change in price of all 5 of the top mentioned
stocks will be recorded and graphed daily.</p>
<div id = "ticker1">
    <h2>""" + toptickers[0] + """</h2>
    <p>As of """ + date[0:10] + """ at 9:15am in the wallstreetbets Discussion Post """ + toptickers[0] + """ had """ + str(tickermentions[0]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[0] + """ was valued at: $""" + str(openprice[0]) + """ at market close """ + toptickers[0] + """ was valued at: $""" + str(closeprice[0]) + """</p>
</div>
<div id = "ticker2">
    <h2>""" + toptickers[1] + """</h2>
    <p>As of """ + date[0:10] + """ at 9:15am in the wallstreetbets Discussion Post """ + toptickers[1] + """ had """ + str(tickermentions[1]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[1] + """ was valued at: $""" + str(openprice[1]) + """ at market close """ + toptickers[1] + """ was valued at: $""" + str(closeprice[1]) + """</p>
</div>
<div id = "ticker3">
    <h2>""" + toptickers[2] + """</h2>
    <p>As of """ + date[0:10] + """ at 9:15am in the wallstreetbets Discussion Post """ + toptickers[2] + """ had """ + str(tickermentions[2]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[2] + """ was valued at: $""" + str(openprice[2]) + """ at market close """ + toptickers[2] + """ was valued at: $""" + str(closeprice[2]) + """</p>
</div>
<div id = "ticker4">
    <h2>""" + toptickers[3] + """</h2>
    <p>As of """ + date[0:10] + """ at 9:15am in the wallstreetbets Discussion Post """ + toptickers[3] + """ had """ + str(tickermentions[3]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[3] + """ was valued at: $""" + str(openprice[3]) + """ at market close """ + toptickers[3] + """ was valued at: $""" + str(closeprice[3]) + """</p>
</div>
<div id = "ticker5">
    <h2>""" + toptickers[4] + """</h2>
    <p>As of """ + date[0:10] + """ at 9:15am in the wallstreetbets Discussion Post """ + toptickers[4] + """ had """ + str(tickermentions[4]) + """ mentions in """ + str(comments) + """ comments. At market open """ + toptickers[4] + """ was valued at: $""" + str(openprice[4]) + """ at market close """ + toptickers[4] + """ was valued at: $""" + str(closeprice[4]) + """</p>
</div>
</body>
</html>"""
f.write(html)
f.close()

#email t&i about davidson domains
#sequel light database
