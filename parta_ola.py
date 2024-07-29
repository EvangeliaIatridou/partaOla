# Evangelia Iatridou, A.M. 4676
import random
players= int(input('Please input number of players: '))
if (players < 2):
    exit()

beans= int(input('Please input number of beans per player: '))
if (beans < 2):
    exit()
lst=[]
for i in range(1,players+1):              #list of players
    num='Player %d'%i
    lst.append(num)
d = dict.fromkeys(lst,beans)              #dictionary with players' budget
elim = 'no'
delim = dict.fromkeys(lst,elim)           #dictionary with eliminated players ('yes' means that player is eliminated, 'no' means that the player is still in the game)
spinlist = ['Take One','Take Two','Put One', 'Put Two', 'everyone puts 1','Take them all']
randomfirst = lst[random.randint(0,len(lst)-1)]
pot=0
r=0                                       #counts rounds while in 'while pot==0'
rounds=0                                  #counts rounds while in 'while pot!=0'
while pot==0:
         print(60*'-')
         r+=1
         print('Round ',r, ' begins: '+spinlist[4])
         print('Current state: ')
         for z in lst:
             if d[z]>=1:
                 pot+=1
         print('Pot: ', pot)
         for i in lst:
             if d[i]>=1:
                 d[i]= d[i]-1
                 print(i+'\'s budget: ', d[i])
             elif d[i]==0:
                 delim[i]= 'yes'
                 print(i+' is eliminated')         

         while pot!=0:
           print('\n')
           rounds+=1                       

           if rounds==1:                  #order 
             order= randomfirst
           if rounds>=2:
             if order== lst[len(lst)-1]:
                 order = lst[0]
             elif order<lst[len(lst)-1]:
                 order=lst[lst.index(order)+1]
             elif order==lst[lst.index(order)+1]:
                 print('winner is'+order)
                 break

           for i in lst:                  #skip the eliminated player
               if delim[order]=='yes':
                   if order== lst[len(lst)-1]:
                      order = lst[0]
                   else:
                      order=lst[lst.index(order)+1]

           randomspin = spinlist[random.randint(0,len(spinlist)-1)]

           if delim[order]!='yes':        #spin
             if randomspin== 'Take One':  
               if pot>=1:
                  pot-=1
                  d[order]=d[order]+1
               elif pot==0:
                  pot=0
             elif randomspin== 'Take Two': 
               if pot>=2:
                  pot-=2
                  d[order]=d[order]+2
               elif pot<=1:
                  pot-=1
                  d[order]+=1
             elif randomspin=='Put One':
               if d[order]>=1:
                  pot=pot+1
                  d[order]-=1
               elif d[order]==0:
                  delim[order]='yes'
             elif randomspin=='Put Two':  
               if d[order]>=2:
                  d[order]-=2
                  pot+=2
               elif d[order]==1:
                  d[order]-=1
                  pot+=1
                  delim[order]='yes'
               elif d[order]==0:
                  delim[order]='yes'
             elif randomspin=='Take them all':  
               d[order]+=pot
               pot=0
             elif randomspin== 'everyone puts 1':      
                 for i in lst:
                     if d[i]>=1:
                         d[i]-=1
                         pot+=1
                     elif d[i]==0:
                         delim[i]='yes'
                         
           print(order,' spinned ', randomspin)

           p=0                          #winner
           for i in lst:               
               if delim[i]=='no':
                   p+=1
                   y=i
           if p==1:
              print('Game finished:',y,' wins')
              break

           u=0
           if randomspin== 'everyone puts 1':
               for i in lst:              #tie
                 if d[i]==0:
                    u+=1
                    if (u>=2) and (u<=len(lst)):
                        print('Game finished: There is a tie; noone wins.')
                        break

           print('Current state: ')    
           print('Pot: ', pot)
           for z in lst:
               if delim[z]=='no':
                   print(z+'\'s budget: ', d[z])
               elif delim[z]=='yes':
                   print(z,' is eliminated') 

           if pot<=0:                   #round ending
               print('Pot is zero: round ends')
