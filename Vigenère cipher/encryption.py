from tkinter import *
def encrypt_click(UserInput,OUTPUT,KEYpath):
    OUTPUT.delete('1.0',END)
    line_list = UserInput.get('1.0', 'end').split('\n')
    with open(KEYpath,'r') as f:
        count=0
        temp=0
        key = f.readline()
        for line in line_list:
            for n in range(len(line)):
                temp=ord(line[n])+ord(key[count])               
                if(temp)>158:
                    OUTPUT.insert(END,chr(temp-127))
                else:
                    OUTPUT.insert(END,chr(temp-32))
                count+=1
                if count >= len(key):
                    count = 0
            OUTPUT.insert(END,'\n')

def decrypt_click(UserInput,OUTPUT,KEYpath):
    OUTPUT.delete('1.0',END)
    line_list = UserInput.get('1.0', 'end').split('\n')
    with open(KEYpath,'r') as f:
        count=0
        temp=0
        key = f.readline()
        for line in line_list:
            for n in range(len(line)):
                temp=ord(line[n])-ord(key[count])
                if(temp)<0:
                    OUTPUT.insert(END,chr(temp+127))
                else:
                    OUTPUT.insert(END,chr(temp+32))
                count+=1
                if count >= len(key):
                    count = 0
            OUTPUT.insert(END,'\n')