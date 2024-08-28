## Variables, imports
floUno = float(input("Float1 > "))

opp = input("Operation? > ") #Choose the operation "+ - / *"
floDos = float(input("Float2 > "))

if opp == "+":
    ans = floUno + floDos
    print(float(floUno), opp , float(floDos),"=", ans)
elif opp == "-":
    ans = floUno - floDos
    print(float(floUno), opp , float(floDos),"=", ans)
elif opp == "/":
    ans = floUno / floDos
    print(float(floUno), opp , float(floDos),"=", ans)
elif opp == "*":
    ans = floUno - floDos
    print(float(floUno), opp , float(floDos),"=", ans)
else:
    print(f"{opp} is not a valid operator")
#Opperation conditions


## Outputs

# Commas (,) seperates prints with spaces between | Plus (+) signs seperates prints without spaces 
