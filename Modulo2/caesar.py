import string 

todas_letras= string.ascii_letters

dict1={}
key=int(input('Escriba un número entero positivo: '))

for i in range(len(todas_letras)):
    dict1[todas_letras[i]] = todas_letras[(i+key)%len(todas_letras)]

plain_text= input('Ingrese una palabra: ')
cipher_text=[]

for char in plain_text:
    if char in todas_letras:
        temp = dict1[char]
        cipher_text.append(temp)
    else: 
        temp = char
        cipher_text.append(temp)

cipher_text="".join(cipher_text)
print("Texto cipher es: ", cipher_text)

dict2 = {}

for i in range(len(todas_letras)):
    dict2[todas_letras[i]] = todas_letras[(i-key)%(len(todas_letras))]

decrypt_text = []

for char in cipher_text:
    if char in todas_letras:
        temp=dict2[char]
        decrypt_text.append(temp)
    else:
        temp=char
        decrypt_text.append(temp)
    
decrypt_text="".join(decrypt_text)

print("Plain text es: ", decrypt_text)

abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

