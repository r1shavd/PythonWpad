"""
W-Pad (Python3)

This is a notepad type text editor application created using Python3 programming language using the tkinter library. The features of this application are listed below :
1. Made using pure python3 and with the help of the tkinter library.
2. Serves the feature to save a new file and also open an already existing file (with loading its data).

Author : Rishav Das (Github : https://github.com/rdofficial/)
"""

# Importing the required functions and modules
try:
	from tkinter import *
	from tkinter import messagebox as mb
except Exception as e:
	# If there are any errors encountered during the process, then we print the error on the console screen and exit the script

	print('[ Error : {} ]'.format(e))

# The main script starts here

__about__ = """
W-Pad is a text editor application written for notes writting and other such writting stuff.
The application is in development stage and currently there are just basic features available
like opening and saving a file, in future more updates will be coming. Just stay connected. The
application is written using python3 programming language and requires tkinter graphical library
for creating the GUI objects.

The application is written by Rishav Das. If there are any errors or makfunctionining in the working
of the application, then kindly report at rdofficial192@gmail.com, or just create an issue on the
Github repository (https://github.com/rdofficial/PythonWpad). If you want to do any updates and modi
-fication to the source code and structure of this project, then can create your pull request at the
above mentioned GIT repository. 
"""

__help__ = """
"""

def openNotepad():
	""" The function which launches a tkinter window for asking the user to enter a file location to open in a new notepad window """

	try:
		# Creating a small tkinter window

		global openWin
		openWin = Tk()
		openWin.title('Open - W-Pad')
		frame = Frame(openWin)
		frame.pack(padx = 5, pady = 5)
		filelocation = StringVar(openWin)
		Label(frame, text = 'Enter the file location to open', font = ('', 11)).pack(side = LEFT, padx = 5, pady = 5)
		Entry(frame, textvariable = filelocation, font = ('', 11)).pack(side = RIGHT, padx = 5, pady = 5)
		Button(openWin, text = 'Open', font = ('', 11), foreground = 'white', background = 'black', activeforeground = 'black', activebackground = 'white', relief = GROOVE, padx = 5, pady = 5, command = lambda : main(filelocation.get())).pack(padx = 5, pady = 5)
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error via messagebox

		mb.showerror('Error occured', e)

def about(mode = 'about'):
	""" The function to display the tkinter window with wheter the about or help text (as per the function argument). """

	aboutWin = Tk()

	if mode == 'about':
		# For the about version of the tkinter window

		aboutWin.title('About - W-Pad')
		Label(aboutWin, text = 'About', font = ('', 11, 'bold', 'italic'), foreground = 'black').pack(padx = 5, pady = 2.5)
		Label(aboutWin, text = __about__, font = ('', 11), foreground = 'black', justify = 'left').pack(padx = 5, pady = 2.5)
	elif mode == 'help':
		# For the help version of the tkinter window

		aboutWin.title('Help - W-Pad')
		Label(aboutWin, text = 'Help', font = ('', 11, 'bold', 'italic'), foreground = 'black').pack(padx = 5, pady = 2.5)
		Label(aboutWin, text = __help__, font = ('', 11), foreground = 'black', justify = 'left').pack(padx = 5, pady = 2.5)
	else:
		# If the mode is not mentioned while calling the function, then we raise a fucking error

		mb.showerror('Error', 'No mode mentioned while calling the function "about()", check the source code for debugging the errors.')

def save(data, mode = 'gui', filename = None):
	""" The function to save the requested written text on the notepad to a file on the local desktop machine """

	if mode == 'ask':
		# If the function is being called for creating the window to ask the filename to save the data

		try:
			# Creating a small tkinter window to ask the user to enter the filename for the requested

			global saveWin
			saveWin = Tk()
			saveWin.title('Save as - W-Pad')
			frame = Frame(saveWin)
			frame.pack(padx = 5, pady = 5)
			filelocation = StringVar(saveWin)
			Label(frame, text = 'Enter the file location to save', font = ('', 11)).pack(side = LEFT, padx = 5, pady = 5)
			Entry(frame, textvariable = filelocation, font = ('', 11,)).pack(side = RIGHT, padx = 5, pady = 5)
			Button(saveWin, text = 'Save', font = ('', 11,), foreground = 'white', background = 'black', activeforeground = 'black', activebackground = 'white', relief = GROOVE, padx = 5, pady = 5, command = lambda : save(data, mode = 'save', filename = filelocation.get())).pack(padx = 5, pady = 5)
		except Exception as e:
			# If there are any errors encountered during the process, then we display the error back to the user using the messagebox

			mb.showerror('Error occured', e)
	elif mode.lower() == 'save':
		# If the function is called for just saving the textarea content to a requested file, then we continue the process

		try:
			# Saving the notepad written text to the user specified file location

			open(filename, 'w+').write(str(data))
			win.title('{} - W-Pad'.format(filename))
		except Exception as e:
			# If there are any errors encountered during the process, then we display the error back to the user using the messagebox

			mb.showerror('Error occured', e)
		else:
			# If there are no errors encountered during the process, then we display the success message using the messagebox

			mb.showinfo('Saved', 'The file has been saved as {}'.format(filename))
		finally:
			# Destroying the save tkinter window after all the process has been completed

			saveWin.destroy()
	else:
		# If the function is called for no specified mode, then we display an error message

		mb.showerror('Error', 'The save function is called without mentioning a proper mode')

def main(filelocation = None):
	""" The main function of the script (DRIVER CODE) """

	# Creating the tkinter window
	global win
	win = Tk()
	win.geometry('500x500')

	# Destroying the save and open tkinter windows only if they exists
	try:
		openWin.destroy()
		saveWin.destroy()
	except:
		pass

	# Creating the menubar for the notepad window
	menubar = Menu(win)

	# Creating the Filemenu
	filemenu = Menu(menubar, tearoff = 0, font = ('', 10))
	# Adding items to the filemenu
	filemenu.add_command(label = 'Save', command = lambda : save(textarea.get('1.0', END), mode = 'ask'))
	filemenu.add_command(label = 'Open', command = openNotepad)

	# Creating the Aboutmenu
	aboutmenu = Menu(menubar, tearoff = 0, font = ('', 10))
	# Adding items to the aboutmenu
	aboutmenu.add_command(label = 'About', command = lambda : about(mode = 'about'))
	aboutmenu.add_command(label = 'Help', command = lambda : about(mode = 'help'))
	aboutmenu.add_separator()
	aboutmenu.add_command(label = 'Exit', command = exit)

	# Adding the created sub menus to the menubar
	menubar.add_cascade(label = 'File', menu = filemenu)
	menubar.add_cascade(label = 'About', menu = aboutmenu)
	win.config(menu = menubar)

	# Creating the textarea object on the main window
	textarea = Text(win, foreground = 'white', insertbackground = 'white', background = 'black', font = ('monospace', 10,))
	textarea.pack(expand = True, fill = BOTH)

	# Checking if the filelocation argument value is set or not
	if filelocation == None:
		win.title('Untitled - W-Pad')
	else:
		# If the filelocation argument value is not none and some argument is given then we open the file here. First setting the window title, then the text area name

		try:
			win.title('{} - W-Pad'.format(filelocation))
			textarea.insert('1.0', open(filelocation, 'r').read())
		except Exception as e:
			# If there are any errors encountered during the process, then we display them using the messagebox

			mb.showerror('Failed to open the file', e)
		else:
			# If there are no errors encountered during the process, then we display the info message to the user

			mb.showinfo('File opened', 'The file has been opened,. When saving the file, use the same name for the saving to avoid creation of new files.');

	mainloop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combination, then the script quits immediately

		quit()
	except Exception as e:
		# If there are any errors encountered during the execution of the main() code, then we display the error to the user using messagebox

		mb.showerror('Error occured', e)