# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:59:02 2024

@author: Madhumitha
"""


import speech_recognition as sr
while True:
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
        
        try:
            filename="draft.txt"
            f=open(filename,"a+")
            
            recognized_text= r.recognize_google(audio)
            print(recognized_text)
            remainder= recognized_text.split()
            while remainder:
                line,remainder=remainder[:5],remainder[5:]
                f.write(' '.join(line)+ "\n")
            if recognized_text =='stop':
                break
        
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Google error: {0}".format(e))
    
