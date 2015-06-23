#MD5sum GUI
import hashlib
import os
from Tkinter import *
from tkFileDialog import askopenfilename

class Application(Frame):
	""" A GUI application for md5sum checker. """
	
	#Initiate GUI
	def __init__(self, master):
		"""Initialize the Frame"""
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
		
	#Design GUI
	def create_widgets(self):
		"""Create button, text, and entry widgets"""
		#Label for file selection
		self.instruction = Label(self, text = "Enter the file:")	
		self.instruction.grid(row = 0, sticky = W)
		
		#Label for MD5 input
		self.instruction = Label(self, text = "Enter the expected md5sum:")	
		self.instruction.grid(row = 1, sticky = W)
		
		#Text box to display selected file
		self.file = Text(self, width=50, height=1)
		self.file.grid(row = 0, column = 1, sticky = W)

		#Button to browse for file to be hashed
		self.open_file = Button(self, text = "Browse", command = self.choosefile)
		self.open_file.grid(row = 0, column = 2)
		
		#Text box to input expected MD5sum
		self.md5sum = Entry(self, width=67)
		self.md5sum.grid(row = 1, column = 1, sticky=W)
		
		#Button to hash and compare
		self.submit_button = Button(self, text = "Submit", command = self.reveal)
		self.submit_button.grid(row = 3, column = 0, sticky = W)
		
		#Textbox for program output
		self.text = Text(self, width=65, height = 5, wrap = WORD)
		self.text.grid(row = 4, column = 0, columnspan = 2, sticky = W)

	#Set file variable after choosing a file to hash
	def choosefile(self):
		global chosen
		chosen = askopenfilename()
		self.file.delete(0.0, END)
		self.file.insert(0.0, chosen)
	
	#Run comparison and output results
	def reveal(self):
		"""Compare MD5sum based on the file and compare it to expected MD5sum"""
		#Set value of expected MD5sum for comparison
		expected = self.md5sum.get()
		
		#Create the file hash
		with open(chosen) as file_to_check:
			contents=file_to_check.read()
			hash = hashlib.md5(contents).hexdigest()
				
		#compare the hashes and determine if hash is as expected	
		if hash == expected:
			message = "The checksum is %s and matches your expectations" % hash
		else:
			message = "The checksum is %s and does not match your expectations" % hash
		
		#Output text in GUI
		self.text.delete(0.0, END)
		self.text.insert(0.0, message)
		
root = Tk()
root.title("MD5sum")
root.geometry("625x200")
app = Application(root)

root.mainloop()
