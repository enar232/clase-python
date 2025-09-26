#if

edad = 12


if edad < 13: 
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
else: 
    print("eres un adulto")

edad = 19
tiene_permiso = True
if edad >= 18:
    print("Puedes entrar")
else:
    if tiene_permiso: 
        print("Puedes entrar con permiso")
    else:
        print("No puedes entrar")
        

