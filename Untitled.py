#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import tkinter as tk

# from tkinter import simpledialog

buttonwidth = 20
name1 = ""
name2 = ""
name3 = ""

loser1 = 99
loser0 = 99


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 

backgroundcolor = _from_rgb((169,169,169))
playercolor = _from_rgb((128,0,0))
fontplayercolor = _from_rgb((255,255,255))

fontplayersize = 60
fontquestionsize = 40
entrywidth = 12


# In[3]:


class Player:
    def __init__(self, name):
        """Parameters of the player"""
        self.timeleft = 60
        self.name = name
        
        
    def addtime(self,timetoadd):
        """Add time to timeleft"""
        self.timeleft += timetoadd
        
        
    def __str__(self):
        """string version of player"""
        return self.name + ": " + str(self.timeleft)
    
    def removetime(self,timetoremove):
        """Remove time from timeleft"""
        self.timeleft -= timetoremove


# In[4]:


class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.remaining = 0
        self.counter = 0
        self.gamemode = 0
        self.playerselection = 0
        self.newgameflag = False
        self.newplayerflag = False
        self.finalflag = False
        
        
        self.players = []
        self.players.append(Player(name1))
        self.players.append(Player(name2))
        self.players.append(Player(name3))
        
        self.label = tk.Label(self, text="", font=("Courier", fontplayersize), bg = playercolor, fg = fontplayercolor)
        self.label.grid(row = 0 , column = 0 )
        
        self.label1 = tk.Label(self, text="", font=("Courier", fontplayersize), bg = playercolor, fg = fontplayercolor)
        self.label1.grid(row = 0 , column = 1)
        
        self.label2 = tk.Label(self, text="", font=("Courier", fontplayersize), bg = playercolor, fg = fontplayercolor)
        self.label2.grid(row = 0 , column = 2)
        self.label.configure(text=str(self.players[0]))
        self.label1.configure(text=str(self.players[1]))
        self.label2.configure(text=str(self.players[2]))
        
        
        self.blank_space = tk.Label(self, text = '', bg = backgroundcolor)
        self.blank_space.grid(row = 1, columnspan = 2)
        
        self.spel_label = tk.Label(self, text = 'Spelkeuze', font=("helvetica", fontquestionsize), bg = backgroundcolor)
        self.spel_label.grid(row = 2, column = 0)
        
        self.speler_label = tk.Label(self, text = 'Spelerkeuze', font=("helvetica", fontquestionsize), bg = backgroundcolor)
        self.speler_label.grid(row = 2, column = 1)
        
        self.functie_label = tk.Label(self, text = 'Functie', font=("helvetica", fontquestionsize), bg = backgroundcolor)
        self.functie_label.grid(row = 2, column = 2)
        
        self.finale_label = tk.Label(self, text = 'Finale Type', font=("helvetica", fontquestionsize), bg = backgroundcolor)
        self.finale_label.grid(row = 7, column = 2)
        
        #buttons
        self.add_button = tk.Button(self, text="Antwoord Correct", command= self.addtotime, width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.add_button.grid(row=3, column = 2)
        
        self.game_button_1 = tk.Button(self, text="3-6-9", command= lambda: self.setgamemode(1), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.game_button_1.grid(row=3, column = 0)
        
        self.game_button_2 = tk.Button(self, text="Open Deur", command= lambda: self.setgamemode(2), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.game_button_2.grid(row=4, column = 0)
        
        self.game_button_3 = tk.Button(self, text="Puzzel", command= lambda: self.setgamemode(3), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.game_button_3.grid(row=5, column = 0)
        
        self.game_button_4 = tk .Button(self, text="De Galerij", command= lambda: self.setgamemode(4), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.game_button_4.grid(row=6, column = 0)
        
        self.game_button_5 = tk.Button(self, text="Collectief Geheugen", command= lambda: self.setgamemode(5), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.game_button_5.grid(row=7, column = 0)
        
        self.game_button_6 = tk.Button(self, text="Finale", command= lambda: self.setgamemode(6), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.game_button_6.grid(row=8, column = 0)
        
        self.player_0_button = tk.Button(self, text=self.players[0].name, command = lambda:  self.setplayerselection(0), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.player_0_button.grid(row=3, column = 1)
        
        self.player_1_button = tk.Button(self, text=self.players[1].name, command = lambda:  self.setplayerselection(1), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.player_1_button.grid(row=4, column = 1)
        
        self.player_2_button = tk.Button(self, text=self.players[2].name, command = lambda:  self.setplayerselection(2), width = buttonwidth, bg='brown', fg='white', font=('helvetica',fontquestionsize, 'bold'))
        self.player_2_button.grid(row=5, column = 1)
        
        self.pause_button = tk.Button(self, text = "Pas", command = lambda: self.setgamemode(0), width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.pause_button.grid(row=4, column = 2)
        
        self.finale_button = tk.Button(self, text = "Normaal", command = self.setfinalflag, width = buttonwidth, bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.finale_button.grid(row=8, column = 2)
        
        self.countdown()
        
    def setfinalflag(self):
        if self.finalflag == False:
            self.finalflag = True
            self.finale_button.configure(text="Aangepast")
        else:
            self.finalflag = False
            self.finale_button.configure(text="Normaal")

        
        
    def addtotime(self):
        if self.gamemode == 1:
            self.players[self.playerselection].addtime(10)
            self.label.configure(text=str(self.players[0]))
            self.label1.configure(text=str(self.players[1]))
            self.label2.configure(text=str(self.players[2]))
                    
        elif self.gamemode == 2:
            self.players[self.playerselection].addtime(20)
            self.label.configure(text=str(self.players[0]))
            self.label1.configure(text=str(self.players[1]))
            self.label2.configure(text=str(self.players[2]))
        elif self.gamemode == 3:
            self.players[self.playerselection].addtime(30)
            self.label.configure(text=str(self.players[0]))
            self.label1.configure(text=str(self.players[1]))
            self.label2.configure(text=str(self.players[2]))
        elif self.gamemode == 4:
            self.players[self.playerselection].addtime(15)
            self.label.configure(text=str(self.players[0]))
            self.label1.configure(text=str(self.players[1]))
            self.label2.configure(text=str(self.players[2]))
        elif self.gamemode == 5:
            self.players[self.playerselection].addtime(10 + self.counter*10)
            self.label.configure(text=str(self.players[0]))
            self.label1.configure(text=str(self.players[1]))
            self.label2.configure(text=str(self.players[2]))
            self.counter += 1
        elif self.gamemode == 6:
            if self.playerselection == loser0:
                self.players[loser1].removetime(20)
                if loser1 == 0:
                    self.label.configure(text=str(self.players[0]))
                elif loser1 == 1:
                    self.label1.configure(text=str(self.players[1]))
                else:
                    self.label2.configure(text=str(self.players[2]))
            else:
                self.players[loser0].removetime(20)
                if loser0 == 0:
                    self.label.configure(text=str(self.players[0]))
                elif loser0 == 1:
                    self.label1.configure(text=str(self.players[1]))
                else:
                    self.label2.configure(text=str(self.players[2]))                

    def setgamemode(self, mode):
        global loser0
        global loser1
        if mode != 0:
            self.newplayerflag = False
            self.newgameflag = True
            self.previousgamemode = mode
        self.secondcounter = 0
        if mode == 5:
            self.counter = 0
        self.gamemode = mode       
        self.label.configure(bg = playercolor, fg = 'white')
        self.label1.configure(bg = playercolor, fg = 'white')
        self.label2.configure(bg = playercolor, fg = 'white')
        
        if mode == 0:
            self.pause_button.configure(bg = 'blue')
        elif mode == 1:
            self.pause_button.configure(bg = 'brown')
            self.game_button_1.configure(bg = 'blue')
            self.game_button_2.configure(bg = 'brown')
            self.game_button_3.configure(bg = 'brown')
            self.game_button_4.configure(bg = 'brown')
            self.game_button_5.configure(bg = 'brown')
            self.game_button_6.configure(bg = 'brown')
        elif mode == 2:
            self.pause_button.configure(bg = 'brown')
            self.game_button_1.configure(bg = 'brown')
            self.game_button_2.configure(bg = 'blue')
            self.game_button_3.configure(bg = 'brown')
            self.game_button_4.configure(bg = 'brown')
            self.game_button_5.configure(bg = 'brown')
            self.game_button_6.configure(bg = 'brown')
        elif mode == 3:
            self.pause_button.configure(bg = 'brown')
            self.game_button_1.configure(bg = 'brown')
            self.game_button_2.configure(bg = 'brown')
            self.game_button_3.configure(bg = 'blue')
            self.game_button_4.configure(bg = 'brown')
            self.game_button_5.configure(bg = 'brown')
            self.game_button_6.configure(bg = 'brown')
        elif mode == 4:
            self.pause_button.configure(bg = 'brown')
            self.game_button_1.configure(bg = 'brown')
            self.game_button_2.configure(bg = 'brown')
            self.game_button_3.configure(bg = 'brown')
            self.game_button_4.configure(bg = 'blue')
            self.game_button_5.configure(bg = 'brown')
            self.game_button_6.configure(bg = 'brown')
        elif mode == 5:
            self.pause_button.configure(bg = 'brown')
            self.game_button_1.configure(bg = 'brown')
            self.game_button_2.configure(bg = 'brown')
            self.game_button_3.configure(bg = 'brown')
            self.game_button_4.configure(bg = 'brown')
            self.game_button_5.configure(bg = 'blue')
            self.game_button_6.configure(bg = 'brown')
        elif mode == 6:
            self.pause_button.configure(bg = 'brown')
            self.game_button_1.configure(bg = 'brown')
            self.game_button_2.configure(bg = 'brown')
            self.game_button_3.configure(bg = 'brown')
            self.game_button_4.configure(bg = 'brown')
            self.game_button_5.configure(bg = 'brown')
            self.game_button_6.configure(bg = 'blue')
            if self.finalflag == False:
                if self.players[0].timeleft > self.players[1].timeleft and self.players[0].timeleft > self.players[2].timeleft:
                    self.label.configure(text= self.players[0].name + ": Gewonnen!")
                    loser0 = 1
                    loser1 = 2

                elif self.players[1].timeleft > self.players[0].timeleft and self.players[1].timeleft > self.players[2].timeleft:
                    self.label1.configure(text= self.players[1].name + ": Gewonnen!")
                    loser0 = 0
                    loser1 = 2
                else:

                    self.label2.configure(text= self.players[2].name + ": Gewonnen!")
                    loser0 = 0
                    loser1 = 1
            
            else:
                if self.players[0].timeleft < self.players[1].timeleft and self.players[0].timeleft < self.players[2].timeleft:
                    self.label.configure(text= self.players[0].name + ": Verloren!")
                    loser0 = 1
                    loser1 = 2

                elif self.players[1].timeleft < self.players[0].timeleft and self.players[1].timeleft < self.players[2].timeleft:
                    self.label1.configure(text= self.players[1].name + ": Verloren!")
                    loser0 = 0
                    loser1 = 2
                else:
                    self.label2.configure(text= self.players[2].name + ": Verloren!")
                    loser0 = 0
                    loser1 = 1                
        
    def setplayerselection(self, selection):
        self.newplayerflag = True
        self.playerselection = selection
        self.secondcounter = 0
        if selection == 0:
            self.label.configure(bg = 'yellow', fg = 'black')
            self.label1.configure(bg = playercolor, fg = 'white')
            self.label2.configure(bg = playercolor, fg = 'white')
        elif selection == 1:
            self.label.configure(bg = playercolor, fg = 'white')
            self.label1.configure(bg = 'yellow', fg = 'black')
            self.label2.configure(bg = playercolor, fg = 'white')
        elif selection == 2:
            self.label.configure(bg = playercolor, fg = 'white')
            self.label1.configure(bg = playercolor, fg = 'white')
            self.label2.configure(bg = 'yellow', fg = 'black')
        if self.gamemode == 0:
            self.gamemode = self.previousgamemode
            self.pause_button.configure(bg = 'brown')
        
        
    def countdown(self):
        "Main loop"


        if self.players[0].timeleft <= 0:
            if self.finalflag == 0:
                self.label.configure(text= self.players[0].name + ": Verloren!")
            else:
                self.label.configure(text= self.players[0].name + ": Verloren!")
                if loser1 == 1:
                    self.label1.configure(text=self.players[1].name + ": Gewonnen!")
                else:
                    self.label2.configure(text=self.players[2].name + ": Gewonnen!")
                    
        elif self.players[1].timeleft <= 0:
            if self.finalflag == 0:
                self.label1.configure(text= self.players[1].name + ": Verloren!")
            else:
                self.label1.configure(text= self.players[1].name + ": Verloren!")
                if loser1 == 2:
                    self.label2.configure(text=self.players[2].name + ": Gewonnen!")
                else:
                    self.label.configure(text=self.players[0].name + ": Gewonnen!")
                    
        elif self.players[2].timeleft <= 0:
            if self.finalflag == 0:
                self.label2.configure(text= self.players[2].name + ": Verloren!")
            else:
                self.label2.configure(text= self.players[2].name + ": Verloren!")
                if loser0 == 0:
                    self.label.configure(text=self.players[0].name + ": Gewonnen!")
                else:
                    self.label1.configure(text=self.players[1].name + ": Gewonnen!")
            
            
            
            
        elif self.gamemode == 1:
            self.label.configure(text=str(self.players[0]))
            self.label1.configure(text=str(self.players[1]))
            self.label2.configure(text=str(self.players[2]))
            
            
        elif self.gamemode == 6: 
            if self.newplayerflag == True:
                self.players[self.playerselection].timeleft = self.players[self.playerselection].timeleft - 1
            
            if loser0 == 0 or loser1 == 0:
                self.label.configure(text=str(self.players[0]))
            if loser0 == 1 or loser1 == 1:
                self.label1.configure(text=str(self.players[1]))
            if loser0 == 2 or loser1 == 2:
                self.label2.configure(text=str(self.players[2]))
            
            
        elif self.gamemode != 0:
            if self.newplayerflag == True:
                self.players[self.playerselection].timeleft = self.players[self.playerselection].timeleft - 1
            self.label.configure(text=str(self.players[0]))
            self.label1.configure(text=str(self.players[1]))
            self.label2.configure(text=str(self.players[2]))


                
        self.after(1000, self.countdown)
        
        


# In[5]:


import tkinter as tk


class getNames(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.label1 = tk.Label(self, text='Voer de namen van de spelers in!', bg = backgroundcolor)
        self.label1.config(font=('helvetica', fontplayersize))
        self.label1.grid(row=0, columnspan = 2)

        self.label2 = tk.Label(self, text='Speler 1: ', bg = backgroundcolor)
        self.label2.config(font=('helvetica', fontplayersize))
        self.label2.grid(row=1, column = 0)
        
        self.label3 = tk.Label(self, text='Speler 2: ', bg = backgroundcolor)
        self.label3.config(font=('helvetica', fontplayersize))
        self.label3.grid(row=2, column = 0)
            
        self.label4 = tk.Label(self, text='Speler 3: ', bg = backgroundcolor)
        self.label4.config(font=('helvetica', fontplayersize))
        self.label4.grid(row=3, column = 0)
        
        self.entry1 = tk.Entry(self, width = entrywidth, font=('helvetica', fontplayersize)) 
        self.entry1.grid(row=1, column = 1)
        
        self.entry2 = tk.Entry(self, width = entrywidth, font=('helvetica', fontplayersize)) 
        self.entry2.grid(row = 2, column = 1)
        
        self.entry3 = tk.Entry(self, width = entrywidth, font=('helvetica', fontplayersize)) 
        self.entry3.grid(row =3, column = 1)

        self.button1 = tk.Button(self, text='Akkoord!', command= self.getSquareRoot , bg='brown', fg='white', font=('helvetica', fontquestionsize, 'bold'))
        self.button1.grid(row = 4, columnspan = 2)

    def getSquareRoot(self):
        global name1
        global name2
        global name3
        name1 = self.entry1.get()
        name2 = self.entry2.get()
        name3 = self.entry3.get()
        if name1 == "" or name2 == "" or name3 == "":
            self.label5 = tk.Label(self, text="Voer 3 namen in!", fg='red', bg = backgroundcolor)
            self.label5.grid(row = 5, columnspan=2)
        else:
            self.destroy()     


# In[6]:


root = getNames()
root.configure(background=backgroundcolor)
root.title("Slimste Mens Start-Up")
root.mainloop()
app = ExampleApp()
app.configure(background=backgroundcolor)
app.title("De Slimste Mens")
app.mainloop()

