
# v1.1 add moving average
#cover #6, #7, #8, #9, #10

import time
import datetime
import numpy as np
import matplotlib.pyplot as plt     # to resolve the problem. install Python(x,y) form google. Sometimes need to reboot
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import datetime
# matplotlib.rcParams.update({'font.size':9}) #not sure why doesn't work

eachStock = 'AAPL','GOOG','MSFT','CMG','AMZN','EBAY','TSLA','T','MU','NUGT','WDC'

def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values,weights,'valid')
    return smas

def graphData(stock,MA1,MA2):
    try:
        stockFile = stock+'.txt'
        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',',unpack=True,
                                                              converters={ 0: mdates.strpdate2num('%Y%m%d')})

        x = 0
        y = len(date)
        candleAr = []
        while x < y:
            appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
            candleAr.append(appendLine)
            x+=1

        Av1 = movingaverage(closep,MA1)
        Av2 = movingaverage(closep,MA2)

        SP = len(date[MA2-1:])
       
        fig = plt.figure()
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
        candlestick(ax1,candleAr,width=1, colorup='g',colordown='r')

        ax1.plot(date[-SP:],Av1[-SP:])
        ax1.plot(date[-SP:],Av2[-SP:])
   

        plt.ylabel('Stock Price')
        ax1.grid(True)

        ax2 = plt.subplot2grid((5,4),(4,0),sharex=ax1, rowspan=1, colspan=4)
        ax2.bar(date,volume)
        ax2.axes.yaxis.set_ticklabels([])
        ax2.grid(True)
        plt.ylabel('Volume')
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(90)

        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.subplots_adjust(left=.10,bottom=.19,right=.93,top=.95)
       
        plt.suptitle(stock+'Stock Price') # ' and " are the same
        plt.setp(ax1.get_xticklabels(), visible=False)

        plt.subplots_adjust(hspace=0)

        print datetime.datetime.now()
       
        #plt.show()
       
        fig.savefig(stock+'.png')
       
    except Exception, e:
        print 'failed main loop', str(e)

for stock in eachStock:
    graphData(stock,12,26)
    print stock
    time.sleep(5)

