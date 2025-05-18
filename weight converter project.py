#projrct  : weight converter 

weigth = int(input("enter your weight :"))

unit=input("(L)bs or (K)g")
if unit.upper() == "L" :
   converted =  weigth * 0.45 
   print (f" you are {converted} kilos")
else : 
   unit.upper()== "K"
   converted= weigth/ 0.45
   print( f'you are {converted}')

    
