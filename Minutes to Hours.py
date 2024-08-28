## Variables, imports
mins = int(input("Minutes > "))

hrResult = mins // 60
minDecimal = (mins / 60) - hrResult
minResult = minDecimal * 60


#Opperation conditions

## Outputs
print(hrResult, "hours and", int(minResult), "minutes") # Commas (,) seperates prints with spaces between | Plus (+) signs seperates prints without spaces 
