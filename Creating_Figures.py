#importing plotly.express for the hover opportunities
from Cleaning.cluster import creating_clusters
import plotly.express as px

filename = 'Data/2007-2016.xlsx'
Values = creating_clusters(filename)



def creating_figures():
    x = Values['x']
    y = Values['y']
    location = Values['location']
    colors = Values['colors']
    #creating a new plot for each of the 10 years in a for loop 
    for i in range(len(Values['x'])):
        fig = px.scatter(x=x[i],y=y[i],color = colors[i],
                         hover_name=location[i],size_max=60,
                         labels={
                             'x':'Total Population',
                             'y':'Clearance Rates (%)'
                         }
                         ,title='DBSCAN Plot for Year ' + str(2007+i) + ' based on Clearance Rates')

        fig.update_layout(height=800)
        return fig

