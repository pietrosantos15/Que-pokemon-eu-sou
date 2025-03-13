from flask import Flask, render_template, request
import requests, random

app = Flask(__name__)

API_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/"

traducao = {
    "normal": "Normal",
    "fighting": "Lutador",
    "flying": "Voador",
    "poison": "Venenoso",
    "ground": "Terrestre",
    "rock": "Pedra",
    "bug": "Inseto",
    "ghost": "Fantasma",
    "steel": "Aço",
    "fire": "Fogo",
    "water": "Água",
    "grass": "Grama",
    "electric": "Elétrico",
    "psychic": "Psíquico",
    "ice": "Gelo",
    "dragon": "Dragão",
    "dark": "Sombrio",
    "fairy": "Fada"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        idade = int(request.form['idade'])
        nome1 = request.form['nome1']

        if idade > 100 or idade < 1:
            erro = "Idade inválida"
            return render_template('index.html', erro=erro)
        
        numaleatorio = random.randint(1, 926)
        pokemon = idade + numaleatorio
        
        response = requests.get(API_ENDPOINT + str(pokemon))

        if response.status_code == 200:
            data = response.json()
            nome = data["name"].capitalize()
            tipos = [traducao.get(t["type"]["name"], t["type"]["name"]) for t in data["types"]]  # aq ele pega os nome dos tipo
            peso = data["weight"] / 10
            altura = data["height"] * 10
            habilidades = [h["ability"]["name"] for h in data["abilities"]] # precisa disso para pegar direto as habildiades
            imagem = data["sprites"]["front_default"]

            return render_template('index.html',nome=nome, idade=idade, tipos=tipos, peso=peso, altura=altura, habilidades=habilidades, imagem=imagem,nome1=nome1 )

        

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
