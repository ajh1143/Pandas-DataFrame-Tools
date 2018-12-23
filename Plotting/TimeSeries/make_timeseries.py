#Generate a standard timeseries plot from a Pandas DataFrame
#Define the DataFrame to use, x and y columns, labels, and title

#--------------------
#Language: Python
#Function: make_timeseries()
#Purpose: Generates a TimeSeries Line Plot with labels
#Inputs: Pandas DataFrame, Independent Variable, Dependent Variable, X-Label, Y-Label, Graph Title
#Outputs: TimeSeries LinePlot
#--------------------

def make_timeseries(df, x, y, xlab, ylab, gtitle):
    #Generate a line plot
    df.plot(kind='line', x=x, y=y)
    #Add X&Y axis labels
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    #Add graph title
    plt.title(gtitle)
    #Add Legend in position 1
    plt.legend(loc=1)
    #Add gridlines to graph
    plt.grid()
    #Show plot
    plt.show()
