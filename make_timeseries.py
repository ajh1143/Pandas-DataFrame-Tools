#Generate a standard timeseries plot from a Pandas DataFrame
#Define the DataFrame to use, x and y columns, labels, and title

def make_timeseries(df, x, y, xlab, ylab, gtitle):
    df.plot(kind='line', x=x, y=y)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(gtitle)
    plt.legend(loc=1)
    plt.grid()
    plt.show()
