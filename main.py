import time
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.rule import Rule
from rich import print
from rich.panel import Panel
from urllib.parse import quote

console = Console()

console.print("[bold]☀️ Weather\n", justify="center")
console.rule(style="white")


site_clima = "https://www.climaeradar.com.br/previsao-tempo/"


while True:
    cidade = input("Digite uma cidade: ")
    print("\n")
    minha_cidade = site_clima + quote(cidade)
    print(f"URL: {minha_cidade}\n")
    print(f"Buscando previsões do tempo para '{cidade}'\n")
    time.sleep(1)

    resultado = requests.get(minha_cidade)
    soup = BeautifulSoup(resultado.text, "html.parser")

    if resultado.status_code == 200:
        print("Conectando ao servidor...")
        time.sleep(1)
        console.print("[green]✅️ Acesso concedido. \n")
        time.sleep(1)

        temperatura = soup.find("span", class_="air-temp")
        tempo = soup.find("h1")

        estado = soup.find("wo-nowcast-time-location-context")

        descricao = soup.find("div", class_="weather-text")

        nascer_do_sol = soup.find("div", class_="info-line")
        por_do_sol = soup.find("div", class_="info-line middle")

        lua = soup.find("div", class_="moon-text")

        qualidade_ar = soup.find("wo-air-quality-indicator")
        
       
        console.print(
            Panel(
                f"{tempo.text}\n\n"
                f"Estado: {estado.text}\n\n"
                f"Temperatura: {temperatura.text}\n\n"
                f"{descricao.text}\n\n"
                f"Nascer do sol: {nascer_do_sol.text}\n\n"
                f"Pôr-do-sol: {por_do_sol.text}\n\n"
                f"Qualidade do ar: {qualidade_ar.text}\n\n"
                f"Lua: {lua.text}\n\n",
                
                 
            )
        )
        
        


    else:
        console.print("[red]❌️ Acesso negado. \n")
        time.sleep(1)
