nombre:str = '\tJene'
apellido:str = 'Rios\n'
sobrenombre:str = '\fBoni\n'
edad:str = '\v33\f' 

print(nombre)
print(apellido)
print(sobrenombre)
print(edad)
print('============== SEPARADOR =============')

nombre = nombre.lstrip()
print(nombre)

apellido = apellido.rstrip()
print(apellido)

sobrenombre = sobrenombre.strip()
print(sobrenombre)

print(edad.strip())


