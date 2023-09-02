import pygame
from kivy.app import App 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import StringProperty,NumericProperty,ListProperty 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
import csv
from vosk import Model, KaldiRecognizer
import pyaudio
from csv import writer
import pandas as pd
import os
import numpy as np

pygame.init()
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
Window.clearcolor = (1,1,1,1)
Window.size = (400,630)

class RegWindow(Screen):
    pass
class SignWindow(Screen):
    
    err_msg1 = StringProperty()
    
    def sCheck(self,na,pa):
        self.nmn = StringProperty(na)
        nm = pd.read_csv('data/users.csv',usecols = [0])
        nm1 = nm.to_string(index=False).split()
        ps = pd.read_csv('data/users.csv',usecols = [1])
        ps1 = ps.to_string(index=False).split()

        if na in nm1 and pa in ps1:
            if ps1.index(pa) == nm1.index(na):
                self.parent.current='main'
        else:
            self.err_msg1 = 'Username or Passwords not correct!!'
            self.parent.current='sign'   


class SignUWindow(Screen):
    
    err_msg = StringProperty()
    
    def addU(self,n,p,p1):  #n = 'hatem' ,p = '1212' , p1 = '1212'
        print(n,p,p1)
        vc = pd.read_csv('data/users.csv',usecols = [0])
        n1 = vc.to_string(index=False).split()
        q = [] 
        q.append(n)
        q.append(p) 
        
        if n != '' and p != '':
            if p1 != p:
                self.err_msg = 'passwords not matched!!'
            else:
                if n in n1:
                    self.err_msg = 'Name is already exist'
                    self.parent.current='signU'
                else:
                    self.parent.current='sign'

                    with open('data/users.csv', 'a',encoding="utf-8-sig") as f_object:
                            writer_object = writer(f_object,lineterminator = '\n')
                            writer_object.writerow(q)
                            f_object.close()
        else:
            self.err_msg = 'Enter Username and Password'

class MainWindow(Screen):
    pass

class Wpage(Screen):
    sor = sorted(os.listdir('testImgs/'))
    olist = sorted(os.listdir('testImgs/'))
    solist = sorted(os.listdir('sounds/'))
    result = StringProperty('white')
    im = StringProperty(olist[0])
    butN = StringProperty('ANSWER')
    sx = NumericProperty(0)
    err_n = NumericProperty(0)
    

    def plso(self):
        print(self.solist)
        pygame.mixer.music.load('sounds/'+self.solist[0])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def reco(self,r):

        if r == '':
            self.butN = 'ANSWER'
            self.im = self.olist[0]
            self.sx = 0

        else:
            res = r+'.png'
            if res == self.olist[0]:
                self.sx+=1
                self.va = str(self.sx)
                self.result = 'correct'
                self.olist.pop(0)
                self.solist.pop(0)

                if len(self.olist) == 0:
                    print('done')
                else:
                    self.im = self.olist[0]
                    print(self.sx)

            else:
                self.result = 'wrong'
                self.err_n +=1
                print(self.err_n)
                if self.err_n == 3:
                    print('You lose')

    def addScore(self,sn,sc):

        v=np.column_stack((sn, sc))
        print(v)
        with open('data/sc.csv', 'a',encoding="utf-8-sig") as f_object:

            writer_object = writer(f_object,lineterminator = '\n')
            
            for i in v:
                writer_object.writerow(i)
    
            f_object.close()

class Spage(Screen):

    sor = sorted(os.listdir('testImgs/'))
    olist = sorted(os.listdir('testImgs/'))
    solist = sorted(os.listdir('sounds/'))
    result = StringProperty('white')
    im = StringProperty(olist[0])
    sx = NumericProperty(0)
    err_n = NumericProperty(0)
    resl = StringProperty()
    
    def plso(self):

        pygame.mixer.music.load('sounds/'+self.solist[0])
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def spd(self):

        self.model = Model(r"v/vosk-model-small-en-us-0.15")
        self.recognizer = KaldiRecognizer(self.model,16000)
        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
        self.stream.start_stream()

        while True:
            self.data = self.stream.read(4096)

            if self.recognizer.AcceptWaveform(self.data):
                self.text = self.recognizer.Result()
                self.resl = self.text[14:-3]+'.png'
                print(self.resl)
                if(self.resl != ''):
                    
                    break
        
        if self.resl == '':

            self.sx = 0
        
        else:
            self.res = self.resl
        
            if self.res == self.olist[0]:
                self.sx+=1
                self.va = str(self.sx)
                self.result = 'correct'
                self.olist.pop(0)
                self.solist.pop(0)
                if len(self.olist) == 0:
                    print('done')
                else:
                    self.im = self.olist[0]
                    print(self.sx)
            else:
                self.result = 'wrong'
                self.err_n +=1
                print(self.err_n)
        
                if self.err_n == 3:
                    print('You lose')        

    def addScore(self,sn,sc):
        
        v=np.column_stack((sn, sc))
        print(v)
        with open('data/sc.csv', 'a',encoding="utf-8-sig") as f_object:
 
            writer_object = writer(f_object,lineterminator = '\n')
            
            for i in v:
                writer_object.writerow(i)
    
            f_object.close() 
class Lbpage(Screen):
    
    val0 = StringProperty()
    val1 = StringProperty()
    val2 = StringProperty()
    val3 = StringProperty()
    val4 = StringProperty()

    vlist = [val0,val1,val2,val3,val4]

    sval0 = StringProperty()
    sval1 = StringProperty()
    sval2 = StringProperty()
    sval3 = StringProperty()
    sval4 = StringProperty()
    
    svlist = [sval0,sval1,sval2,sval3,sval4]

    def ref(self):
        
        self.nn = pd.read_csv('data/sc.csv',usecols = [0])
        self.ss = pd.read_csv('data/sc.csv',usecols = [1])
        self.j = self.nn.to_string(index=False).split()
        self.s = self.ss.to_string(index=False).split()
           
        for i in range(len(self.s)):
            for h in range(len(self.s)-1):
                if self.s[i]>self.s[h]:
                    self.s[i],self.s[h] = self.s[h],self.s[i]
                    self.j[i],self.j[h] = self.j[h],self.j[i]
        self.sval0 = self.s[0]#s =[6,5,5,5,4]
        self.sval1 = self.s[1]
        self.sval2 = self.s[2]
        self.sval3 = self.s[3]
        self.sval4 = self.s[4]
        self.val0 = self.j[0] #j = [alaa,ali,randy,lala,john]
        self.val1 = self.j[1]
        self.val2 = self.j[2]
        self.val3 = self.j[3]
        self.val4 = self.j[4]  

class WinPage(Screen):
    pass

class LosePage(Screen):
    pass

class WindowsManager(ScreenManager):
    pass

kv = Builder.load_file('st.kv')

class myApp(App):
    def build(self):
        self.title = 'English for Kids'
        return kv

if __name__ == '__main__':
    myApp().run()