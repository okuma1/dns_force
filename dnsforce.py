import requests
import sys
import pyfiglet

#banner
texto = "DNS_force"

banner = pyfiglet.figlet_format(texto, font="slant")

print("========================================================")
print(banner)
print("========================================================")

if len(sys.argv) <= 1:
    print("\nMODO DE USO:./script <comando> <target / dominio>")

#ajuda
elif (sys.argv[1] == "-h"):
    print("[COMANDOS]\n")
    print("[ -s ] - Brute Force em Subdominios")


elif (sys.argv[1] == "-s"):
    if len(sys.argv) <= 2:
        print("Esqueceu de adicionar 1 target / dominio!!!")
    else:

        print("[SCAN-SUBDOMINIOS]")

        #wordlist input
        file = input("Insisra o path/wordlist:")
        openfile = open(file, 'r', )
        content = openfile.read()
        subdominios = content.splitlines()

        print("Protocolo utilizado na url:\n")
        print("[ 1 ] - HTTP")
        protocolo = input("[ 2 ] - HTTPS\n>")

        if protocolo == "1":

            print("[Subdominios / HTTP]")

            for subs in subdominios:

                url = "http://{}.{}.".format(subs, sys.argv[2])
                try:
                    requests.get(url)

                except requests.ConnectionError:
                    pass
                else:
                    print(url)

        else:

            print("[Subdominios / HTTPS]")

            for subs in subdominios:
                url = "https://{}.{}.".format(subs, sys.argv[2])

                try:
                    requests.get(url)

                except requests.ConnectionError:
                    pass
                else:
                    print(url)