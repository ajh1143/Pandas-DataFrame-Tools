#Generate a standard scatter plot from Pandas DataFrame
#Define x and y columns and associated labels, a graph title

#--------------------
#Language: Python
#Function: make_scatter()
#Purpose: Generate a scatter plot from given datasets 
#Inputs: X-axis data, Y-axis data, X-Axis Label, Y-Axis Label, Graph Title
#Outputs: Populated Scatter Plot with Labels/Title and Legend
#--------------------

def make_scatter(x, y, xlab, ylab, gtitle):
    plt.scatter(x = x, y = y)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(gtitle)
    plt.legend(loc=1)
    plt.grid()
    plt.show()
