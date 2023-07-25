import speech_recognition as sr
import os

def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando ruído ambiente. Aguarde...")
        r.adjust_for_ambient_noise(source)
        print("Fale alguma coisa:")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: ", texto)

        if "navegador" in texto:
            print("Abrindo o Chrome. Aguarde...")
            os.system("start Chrome.exe")
        elif "Spotify" in texto:
            print("Abrindo o Spotify. Aguarde...")
            os.system("start Spotify.exe")
            
    except sr.UnknownValueError:
        print("Não entendi o que você quis dizer, poderia repetir?")
    except sr.RequestError as e:
        print("Erro durante a requisição ao serviço de reconhecimento de fala; {0}".format(e))

ouvir_microfone()
