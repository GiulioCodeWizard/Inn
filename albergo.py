'''
Dajani Giulio classe 4^C 30/04/21
Esercizio in preparazione alla verifica
'''
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import locale
locale.setlocale(locale.LC_ALL, '')

class Albergo(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master.title('Esercitazione di informatica')
		self.master.minsize(1060, 650)
		self.master.resizable(True, True)
		self.master.option_add('*Font', 'arial 13')
		self.grid()
		self.lancio_widgets()
	
	def lancio_widgets(self):
		font1 = font.Font(family = 'arial', size = 18, weight = 'bold')
		#titolo
		self.lbl1 = tk.Label(self, text = 'Prenotazione Alberghiera', font = font1)
		self.lbl1.grid(row = 0, column = 0, columnspan = 6)
		#nome
		self.lbl2 = tk.Label(self, text = 'Nome Prenotazione', height = 4)
		self.lbl2.grid(row = 2, column = 0, sticky = tk.W)
		self.nome = tk.StringVar()
		self.txtnome = tk.Entry(self, textvariable = self.nome, bg = '#fff', justify = tk.LEFT, width = 40)
		self.txtnome.grid(row = 2, column = 1)
		#cognome
		self.lbl3 = tk.Label(self, text = 'Cognome Prenotazione')
		self.lbl3.grid(row = 3, column = 0, sticky = tk.W)
		self.cognome = tk.StringVar()
		self.txtcognome = tk.Entry(self, textvariable = self.cognome, bg = '#fff', justify = tk.LEFT, width = 40)
		self.txtcognome.grid(row = 3, column = 1)
		#ntotpers
		self.lbl4 = tk.Label(self, text = 'Numero Totale Persone')
		self.lbl4.grid(row = 4, column = 0, sticky = tk.W)
		self.npers = tk.IntVar()
		self.txtnpers = tk.Entry(self, textvariable = self.npers, bg = '#fff', justify = tk.CENTER, width = 14)
		self.txtnpers.grid(row = 4, column = 1, rowspan = 2, ipady = 50, sticky = tk.W)
		#nadulti
		self.lbl5 = tk.Label(self, text = 'Numero Adulti')
		self.lbl5.grid(row = 4, column = 2, sticky = tk.W)
		self.nadulti = tk.IntVar()
		self.txtadulti = tk.Entry(self, textvariable = self.nadulti, bg = '#fff', justify = tk.LEFT)
		self.txtadulti.grid(row = 4, column = 3)
		#nbambini
		self.lbl6 = tk.Label(self, text = 'Numero Bambini')
		self.lbl6.grid(row = 5, column = 2, sticky = tk.W)
		self.nbambini = tk.IntVar()
		self.txtbambini = tk.Entry(self, textvariable = self.nbambini, bg = '#fff', justify = tk.LEFT)
		self.txtbambini.grid(row = 5, column = 3)
		#nnotti
		self.lbl7 = tk.Label(self, text = 'Numero Notti')
		self.lbl7.grid(row = 7, column = 1, sticky = tk.W)
		self.nnotti = tk.IntVar()
		self.txtnotti = tk.Entry(self, textvariable = self.nnotti, bg = '#fff', justify = tk.LEFT)
		self.txtnotti.grid(row = 7, column = 2, sticky = tk.W)
		#ncameresingole
		self.lbl8 = tk.Label(self, text = 'Numero Camere Singole')
		self.lbl8.grid(row = 8, column = 0, sticky = tk.W)
		self.ncamsing = tk.IntVar()
		self.txtcamsing = tk.Entry(self, textvariable = self.ncamsing, bg = '#fff', justify = tk.LEFT)
		self.txtcamsing.grid(row = 8, column = 1, sticky = tk.W)
		#ncamerematrimoniali
		self.lbl9 = tk.Label(self, text = 'Numero Camere Matrimoniali')
		self.lbl9.grid(row = 8, column = 2, sticky = tk.W)
		self.ncammat = tk.IntVar()
		self.txtcammat = tk.Entry(self, textvariable = self.ncammat, bg = '#fff', justify = tk.LEFT)
		self.txtcammat.grid(row = 8, column = 3, sticky = tk.W)
		#btncalcola
		self.btncalcola = tk.Button(self, text = 'Calcola', width = 18, height = 2, command = self.contr_calcola)
		self.btncalcola.grid(row = 11, column = 1, sticky = tk.W)
		#btnannulla
		self.btnannulla = tk.Button(self, text = 'Annulla', width = 18, height = 2, command = self.svuota_caselle)
		self.btnannulla.grid(row = 11, column = 2, sticky = tk.W)
		#sommadaversare
		self.lbl10 = tk.Label(self, text = 'Somma da Versare', height = 5)
		self.lbl10.grid(row = 12, column = 0, sticky = tk.W)
		self.sommavers = tk.IntVar()
		self.txtsomma = tk.Entry(self, textvariable = self.sommavers, bg = '#fff', justify = tk.LEFT, width = 40)
		self.txtsomma.grid(row = 12, column = 1, ipady = 5)
		#btnesci
		self.btnesci = tk.Button(self, text = 'Esci', width = 18, height = 2, command = self.master.destroy)
		self.btnesci.grid(row = 13, column = 3, columnspan = 2)
		
	
	def contr_calcola(self):
		if (self.nome.get() == ''):
			messagebox.showerror('Import Dati', 'Non è stato inserito nessun dato come nome')
		elif (self.cognome.get() == ''):
			messagebox.showerror('Import Dati', 'Non è stato inserito nessun dato come cognome')
			
		if (self.nome.get() != '' and self.cognome.get() != ''):	
			if (self.npers.get() != (self.nbambini.get() + self.nadulti.get())):
				self.txtnpers['bg'] = 'red'
				messagebox.showwarning('Numero totale persone', 'Il numero totale tra bambini e adulti non è corretto')
			self.txtnpers['bg'] = 'white'
			if (self.nbambini.get() == 0 and self.nadulti.get() == 0):
				messagebox.showwarning('Numero totale persone', 'Il numero di bambini e di adulti è impostato a 0')
		
			if (self.npers.get() == (self.nbambini.get() + self.nadulti.get()) and self.npers.get() != 0):
				if (self.nnotti.get() <= 0):
					self.txtnotti['bg'] = 'red'
					messagebox.showwarning('Numero notti', 'Il numero delle notti deve essere maggiore di 0!')
				self.txtnotti['bg'] = 'white'
				if (self.nnotti.get() > 0):
					if ((self.ncamsing.get() + self.ncammat.get()) > (self.npers.get())):
						messagebox.showwarning('Numero camere', 'Somma numero camere maggiore delle persone!')
					if (self.ncamsing.get() + self.ncammat.get()) <= (self.npers.get()) and (self.ncamsing.get() + self.ncammat.get() != 0):
						n = self.nnotti.get()
						ns = self.ncamsing.get()
						nm = self.ncammat.get()
						s = (n * 80 * ns) + (n * 150 * nm)
						self.sommavers.set(locale.currency(s))
						if (s > 300):
							self.txtsomma['bg'] = 'blue'
							self.txtsomma['fg'] = 'white'
						else:
							self.txtsomma['bg'] = 'green'
							self.txtsomma['fg'] = 'white'
					else:
						messagebox.showwarning('Numero camere', 'Le camere sia matrimoniali che singole non possono essere entrambe 0 o più del numero totale delle persone')
					
	def svuota_caselle(self):				
		self.txtnome.delete(0, tk.END)	
		self.txtcognome.delete(0, tk.END)	
		self.npers.set(0)
		self.nadulti.set(0)
		self.nbambini.set(0)
		self.nnotti.set(0)
		self.ncamsing.set(0)
		self.ncammat.set(0)
		self.sommavers.set(0)			
		self.txtnpers['bg'] = 'white'		
		self.txtnotti['bg'] = 'white'			
		self.txtsomma['bg'] = 'white'			
									
A = Albergo()		
A.mainloop()
