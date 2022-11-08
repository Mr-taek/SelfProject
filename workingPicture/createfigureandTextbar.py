import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
def create_by_subplots():
    fig=plt.figure()
    mainaxis=fig.add_axes([0.1,0.3,0.8,0.6])
    baraxis=fig.add_axes([0.1,0.1,0.8,0.15])
    
    return fig,mainaxis,baraxis
