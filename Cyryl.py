from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import pyperclip
from pynput import keyboard


russian = ''
shift = False
previousContent = ''

class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		
		global russian
		self.keys = []
		self.master.title('Кирил')
		
		self.pack(fill = BOTH, expand = 1)
		
		menu = Menu(self.master)
		self.master.config(menu = menu)
		
		plikMenu = Menu(menu)
		
		plikMenu.add_command(label = 'Koniec', command = self.app_exit)

		menu.add_cascade(label = 'Plik', menu = plikMenu)
		
		self.textBox = Text(self.master, height=8, width = 98)
		self.textBox.place(x = 1, y = 1)		
		
		self.btTilde = Button(self, text = self.getCyryl('`'), command = lambda : self.btAction('`'), height=2, width = 6)
		self.btTilde.place(x = 10, y = 150)
		self.keys.append(self.btTilde)
		
		self.bt1 = Button(self, text = self.getCyryl('1'), command = lambda : self.btAction('1'), height=2, width = 6)
		self.bt1.place(x = 70, y = 150)
		self.keys.append(self.bt1)
		
		self.bt2 = Button(self, text = self.getCyryl('2'), command = lambda : self.btAction('2'), height=2, width = 6)
		self.bt2.place(x = 130, y = 150)
		self.keys.append(self.bt1)
		
		self.bt3 = Button(self, text = self.getCyryl('3'), command = lambda : self.btAction('3'), height=2, width = 6)
		self.bt3.place(x = 190, y = 150)
		self.keys.append(self.bt1)
		
		self.bt4 = Button(self, text = self.getCyryl('4'), command = lambda : self.btAction('4'), height=2, width = 6)
		self.bt4.place(x = 250, y = 150)
		self.keys.append(self.bt1)
		
		self.bt5 = Button(self, text = self.getCyryl('5'), command = lambda : self.btAction('5'), height=2, width = 6)
		self.bt5.place(x = 310, y = 150)
		self.keys.append(self.bt1)
		
		self.bt6 = Button(self, text = self.getCyryl('6'), command = lambda : self.btAction('6'), height=2, width = 6)
		self.bt6.place(x = 370, y = 150)
		self.keys.append(self.bt1)
		
		self.bt7 = Button(self, text = self.getCyryl('7'), command = lambda : self.btAction('7'), height=2, width = 6)
		self.bt7.place(x = 430, y = 150)
		self.keys.append(self.bt1)
		
		self.bt8 = Button(self, text = self.getCyryl('8'), command = lambda : self.btAction('8'), height=2, width = 6)
		self.bt8.place(x = 490, y = 150)
		self.keys.append(self.bt1)
		
		self.bt9 = Button(self, text = self.getCyryl('9'), command = lambda : self.btAction('9'), height=2, width = 6)
		self.bt9.place(x = 550, y = 150)
		self.keys.append(self.bt1)
		
		self.bt0 = Button(self, text = self.getCyryl('0'), command = lambda : self.btAction('0'), height=2, width = 6)
		self.bt0.place(x = 610, y = 150)
		self.keys.append(self.bt1)
		
		self.btEqual = Button(self, text = self.getCyryl('='), command = lambda : self.btAction('='), height=2, width = 6)
		self.btEqual.place(x = 670, y = 150)
		self.keys.append(self.btEqual)
		
		self.btBackspace = Button(self, text = 'Bcksp', command = lambda : self.backSpace(), height=2, width = 7)
		self.btBackspace.place(x = 730, y = 150)
		self.keys.append(self.btBackspace)
		
		# ---------
		
		self.btQ = Button(self, text = self.getCyryl('q'), command = lambda : self.btAction('q'), height=2, width = 6)
		self.btQ.place(x = 20, y = 200)
		self.keys.append(self.btQ)
		
		self.btW = Button(self, text = self.getCyryl('w'), command = lambda : self.btAction('w'), height=2, width = 6)
		self.btW.place(x = 80, y = 200)
		self.keys.append(self.btW)
		
		self.btE = Button(self, text = self.getCyryl('e'), command = lambda : self.btAction('e'), height=2, width = 6)
		self.btE.place(x = 140, y = 200)
		self.keys.append(self.btE)
		
		self.btR = Button(self, text = self.getCyryl('r'), command = lambda : self.btAction('r'), height=2, width = 6)
		self.btR.place(x = 200, y = 200)
		self.keys.append(self.btR)
		
		self.btT = Button(self, text = self.getCyryl('t'), command = lambda : self.btAction('t'), height=2, width = 6)
		self.btT.place(x = 260, y = 200)
		self.keys.append(self.btT)
		
		self.btY = Button(self, text = self.getCyryl('y'), command = lambda : self.btAction('y'), height=2, width = 6)
		self.btY.place(x = 320, y = 200)
		self.keys.append(self.btY)
		
		self.btU = Button(self, text = self.getCyryl('u'), command = lambda : self.btAction('u'), height=2, width = 6)
		self.btU.place(x = 380, y = 200)
		self.keys.append(self.btU)
		
		self.btI = Button(self, text = self.getCyryl('i'), command = lambda : self.btAction('i'), height=2, width = 6)
		self.btI.place(x = 440, y = 200)
		self.keys.append(self.btI)
		
		self.btO = Button(self, text = self.getCyryl('o'), command = lambda : self.btAction('o'), height=2, width = 6)
		self.btO.place(x = 500, y = 200)
		self.keys.append(self.btO)
		
		self.btP = Button(self, text = self.getCyryl('p'), command = lambda : self.btAction('p'), height=2, width = 6)
		self.btP.place(x = 560, y = 200)
		self.keys.append(self.btP)
		
		self.btLeftBracket = Button(self, text = self.getCyryl('['), command = lambda : self.btAction('['), height=2, width = 6)
		self.btLeftBracket.place(x = 620, y = 200)
		self.keys.append(self.btLeftBracket)
		
		self.btRightBracket = Button(self, text = self.getCyryl(']'), command = lambda : self.btAction(']'), height=2, width = 6)
		self.btRightBracket.place(x =680, y = 200)
		self.keys.append(self.btRightBracket)
		
		self.btBackSlash = Button(self, text = self.getCyryl('\\'), command = lambda : self.btAction('\\'), height=2, width = 6)
		self.btBackSlash.place(x =740, y = 200)
		self.keys.append(self.btBackSlash)
		
		# ---------
		
		self.btA = Button(self, text = self.getCyryl('a'), command = lambda : self.btAction('a'), height=2, width = 6)
		self.btA.place(x = 30, y = 250)
		self.keys.append(self.btA)
		
		self.btS = Button(self, text = self.getCyryl('s'), command = lambda : self.btAction('s'), height=2, width = 6)
		self.btS.place(x = 90, y = 250)
		self.keys.append(self.btS)
		
		self.btD = Button(self, text = self.getCyryl('d'), command = lambda : self.btAction('d'), height=2, width = 6)
		self.btD.place(x = 150, y = 250)
		self.keys.append(self.btD)
		
		self.btF = Button(self, text = self.getCyryl('f'), command = lambda : self.btAction('f'), height=2, width = 6)
		self.btF.place(x = 210, y = 250)
		self.keys.append(self.btF)
		
		self.btG = Button(self, text = self.getCyryl('g'), command = lambda : self.btAction('g'), height=2, width = 6)
		self.btG.place(x = 270, y = 250)
		self.keys.append(self.btG)
		
		self.btH = Button(self, text = self.getCyryl('h'), command = lambda : self.btAction('h'), height=2, width = 6)
		self.btH.place(x = 330, y = 250)
		self.keys.append(self.btH)
		
		self.btJ = Button(self, text = self.getCyryl('j'), command = lambda : self.btAction('j'), height=2, width = 6)
		self.btJ.place(x = 390, y = 250)
		self.keys.append(self.btJ)
		
		self.btK = Button(self, text = self.getCyryl('k'), command = lambda : self.btAction('k'), height=2, width = 6)
		self.btK.place(x = 450, y = 250)
		self.keys.append(self.btK)
		
		self.btL = Button(self, text = self.getCyryl('l'), command = lambda : self.btAction('l'), height=2, width = 6)
		self.btL.place(x = 510, y = 250)
		self.keys.append(self.btL)
		
		self.btSemicolon = Button(self, text = self.getCyryl(';'), command = lambda : self.btAction(';'), height=2, width = 6)
		self.btSemicolon.place(x = 570, y = 250)
		self.keys.append(self.btSemicolon)
		
		# ------
		
		self.btCopy = Button(self, text = "Copy", command = lambda : self.copy(), height=5, width = 12)
		self.btCopy.place(x = 660, y = 250)
		self.keys.append(self.btCopy)
		
		# ------
		
		self.btZ = Button(self, text = self.getCyryl('z'), command = lambda : self.btAction('z'), height=2, width = 6)
		self.btZ.place(x = 40, y = 300)
		self.keys.append(self.btZ)
		
		self.btX = Button(self, text = self.getCyryl('x'), command = lambda : self.btAction('x'), height=2, width = 6)
		self.btX.place(x = 100, y = 300)
		self.keys.append(self.btX)
		
		self.btC = Button(self, text = self.getCyryl('c'), command = lambda : self.btAction('c'), height=2, width = 6)
		self.btC.place(x = 160, y = 300)
		self.keys.append(self.btX)
		
		self.btV = Button(self, text = self.getCyryl('v'), command = lambda : self.btAction('v'), height=2, width = 6)
		self.btV.place(x = 220, y = 300)
		self.keys.append(self.btV)
		
		self.btB = Button(self, text = self.getCyryl('b'), command = lambda : self.btAction('b'), height=2, width = 6)
		self.btB.place(x = 280, y = 300)
		self.keys.append(self.btB)
		
		self.btN = Button(self, text = self.getCyryl('n'), command = lambda : self.btAction('n'), height=2, width = 6)
		self.btN.place(x = 340, y = 300)
		self.keys.append(self.btN)
		
		self.btM = Button(self, text = self.getCyryl('m'), command = lambda : self.btAction('m'), height=2, width = 6)
		self.btM.place(x = 400, y = 300)
		self.keys.append(self.btM)
		
		self.btComma = Button(self, text = self.getCyryl(','), command = lambda : self.btAction(','), height=2, width = 6)
		self.btComma.place(x = 460, y = 300)
		self.keys.append(self.btComma)
		
		self.btDot = Button(self, text = self.getCyryl('.'), command = lambda : self.btAction('.'), height=2, width = 6)
		self.btDot.place(x = 520, y = 300)
		self.keys.append(self.btDot)
		
		self.btSlash = Button(self, text = self.getCyryl('/'), command = lambda : self.btAction('/'), height=2, width = 6)
		self.btSlash.place(x = 580, y = 300)
		self.keys.append(self.btSlash)
		
		# ------
		
		self.btShift = Button(self, text = "Shift", command = lambda : self.toggleShift(), height=2, width = 15)
		self.btShift.place(x = 20, y = 350)
		self.keys.append(self.btShift)
		
		self.btSpace = Button(self, text = "", command = lambda : self.addSpace(), height=2, width = 50)
		self.btSpace.place(x = 150, y = 350)
		self.keys.append(self.btSpace)
		
		self.btReset = Button(self, text = "Reset", command = lambda : self.reset(), height=2, width = 12, bg = 'red')
		self.btReset.place(x = 680, y = 350)
		self.keys.append(self.btReset)
		
		self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
		self.listener.start()
	
	def app_exit(self):
		if messagebox.askokcancel("Zakończ program", "Czy naprawdę chcesz wyjść?"):
			exit()

	def getCyryl(self, litera):
		global shift
		retChar = 0
		match litera:
			case 'a':
				retChar = 0x430
			case 'b':
				retChar = 0x431
			case 'v':
				retChar = 0x432
			case 'g':
				retChar = 0x433
			case 'd':
				retChar = 0x434
			case 'e':
				retChar = 0x435
			case ',':
				retChar = 0x436
			case 'z':
				retChar = 0x437
			case 'i':
				retChar = 0x438
			case 'j':
				retChar = 0x439
			case 'k':
				retChar = 0x043A
			case 'l':
				retChar = 0x043b
			case 'm':
				retChar = 0x043c
			case 'n':
				retChar = 0x043d
			case 'o':
				retChar = 0x043e
			case 'p':
				retChar = 0x043f
			case 'r':
				retChar = 0x0440
			case 's':
				retChar = 0x0441
			case 't':
				retChar = 0x0442
			case 'u':
				retChar = 0x0443
			case 'f':
				retChar = 0x0444
			case 'x':
				retChar = 0x0445
			case 'c':
				retChar = 0x0446
			case 'h':
				retChar = 0x0447
			case 'w':
				retChar = 0x0448
			case ']':
				retChar = 0x0449
			case '=':
				retChar = 0x044A
			case 'y':
				retChar = 0x044b

			case ';':
				retChar = 0x044c
			case '\\':
				retChar = 0x044d
			case '[':
				retChar = 0x044e
			case 'q':
				retChar = 0x044f
			case ' ':
				retChar = ' '
			case '`':
				if shift == True:
					retChar = 0x0421
				else:
					retChar = 0x0451
			case _:
				retChar = ord(litera)
		
		if shift == False:
			return chr(retChar)
		
		else :
			return chr(retChar - 0x20)

	def btAction(self, litera):
        
		global russian
		russian += self.getCyryl(litera)
		self.textBox.delete('1.0', END)
		self.textBox.insert('1.0', russian)
	
	def toggleShift(self):
		global shift
		if shift == True:
			shift = False
		else:
			shift = True
		self.literkiNaGuzikach()
	
	def literkiNaGuzikach(self):
		self.btTilde.config(text = self.getCyryl('`'))
		
		
		
		
		
		
		
		
		
		
		self.btEqual.config(text = self.getCyryl('='))
		
		self.btQ.config(text = self.getCyryl('q'))
		self.btW.config(text = self.getCyryl('w'))
		self.btE.config(text = self.getCyryl('e'))
		self.btR.config(text = self.getCyryl('r'))
		self.btT.config(text = self.getCyryl('t'))
		self.btY.config(text = self.getCyryl('y'))
		self.btU.config(text = self.getCyryl('u'))
		self.btI.config(text = self.getCyryl('i'))
		self.btO.config(text = self.getCyryl('o'))
		self.btP.config(text = self.getCyryl('p'))
		self.btLeftBracket.config(text = self.getCyryl('['))
		self.btRightBracket.config(text = self.getCyryl(']'))
		self.btBackSlash.config(text = self.getCyryl('\\'))
		
		self.btA.config(text = self.getCyryl('a'))
		self.btS.config(text = self.getCyryl('s'))
		self.btD.config(text = self.getCyryl('d'))
		self.btF.config(text = self.getCyryl('f'))
		self.btG.config(text = self.getCyryl('g'))
		self.btH.config(text = self.getCyryl('h'))
		self.btJ.config(text = self.getCyryl('j'))
		self.btK.config(text = self.getCyryl('k'))
		self.btL.config(text = self.getCyryl('l'))
		self.btSemicolon.config(text = self.getCyryl(';'))
		
		self.btZ.config(text = self.getCyryl('z'))
		self.btX.config(text = self.getCyryl('x'))
		self.btC.config(text = self.getCyryl('c'))
		self.btV.config(text = self.getCyryl('v'))
		self.btB.config(text = self.getCyryl('b'))
		self.btN.config(text = self.getCyryl('n'))
		self.btM.config(text = self.getCyryl('m'))
		self.btComma.config(text = self.getCyryl(','))
	
	def reset(self):
		global russian
		global previousContent
		pyperclip.copy(previousContent)
		russian = ''
		self.textBox.delete('1.0', END)

	def copy(self):
		global russian
		global previousContent
		previousContent = pyperclip.paste()
		pyperclip.copy(russian)	
	
	def addSpace(self):
		global russian
		russian += ' '
		self.textBox.delete('1.0', END)
		self.textBox.insert('1.0', russian)
		
	def backSpace(self):
		global russian
		if len(russian) > 0:
			russian = russian[:len(russian) - 1]
			self.textBox.delete('1.0', END)
			self.textBox.insert('1.0', russian)
		
	def on_press(self, key):
		global russian
		if self.focus_displayof():
			try:
				if key == keyboard.Key.backspace:
					self.backSpace()
				elif key == keyboard.Key.space:
					self.addSpace()
				elif key == keyboard.Key.caps_lock:
					self.toggleShift()
				elif key == keyboard.Key.shift:
					self.toggleShift()
				else:
					self.btAction(key.char)
			except Exception as ex:
				...
			
	def on_release(self, key):
		global russian
		global shift
		try:
			if key == keyboard.Key.shift:
				shift = False
		except Exception as ex:
			...

		
root = Tk()

root.geometry("795x420")
app = Window(root)
		
root.mainloop()
