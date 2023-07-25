import tkinter as tk
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
        global texto
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: ", texto)
        text_box.delete(1.0, tk.END)  # Clear previous text
        text_box.insert(tk.END, texto)

        if "navegador" in texto:
            print("Abrindo o Chrome. Aguarde...")
            os.system("start Chrome.exe")
        elif "Spotify" in texto:
            print("Abrindo o Spotify. Aguarde...")
            os.system("start Spotify.exe")
            
    except sr.UnknownValueError:
        print("Não entendi o que você quis dizer, poderia repetir?")
        text_box.delete(1.0, tk.END)  # Clear previous text
        text_box.insert(tk.END, "Unable to recognize speech")
    except sr.RequestError as e:
        print("Erro durante a requisição ao serviço de reconhecimento de fala; {0}".format(e))
        text_box.delete(1.0, tk.END)  # Clear previous text
        text_box.insert(tk.END, f"Error: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Speech Recognition")

# Create a frame to hold the widgets
frame = tk.Frame(window, padx=50, pady=50)
frame.pack()

# Create a label to display the recognized speech
text_box = tk.Text(frame, width=40, height=10, font=("Arial", 14))
text_box.pack(pady=20)

# Create a button to start listening
button = tk.Button(frame, text="Start Listening", font=("Arial", 12), command=ouvir_microfone)
button.pack()

# Run the main event loop
window.mainloop()
