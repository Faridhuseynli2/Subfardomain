import requests
import json
import os

welcomeText = ""

languages = {
    "1": "Azerbaijani",
    "2": "English",
    "3": "Türkçe",
    "4": "Deutsch", 
    "5": "Español"
}

expressions = {
    "1": {
        "selected": "[i] Azərbaycan dilini seçdiniz",
        "trying": "[i] Subdomen yoxlanılır: {}",
        "found":  "[+] Subdomen keçərlidir: {}",
        "info": "[i] {} subdomen adresi aşkar edildi",
        "target": "[+] Hədəf: ",
        "wordlistError": "[-] Wordlist'in yolu düzgün deyil və ya fayl mövcud deyil. Script dayandırıldı"
    },
    "2": {
        "selected": "[i] You chose english",
        "trying": "[i] Checking subdomain: {}",
        "found":  "[+] Subdomain is valid: {}",
        "info": "[i] {} subdomains detected",
        "target": "[+] Target: ",
        "wordlistError": "[-] Wordlist file path is incorrect or does not exist. Exiting..."
    },
    "3": {
        "selected": "[i] Türkçeyi seçtiniz",
        "trying": "[i] Alt etki alanı kontrol ediliyor: {}",
        "found":  "[+] Alt etki alanı geçerli: {}",
        "info": "[i] {} alt etki alanı tespit edildi",
        "target": "[+] Hedef: ",
        "wordlistError": "[-] Wordlist yolu yanlış veya dosya mevcut değil. Çıkılıyor..."
    },
    "4": {
        "selected": "[i] Sie haben sich für Deutsch entschieden",
        "trying": "[i] Subdomain wird überprüft: {}",
        "found":  "[+] Die Subdomain ist gültig: {}",
        "info": "[i] {} Subdomains erkannt",
        "target": "[+] Ziel: ",
        "wordlistError": "[-] Der Dateipfad der Wortliste ist falsch oder existiert nicht. Verlassen..."
    },
    "5": {
        "selected": "[i] Elegiste español",
        "trying": "[i] Comprobando subdominio: {}",
        "found":  "[+] El subdominio es válido: {}",
        "info": "[i] {} subdominios detectados",
        "target": "[+] Apuntar: ",
        "wordlistError": "[-] La ruta del archivo de la lista de palabras es incorrecta o no existe. Saliendo..."
    },
}

for key, language in languages.items():
    welcomeText += "\n{}. {}".format(key, language)

welcomeText += "\n"
print(welcomeText)

lang_input_text = "[+] Choose a language ('q' to exit): "
selected_language = input(lang_input_text)

while str(selected_language) not in languages:
    if selected_language == 'q':
        print('\n[i] Exiting...', end="\n\n")
        exit()

    print("[-] You choose the wrong language. Try again");
    print(welcomeText);
    selected_language = input(lang_input_text)

expressions = expressions[selected_language]

user_agents = {
    "1": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "2": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "3": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "4": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "5": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
}

user_agent = user_agents.get(selected_language)

print()
target_domain = input(expressions["target"])

wordlist_path = "wordlists/subdomains.list"
current_dir = os.path.join(os.path.dirname(__file__))
wordlist_full_path = os.path.join(current_dir, wordlist_path)

print()
try:
    subdomains_file = open(wordlist_full_path, 'r')
    subdomains = subdomains_file.read().splitlines()
except (FileNotFoundError):
    print("\033[1;31m" + expressions["wordlistError"], end="\n\n")
    exit();
finally:
    subdomains_file.close()

founded_count = 0
for sub in subdomains:
    domain_test = f"http://{sub}.{target_domain}"

    info = expressions["trying"].format(domain_test)
    success = expressions["found"].format(domain_test)

    print(info, end='\r')

    try:
        response = requests.get(
            domain_test,
            headers={"User-Agent": user_agent},
        )
        if response.status_code == 200:
            print("\033[1;32m" + success)
            founded_count += 1

    except requests.exceptions.RequestException:
        print(" " * len(info), end="\r")

print("");
info = expressions['info']
print("\033[1;33m" + info.format(founded_count))
print("")