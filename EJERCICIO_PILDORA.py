email = input("Introduce tu direccion de email: ")

arroba = email.count('@')

if(arroba!=1 or email.rfind('@')==(len(email)-1) or email.rfind('@')==0 ):
    print("EMAIL INCORRECTO")
else:
    print("EMAIL CORRECTO")

