import pyfiglet
import requests
import urllib3
import time
import sys

print(f'\033[34m{pyfiglet.Figlet().renderText("kpag3s")}\033[0;0m')
time.sleep(.8)

info = '''
 para usar basta usar o seguinte padrão:
    python3 main.py https://domonio.com/ wordlist.txt
 
 você tambem pode passar um arquivo com dominios, por exemplo
    python3 main.py listadominios.txt wordlist.txt

 você tambem pode pedir para exibir apenas um codigo de status
  (basta colocar o codigo logo apos o dominio)

  IMPORTANTE!!
    para indentificar se você passou um arquivo ou um dominio,
    você deve colocar a barra '/' no final do dominio.
'''

try:
    dominio = sys.argv[1]
    wordlist = sys.argv[2]
except:
    print(info)
    exit()
try:
    codigo = sys.argv[3]
except: 
    codigo = None

if dominio[len(dominio) - 1] == '/': # se entrar aqui é um dominio
    words = open(wordlist)
    for word in words.readlines():
        word = word.replace('\n','')
        link = str(dominio)+str(word)
        try:
            requisicao = requests.get(link)
            status = str(requisicao.status_code)
            if codigo != None:
                if str(codigo) == status:
                    print(f'{link}')
            else:
                print(f'{link}\t[\033[36m{status}\033[0;0m]')
        except requests.Timeout:
            print(f'A conexão com "{link}" demorou muito para responder')


else: # se entrar aqui é uma lista de dominios
    dominios = open(dominio)
    for dominio in dominios.readlines():
        dominio = dominio.replace('\n','')
        words = open(wordlist)
        for word in words.readlines():
            word = word.replace('\n','')
            link = str(dominio)+str(word)
            requisicao = requests.get(link)
            status = str(requisicao.status_code)
            if codigo != None:
                if str(codigo) == status:
                    print(f'{link}\t[\033[36m{status}\033[0;0m]')
            else:
                print(f'{link}\t[\033[36m{status}\033[0;0m]')
        words.close()
        