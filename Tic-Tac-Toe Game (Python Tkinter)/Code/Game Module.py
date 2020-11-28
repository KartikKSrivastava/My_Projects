from tkinter import *
import tkinter.messagebox


class Create:
	z , dic , count , score_1 , score_2= '' , {1:'B' , 2:'C' , 3:'D' , 4:'E' , 5:'F' , 6:'G' , 7:'H' , 8:'I' , 9:'J'},0,0,0
	def __init__(self , root ,row , col , num):
		self.num = num
		self.root , self.row , self.col = root , row , col
		self.button = Button(root , text = '' , bg = 'White' , fg = 'black' ,  height = 4 , width = 8 , font = ('Courier' ,15,'bold'),command = self.sign)
		self.button.grid(row= row ,  column = col)	
		self.line = self.button['text']

	def mark_x(self):
		self.button['text']='X'

	def mark_y(self):
		self.button['text']='O'

	def check_num(self , x):
		if x%2!=0:
			return True
		else:
			return False		
	def increment(var):
		if Create.dic[var].lower()=='x':
			Create.score_1+=1
			score_1_lab['text'] = 'Player 1 Score : '+str(Create.score_1)
		if Create.dic[var].lower()=='o':
			Create.score_2+=1
			score_2_lab['text'] = 'Player 2 Score : '+str(Create.score_2)
				
	def sign(self):
		if self.check_num(Create.count)==True:
			if self.button['text']=='':
				Create.count+=1
				self.mark_x()
				Create.dic[self.num] = self.button['text']
		if self.check_num(Create.count)==False:
			if self.button['text']=='':
				Create.count+=1
				self.mark_y()
				Create.dic[self.num] = self.button['text']
               
		k , j = 1 ,1
		for i in range(1 , 4): ############ Checks Rows ##################
			if Create.dic[j]==Create.dic[j+1]==Create.dic[j+2]:
				Create.increment(var = j)
				Create.z = tkinter.messagebox.showinfo('Window title' , 'Congratulations !!'+'\n'+'\"'+str(Create.dic[j])+'\"'+' WINS by Symmetry in ROW')
				new(x = lis , root = self.root)
			j+=3
	      
		for i in range(1 , 4): ############### Check columns ##############
			if Create.dic[k]==Create.dic[k+3]==Create.dic[k+6]:
				Create.increment(var = k)
				Create.z=tkinter.messagebox.showinfo('Window title' ,'Congratulations !!'+'\n'+'\"'+str(Create.dic[k])+'\"'+' WINS by Symetry in Columns')
				new(x = lis , root = self.root)
			k+=1

		if Create.dic[1]==Create.dic[5]==Create.dic[9]: ######### Check first diaognal ############
			Create.increment(5)
			Create.z=tkinter.messagebox.showinfo('Window title' ,'Congratulations !!'+'\n'+'\"'+str(Create.dic[5])+'\"' +' WINS by Symmetry in Principal diagonal')
			new(x = lis , root = self.root)

		if Create.dic[3]==Create.dic[5]==Create.dic[7]: ######### Check Second diaognal ############
			Create.increment(5)
			Create.z=tkinter.messagebox.showinfo('Window title' ,'Congratulations !!'+'\n'+'\"'+str(Create.dic[5])+'\"'+' WINS by Symmetry in Secondary diagonal')
			new(x = lis , root = self.root)

       

def create_bt(root):
	global lis 
	lis  , c = [] , 0
	for i in range(3):
		row , col = i ,  0
		for i in range(3):
			c+=1
			lis.append(Create(wind , row , col , c))
			col+=1		
	return lis

def new(x , root):
	del x 	
	Create.dic = {1:'B' , 2:'C' , 3:'D' , 4:'E' , 5:'F' , 6:'G' , 7:'H' , 8:'I' , 9:'J'}
	create_bt(root)

def reset(x , root):
	score_1_lab['text'] , score_2_lab['text'] ,Create.score_2 , Create.score_1 = 'Player 1 Score : 0' , 'Player 2 Score : 0',0,0	



wind = Tk()

wind.geometry('500x500')
wind.configure(background = 'light blue')
create_bt(root = wind)

score_1_lab = Label(wind , text= 'Player 1 Score : 0',  height = 2 , bg = 'Black' , fg = 'Cyan' , font = ('Courier' , 10))
score_1_lab.place(x = 350 , y = 0)
score_2_lab = Label(wind , text= 'Player 2 Score : 0' ,  height = 2 , bg = 'Black' , fg = 'Cyan' ,font = ('Courier' , 10))
score_2_lab.place(x = 350 , y = 40)

new_game = Button(wind , text = 'New Game' , bg = 'White'  ,fg=  'Dark olive green' , height = 3, width = 15 , font = ('Courier' , 11, 'bold'),command = lambda : new(lis , root = wind))
new_game.place(x = 350 , y = 100)

reset_game = Button(wind , text = 'Reset Game' , bg = 'White' , fg=  'Dark slate gray' , height = 3 , width = 15 ,font = ('Courier' , 11,'bold') ,command = lambda : reset(lis , root = wind))
reset_game.place(x = 350 , y = 170)

wind.mainloop()
