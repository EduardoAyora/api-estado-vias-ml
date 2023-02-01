import tweepy
from datetime import datetime

accidentes = []


def saveFormatedData(tweet):
    print(type(tweet))
    if 'accidente' in tweet:
        textoDivididoPorPalabraAccidente = tweet.split("accidente")
    else:
        textoDivididoPorPalabraAccidente = tweet.split("Accidente")
    textoDespuesDePalabraAccidente = textoDivididoPorPalabraAccidente[1]
    startPositionOfDirection = -1
    for index, char in enumerate(textoDespuesDePalabraAccidente):
        if (char.isupper()):
            startPositionOfDirection = index
            break
    textoDesdeInicioDireccion = textoDespuesDePalabraAccidente[startPositionOfDirection:]
    arrayPalabrasDesdeInicioDireccion = textoDesdeInicioDireccion.split(" ")
    arrayPalabrasDireccion = []
    for word in arrayPalabrasDesdeInicioDireccion:
        lowerWord = word.lower()
        if (word[0].isupper() or lowerWord == "de" or lowerWord == "las" or lowerWord == "los" or lowerWord == "y" or lowerWord == "avenida" or lowerWord == "av." or lowerWord == "calles" or lowerWord == "calle"):
            arrayPalabrasDireccion.append(word)
            if (word[len(word) - 1] == "."):
                break
        else:
            break
    direccion = ' '.join([str(elem) for elem in arrayPalabrasDireccion])
    direccion = direccion.replace(".", "")
    direccion = direccion.replace(",", "")
    direccion = direccion.replace(";", "")
    currentDateAndTime = datetime.now()
    accidentes.append({
        "direccion": direccion,
        "fecha": currentDateAndTime.strftime("%d/%m/%Y"),
        "hora": currentDateAndTime.strftime("%H:%M:%S")
    })


saveFormatedData(
    "#Cuenca | Se registra un accidente de tránsito en la Panamericana Norte, sector redondel Mujeres de Piedra. Circule con precaución en la zona.")
saveFormatedData(
    "Se registra un accidente de tránsito en la Avenida de las Américas, sector control sur, volcamiento de camión, circular con precaución.")
saveFormatedData(
    "#Cuenca: Una mujer resultó herida en un accidente de tránsito registrado en las calles Yaguarcocha y Totoracocha.")
saveFormatedData("#Cuenca | Se hace un llamado al conductor de este taxi que provocó un accidente de tránsito y fugó el pasado jueves 26 de enero de 2023, en la avenida Primero de Mayo. Esto con la finalidad de evitar trámites judiciales. El motocilista permanece internado en una casa de salud.")
saveFormatedData("#ATENCION  Esta mañana, dos personas que se movilizaban en una motocicleta resultaron heridas tras impactarse contra un vehículo de la alcaldía de Chordeleg. El accidente ocurrió en la calle Antiplano y avenida de los Andes, sector Totoracocha, al norte de #Cuenca.")
saveFormatedData("Accidente en la vía rápida Cuenca #Azogues")
saveFormatedData("En #Cuenca un vehículo destruyó una puerta de vidrio e ingreso a una farmacia, el hecho se dio en la Av. González Suárez y García Moreno. El automóvil se encontraba estacionado cuando por accidente la copiloto accionó el switch de encendido.")

print(accidentes)
accidentes = []

class IDPrinter(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        saveFormatedData(tweet.text)
        print(accidentes)


printer = IDPrinter(
    "AAAAAAAAAAAAAAAAAAAAADC4igEAAAAAFN2leiur%2FgEX7T42zQB1HOsAnUc%3DgorTksh5Ij6BmO3Y7NLrZAPO3kFCr2DtGoopRqOQOGc3T3lGN0")
# https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule#build
printer.add_rules(tweepy.StreamRule("#cuenca (accidente OR accidentes)"))
# printer.delete_rules(["1620811005088436225"])
print(printer.get_rules())
printer.filter()

# import pickle
# import numpy as np
# loaded_model = pickle.load(open('ModeloEntrando.sav', 'rb'))
# tfidf = pickle.load(open('tfidf.pickle', 'rb'))
# # resul=tweet.full_text
# resul="hola esto es txt"
# test=np.array([resul])
# tweetsreal = tfidf.transform(test)
# predi=loaded_model.predict(tweetsreal)
