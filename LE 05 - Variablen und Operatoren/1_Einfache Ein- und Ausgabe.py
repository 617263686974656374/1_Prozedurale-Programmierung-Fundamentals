# Programm das alle vier Möglichkeiten der Division von zwei einzugebenden Zahlen berechnet und am Bildschirm ausgibt
Zahl1 = int(input("Entry first Number: "))
Zahl2 = int(input("Entry second Number: "))

#   Division (float): divides the first operand by the second
print("First Number:", Zahl1, " divides ", " second Number", Zahl2, "is: ", Zahl1 / Zahl2)
#	Division (floor): divides the first operand by the second
print("First Number:", Zahl1, " division ", " second Number", Zahl2, "is: ", Zahl1 // Zahl2)
#   Modulus: returns the remainder when the first operand is divided by the second
print("First Number:", Zahl1, " modulus ", " second Number", Zahl2, "is: ", Zahl1 % Zahl2)