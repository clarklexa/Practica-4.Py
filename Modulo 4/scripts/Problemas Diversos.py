#Problema 1

n = int(input('Introduce un número entero entre 1 y 10: '))
new_file = 'tabla-' + str(n) + '.txt'
f = open(new_file, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()


#Problema 2
n = int(input('Introduce un número entero entre 1 y 10: '))
new_file = 'tabla-' + str(n) + '.txt'
try: 
    f = open(new_file, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())


#Problema 3
n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
new_file = 'tabla-' + str(n) + '.txt'
try: 
    f = open(new_file, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])




#-------------------------------------------------------------------


#Expresiones regulares
import re
from ..modulo import datos
path = './data/re/short_tweets.csv'



#Problema 4

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
patron = r"@robot\d!"
re.findall(patron, s)



#Problema 5
s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

patron1 = r"User_mentions:\d"
patron2 = r"likes: \d"
patron3 = r"number of retweets: \d"

re.findall(patron1, s)
re.findall(patron2, s)
re.findall(patron3, s)




#Problema 6
analisis_sentimientos = datos.read_pandas(path,780,782)

regex = r""  # complete aqui

for tweet in analisis_sentimientos:
    print(tweet)
    
    # Encuentre todos los casos
    print(re.findall(regex, tweet))


#Problema 7


# Escriba una expresión regular para validar un correo
regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example)) 