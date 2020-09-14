'''
Create an application that will prompt for a user to input a string. Using the user’s 
inputted string, find the first letter that is not repeated. 
 
For example: If given the string ‘Bubble’, the letter ‘u’ would be the first character
returned from the program. Once the first character is found and displayed back to the
user, rewrite the string in order of number of occurrences and order from the inputted
string. In the above example ‘Bubble’ would then be rewritten as ‘uleBbb’. Display 
this to the user.

Assumptions in the question: testcase - "Bubble"
1. The unique character should not be repeated in upper or lower case which means 'B'
and 'b' are considered as the same while counting frequency
2. User can enter anything (chars, ints, special char etc)

Submitted by
	Sharath Patlolla 
	sharath.patlolla@utah.edu
	sharathpatlolla@outlook.com
'''

from tkinter import *
from functools import cmp_to_key
import sys

class MyWindow:
	def __init__(self, win = None):
		self.lbl1=Label(win, text='Enter the string')
		self.t1=Entry(bd=3)
		self.lbl1.place(x=50, y=50)
		self.t1.place(x=200, y=50)

		self.lbl3=Label(win, text='First Unique Character')
		self.t3=Entry()
		self.lbl3.place(x=50, y=150)
		self.t3.place(x=200, y=150)

		self.lbl4=Label(win, text='Manipulated String')
		self.t4=Entry()
		self.lbl4.place(x=50, y=200)
		self.t4.place(x=200, y=200)

		self.btn1 = Button(win, text='enter')
		self.b1=Button(win, text='enter', command=self.enter)
		self.b1.place(x=200, y=100)
		
	def enter(self):
		input_string = self.t1.get()
		if ' ' in input_string:
			unique_char = "INVALID INPUT"
			new_string = "Enter input without spaces"
		else:
			[unique_char, new_string] = self.manipulate_string(input_string)
		if unique_char == None:
			unique_char = "NO UNIQUE CHARACTER"
		self.t3.delete(0, 'end')
		self.t3.insert(END, unique_char)
		self.t4.delete(0, 'end')
		self.t4.insert(END, new_string)

	'''
		s : input string
		returns unique_char, new_string

		unique_char :	First character in the string which is not repeated either in upper or
						lower case. Return None if there is no unique character.
		new_string  :  	new string after sorting the input string by frequency and order in 
						ascending order
	'''
	def manipulate_string(self, s):
		freq_dict = {}
		for i in range(len(s)):
			if s[i].upper() not in freq_dict:
				freq_dict[s[i].upper()] = [1, i]
			else:
				freq_dict[s[i].upper()][0] += 1
		
		unique_char = None
		
		for c in s:
			if freq_dict[c.upper()][0] == 1:
				unique_char = c
				break

		def mycmp(ga, gb):
			a, b = ga.upper(), gb.upper()
			if freq_dict[a][0] < freq_dict[b][0]:
				return -1
			elif freq_dict[a][0] == freq_dict[b][0] and (freq_dict[a][1] < freq_dict[b][1]):
				return -1
			return 1
		new_list = sorted(s, key = cmp_to_key(mycmp))
		return [unique_char, str(''.join(new_list))]

# Run this to get the graphical interface version
def with_GUI():
	window=Tk()
	mywin=MyWindow(window)
	window.title('Plena Data Assesment')
	window.geometry("400x400+10+10")
	window.mainloop()

# Run this to get the command line version
def without_GUI():
	input_string = str(input("Enter the string: "))
	if ' ' in input_string:
		print("INVALID INPUT! Enter string without spaces")
	else:
		[unique_char, new_string] = MyWindow.manipulate_string(None, input_string)
		print("First Unique Character: ", unique_char)
		print("Manipulated String: ", new_string)

def main():
	if len(sys.argv) > 1 and sys.argv[1] == '0':
		without_GUI()
	else:
		with_GUI()

if __name__ == "__main__":
	main()