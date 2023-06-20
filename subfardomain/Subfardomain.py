import requests
import json

welcomeText = ""

languages = {
    "1": "Azerbaijani",
    "2": "English",
    "3": "Türkçe",
    "4": "Deutsch", 
    "5": "Español"
}

for key, language in languages.items():
    welcomeText += "\n{}. {}".format(key, language)

welcomeText += "\n"
print(welcomeText)

selected_language = input("[+] Choose a language: ")

while str(selected_language) not in languages:
    print("[-] You choose the wrong language. Try again");
    print(welcomeText);
    selected_language = input("[+] Choose a language: ")

user_agents = {
    "1": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "2": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "3": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "4": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "5": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
}

user_agent = user_agents.get(selected_language)

print("Enter Domain :")
target_domain = input()

subdomain_list = open("mySubDomain.txt").read()
subdoms = subdomain_list.splitlines()

for sub in subdoms:
    domain_test = f"http://{sub}.{target_domain}"

    try:
        response = requests.get(
            domain_test,
            headers={"User-Agent": user_agent},
        )
        if response.status_code == 200:
            if selected_language == "1":
                print("Domain Tapildi:", domain_test)  # Azerbaijan
            elif selected_language == "2":
                print("Valid Domain:", domain_test)  # English
            elif selected_language == "3":
                print("Geçerli Alan Adı:", domain_test)  # Türkçe
            elif selected_language == "4":
                print("Gültige Domain:", domain_test)  # Almanca
            elif selected_language == "5":
                print("Dominio válido:", domain_test)  # İspanyolca
            else:
                print("Geçerli Alan Adı:", domain_test)  
    except requests.exceptions.RequestException:
        pass