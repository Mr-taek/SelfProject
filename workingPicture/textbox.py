import matplotlib.pyplot as plt
class textbox:
    def __init__(self,fig) -> None:
        self.fig=fig
        self.fig.canvas.mpl_connect("pick_event",self.hist_text_click)
        self.fig.canvas.mpl_connect("button_release_event",self.hist_text_release)
        self.artist=None
        self.initial_pos=(None,None)
        self.axisdict={

        }
    def hist_text_click(self,event):
        self.artist=event.artist
        self.initial_pos=(event.mouseevent.xdata,event.mouseevent.ydata)
    def hist_text_release(self,event):
        if self.artist!=None:
            old_pos=self.artist.get_position()
            new_pos=(old_pos[0]+event.xdata-self.initial_pos[0],old_pos[1]+event.ydata-self.initial_pos[1])
            self.artist.set_position(new_pos)
            self.artist=None
            plt.gcf().canvas.draw()
    def make(self,axis,text):
            box={
                'boxstyle':"square",
                "ec":"yellow",
                "fc":"white",
                "linestyle":"-."
            }
            add=axis.text(0.5,0.5,text,bbox=box,picker=True)
            self.axisdict.update({text:add})
    def delete(self,text):
        self.axisdict[text].remove()
        self.fig.canvas.draw()