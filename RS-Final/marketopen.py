from yahoo_fin import stock_info as si
input = open("tickers.txt", "r")
toptickers = []
tickermentions = []
Lines = input.readlines()
for line in Lines:
    data = line.strip().split()
    toptickers.append(data[0])
    tickermentions.append(data[1])
    comments = data[4]
input.close()
output = open("marketopen.txt","w")
for i in range(len(toptickers)):
    if(i == 5):
        break
    else:
        curr_price = round(si.get_live_price(toptickers[i]),2)
        output.write(str(toptickers[i]) + " " + str(tickermentions[i]) + " " + str(comments) + " " + str(curr_price) + "\n")
output.close()
