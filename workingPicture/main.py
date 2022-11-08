import createfigureandTextbar as create
import matplotlib.pyplot as plt

from matplotlib.widgets import TextBox
import textbox as tb

class main:
    def __init__(self):
        self.fig,self.mainaxis,self.baraxis=create.create_by_subplots()
        # for i in ["bottom","left","right","top"]:
        #     self.mainaxis.tick_params(i=False)
    def update(self,text):
        print(text)
        if "delete" not in text:
            self.text.make(self.mainaxis,text)
        else:
            splottext=text.split(" ")[1]
            self.text.delete(splottext)
        self.fig.canvas.draw()
    def excute(self):
        tbt=TextBox(self.baraxis,"")
        tbt.on_submit(self.update)
        self.text=tb.textbox(self.fig)
        self.fig.show()
        input()

main().excute()