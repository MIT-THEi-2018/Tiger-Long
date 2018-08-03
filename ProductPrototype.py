import tkinter as tk # imports
from tkinter import ttk
import webbrowser

win = tk.Tk()
win.title("Python guide book")
win.geometry('850x870')
tabControl = ttk.Notebook(win)
#---------------------------------------------------------------------
#style = ttk.Style()
#style.configure("BW.TLabel", foreground="black", background="black")
#tab1 = ttk.Frame(tabControl,style="BW.TLabel")
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Home')
Tab1Label01 = ttk.Label(tab1, text="Python guide book",font='Helvetica -50 bold').place(x=400, y=25, anchor="center")
Tab1Label02 = ttk.Label(tab1, text="V0.0.1",font='Helvetica -20 bold').place(x=400, y=70, anchor="center")
img_png = tk.PhotoImage(file = 'Logo.png')
Tab1Label03 = ttk.Label(tab1, image = img_png).place(x=400, y=225, anchor="center")
Tab1Label04 = ttk.Label(tab1, text="The First Step to Begin~",font='Helvetica -30 italic').place(x=250, y=400, anchor="center")
Tab1Label05 = ttk.Label(tab1, text="HLche",font='Helvetica -20').place(x=800, y=800, anchor="center")
tabControl.pack(expand=1, fill="both")
TabNameList = ["Print","Variables","Casting","String 0","String 1","List","Tuples","Set","Dictionary", "condition","Looping","Functions","Array","+"]
ExplainationList = [	"Displaying contents in the concole or command prompt ",
					 	"Basic operating variables, data attribute is NOT required to declare",
					 	"Manually declare the data attribute, will be used when handling user inputs",
					 	"Basic operating variables, data attribute is NOT required to declare",
					 	"Additional function of string",
					 	"Storing data with a LIST, able to access it with index, content COULD be changed",
					 	"Storing data with a TUPLE, able to access it with index, content COULD NOT be changed",
					 	"A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.",
					 	"A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.",
					 	"Python supports the usual logical conditions from mathematics:\nEquals: a == b\nNot Equals: a != b\nLess than: a < b\nLess than or equal to: a <= b\nGreater than: a > b\nGreater than or equal to: a >= b",
					 	"While Loops:\nWith the while loop we can execute a set of statements as long as a condition is true.\n\tThe break Statement:\n\t\tWith the break statement we can stop the loop even if the while condition is true\n\tThe continue Statement:\n\t\tWith the continue statement we can stop the current iteration, and continue with the next\n-------------------------------------------------------------------------------------------------------------------------------\nFor Loops\nA for loop is used for iterating over a sequence (that is either a list, a tuple or a string).\n\tThe break Statement:\n\t    With the break statement we can stop the loop before it has looped through all the items\n\tThe continue Statement\n\t    With the continue statement we can stop the current iteration of the loop, and continue with the next:",
					 	"In Python a function is defined using the def keyword",
					 	"Arrays are used to store multiple values in one single variable",
					 	""
					 	]
UrlList = [				"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp",
						"https://www.w3schools.com/python/default.asp"
					 	]
ExampleList = [			'print("Hello, World!")',
					 	'x = 5 # integer\ny = "John" # String\nz = " Esca" # String\nprint(x)\nprint(y)\nprint(y+z)',
					 	'z1 = int("3") # become integer\nz2 = float("3") # become float\nz3 = str(2) # become string',
					 	'TestText = "Hello, World!"\n\nprint(TestText[1])\nprint(TestText[2:5])',
					 	'TestText = "Hello, World!"\n\nprint(len(TestText)) # return the length of string\nprint(TestText.lower()) # eturn lower case\nprint(TestText.upper())# return upper case\nprint(TestText.replace("o", "J")) # replace o with J\nprint(TestText.split(",")) # split text be a specific character',
					 	'thislist = ["apple", "banana", "cherry"] # create new list\nprint(thislist)\nthislist[1] = "blackcurrant" # Set value in 1 index\nprint(thislist)\nthislist.append("damson") # Add value in List\nprint(thislist)\nthislist.remove("cherry") # Remove value from list\nprint(thislist)\nprint(len(thislist)) # return length of list',
					 	'thistuple = ("apple", "banana", "cherry")\nprint(thistuple)\nprint(thistuple[1]) #get 1st index value(i.e. second value)\nprint(len(thistuple)) # return length of tuples',
					 	'thisset = {"apple", "banana", "cherry"} # create new set\nprint(thisset)\nthisset.add("damson") # Add value in set\nprint(thisset)\nthisset.remove("banana") # Remove value in set\nprint(thisset)\nprint(len(thisset)) #return length of set',
					 	'thisdict =	{\n"apple": "green",\n"banana": "yellow",\n"cherry": "red"\n} #create a new Dictionary\nprint(thisdict)\n\nthisdict["apple"] = "red" # set value in apple key\nprint(thisdict)\n\nthisdict["damson"] = "purple"#add value in dictionary\ndel(thisdict["banana"])#remove in dictionary\nprint(thisdict)\n\nprint(len(thisdict)) # return length of Dictionary',
					 	'a = 200\nb = 33\nif b > a:\n    print("b is greater than a")\nelif a == b:\n    print("a and b are equal")\nelse:\n    print("a is greater than b")',
					 	'i = 0\nwhile i < 6:\n    i += 1\n    if i == 3:\n        continue\n    elif i == 5:\n        break\n    else:\n        print(i)\n-------------------------------------------------------------------------------------------------------------------------------\nfruits = ["apple", "banana", "cherry"]\nfor x in fruits:\n    print(x)\nfor x in range(6):\n    print(x)\n',
					 	'def my_function(fname):\n    print(fname + " Refsnes")\n\nmy_function("Emil")\nmy_function("Tobias")\nmy_function("Linus")\n\ndef my_function1(x):\n    return 5 * x\n\nprint(my_function1(3))\nprint(my_function1(5))\nprint(my_function1(9))',
					 	'cars = ["Ford", "Volvo", "BMW"] # create a array\nprint(cars)\n\ncars[0] = "Toyota" # Update the value in 0 index in the array\nprint(cars)\n\ncars.append("Honda")#add in arrayprint(cars)\nprint(cars)\n\ncars.pop(1)#remove in array\nprint(cars)\n\nprint(len(cars)) # return length of array',
					 	""
					 	]
OutcomeList = [			"Hello, World!",
					 	"5\nJohn\nJohn Esca",
					 	"",
					 	"e\nllo",
					 	"18\nhello, world!\nHELLO, WORLD!\nHellJ, WJrld!\n['Hello', ' World!']",
					 	"['apple', 'banana', 'cherry']\n['apple', 'blackcurrant', 'cherry']\n['apple', 'blackcurrant', 'cherry', 'damson']\n['apple', 'blackcurrant', 'damson']\n3",
					 	"('apple', 'banana', 'cherry')\nbanana\n3",
					 	"{'cherry', 'apple', 'banana'}\n{'cherry', 'damson', 'apple', 'banana'}\n{'cherry', 'damson', 'apple'}\n3",
					 	"{'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}\n{'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}\n{'apple': 'red', 'cherry': 'red', 'damson': 'purple'}\n3",
					 	"a is greater than b",
					 	"1\n2\n4\n-------------------------------------------------------------------------------------------------------------------------------\napple\nbanana\ncherry\n0\n1\n2\n3\n4\n5",
					 	"Emil Refsnes\nTobias Refsnes\nLinus Refsnes\n15\n25\n45",
					 	"['Ford', 'Volvo', 'BMW']\n['Toyota', 'Volvo', 'BMW']\n['Toyota', 'Volvo', 'BMW', 'Honda']\n['Toyota', 'BMW', 'Honda']\n3",
					 	""
					 	]
for x in range(len(TabNameList)):
	#---------------------------------------------------------------------
	globals()['tab%s' % x] = ttk.Frame(tabControl)
	if TabNameList[x] != "+":
		tabControl.add(globals()['tab%s' % x], text=TabNameList[x])
		ttk.Label(globals()['tab%s' % x], text="Explaination",font='Helvetica -20 bold').grid(column=0, row=0,sticky='W')
		ttk.Label(globals()['tab%s' % x], text=ExplainationList[x], wraplength=820, justify=tk.LEFT,font='Helvetica -16 bold').grid(column=0, row=1,sticky='W')
		new = 1
		url = UrlList[x]
		def openweb():
			webbrowser.open(url,new=new)

		ttk.Button(globals()['tab%s' % x], text = "Details",command=openweb).grid(column=0, row=2,sticky='W')
		ttk.Label(globals()['tab%s' % x], text="Example",font='Helvetica -20 bold').grid(column=0, row=3,sticky='W')
		ttk.Label(globals()['tab%s' % x], text=ExampleList[x], wraplength=820, justify=tk.LEFT,font='Helvetica -14').grid(column=0, row=4,sticky='W')
		ttk.Label(globals()['tab%s' % x], text="output",font='Helvetica -16 bold').grid(column=0, row=5,sticky='W')
		ttk.Label(globals()['tab%s' % x], text=OutcomeList[x], wraplength=820, justify=tk.LEFT,font='Helvetica -14').grid(column=0, row=6,sticky='W')
		tabControl.pack(expand=1, fill="both")
	else:
		tabControl.add(globals()['tab%s' % x], text=TabNameList[x])
		tk.Text(globals()['tab%s' % x],height=1).grid(column=0, row=0,sticky='W')
		ttk.Label(globals()['tab%s' % x], text="Explaination",font='Helvetica -20 bold').grid(column=0, row=1,sticky='W')
		tk.Text(globals()['tab%s' % x],height=5).grid(column=0, row=2,sticky='W')
		ttk.Label(globals()['tab%s' % x], text="Example",font='Helvetica -20 bold').grid(column=0, row=3,sticky='W')
		tk.Text(globals()['tab%s' % x],height=5).grid(column=0, row=4,sticky='W')
		ttk.Label(globals()['tab%s' % x], text="output",font='Helvetica -16 bold').grid(column=0, row=5,sticky='W')
		tk.Text(globals()['tab%s' % x],height=5).grid(column=0, row=6,sticky='W')
		tk.Button(globals()['tab%s' % x],text='Don\'t press me yet!!', width=15, height=2,foreground="black", background="white").grid(column=0, row=7,sticky='W')
		tabControl.pack(expand=1, fill="both")
	#---------------------------------------------------------------------

win.mainloop()