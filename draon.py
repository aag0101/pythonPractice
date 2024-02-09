import random
import time

def displayintro():
    print('choose cave 1 or 2')
    print()

def chosecave():
    cave=''
    while cave!='1' and cave!='2':
        print('select 1 or 2')
        cave=input()
    return cave

def checkcave(chosencave):
    print('you approach the cave ...')
    time.sleep(2)
    print('dragon jumps out..')
    print()
    time.sleep(2)

    friendlycave=random.randint(1,2)

    if chosencave==str(friendlycave):
        print('good dragon')
    else:
        print('bad dragon')

playagain='yes'
while playagain =='yes' or playagain=='y':
    displayintro()
    cavenumber=chosecave()
    checkcave(cavenumber)

    print ('play again?')
    playagain=input()
    
            
          
    
    
    
