from yahoo_fin import stock_info as si
input = open("tickers.txt", "r")
toptickers = []
Lines = input.readlines()
for line in Lines:
    data = line.strip().split()
    toptickers.append(data[0])
input.close()
output = open("marketclose.txt","w")
for i in range(len(toptickers)):
    if(i == 5):
        break
    else:
        curr_price = round(si.get_live_price(toptickers[i]),2)
        output.write(str(curr_price) + "\n")
output.close()
nasdaqdata = open('nasdaqdata.txt','a+')
nasdaqprice = round(si.get_live_price('^IXIC'),2)
nasdaqdata.write(str(nasdaqprice) + "\n")
nasdaqdata.close()
