#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemy = drawpad.create_rectangle(50,75,125,100, fill="blue")
enemy2 = drawpad.create_rectangle(200,175,300,190, fill="purple")
enemy3 = drawpad.create_rectangle(560,250,600,270, fill="light blue")
enemy4 = drawpad.create_rectangle(320,390,420,405, fill="purple")
direction = 1
direction2 = -1
direction3 = 2
direction4 = -1

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background="green")
       	    self.down.grid(row=0,column=3)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background="green")
       	    self.left.grid(row=0,column=1)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background="green")
       	    self.right.grid(row=0,column=2)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()

	def animate(self):
	    global drawpad
	    global player	    
	    global enemy
	    global enemy2
	    global enemy3
	    global enemy4
	    global direction
	    global direction2
	    global direction3
	    global direction4
	    # Remember to include your "enemies" with "global"
	    x1, y1, x2, y2 = drawpad.coords(enemy)
            if x1 > 800: 
                direction = -840
            elif x1 < 0:
                direction = 1
            drawpad.move(enemy, direction, 0)
            x1, y1, x2, y2 = drawpad.coords(enemy2)
            if x1 < 0: 
                direction2 = 840
            elif x1 > 0:
                direction2 = -1
            drawpad.move(enemy2, direction2, 0)
            x1, y1, x2, y2 = drawpad.coords(enemy3)
            if x1 > 800: 
                direction3 = -840
            elif x1 < 0:
                direction3 = 2
            drawpad.move(enemy3, direction3, 0)
            x1, y1, x2, y2 = drawpad.coords(enemy4)
            if x1 < 0: 
                direction4 = 840
            elif x1 > 0:
                direction4 = -1
            drawpad.move(enemy4, direction4, 0)
            

	    # Uncomment this when you're ready to test out your animation!
	    drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)		

        def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)	
	   	
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)	 
	   
app = MyApp(root)
root.mainloop()