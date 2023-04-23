# Previsão do tempo API OpenWeather
cidade, api_key = 'Aracaju,BR', 'sua_API'
url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()
temperatura = data['main']['temp']
tempo = data['weather'][0]['description']
umidade = data['main']['humidity']
PrevisaoTempo= f'Previsão do tempo para {cidade}: Temp: {data["main"]["temp"]}°C - Descrição: {data["weather"][0]["description"]} - Humidade: {data["main"]["humidity"]}%'
print(PrevisaoTempo)
