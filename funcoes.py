import os, time
def limparTela ():
    os.system ("cls")
def aguarde (numero):
    time.sleep (numero)

def forca(vidas):
    print ("________")
    print ("|/      |")
    
    if vidas == 5:
        print ("|      (_)   ")
        print ("|")
        print ("|")
        

    elif vidas ==4:
        print ("|      (_)   ")
        print ("|      /     ")
        print ("|")
        
        
    elif vidas == 3:
        print ("|      (_)   ")
        print ("|      /|    ")
        print ("|")
    
    elif vidas == 2:
        print ("|      (_)   ")
        print ("|      /|\   ")
        print ("|")

    elif vidas == 1:
        print ("|      (_)   ")
        print ("|      /|\   ")
        print ("|      /     ")

    elif vidas == 0:
        print ("|      (_)   ")
        print ("|      /|\   ")
        print ("|      / \   ")






    
