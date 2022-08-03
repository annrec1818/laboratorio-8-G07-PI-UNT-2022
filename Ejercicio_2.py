import pyttsx3
import speech_recognition
import wikipedia



engine = pyttsx3.init()
recognizer = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()


engine.say(f'Hola, ¿Desea saber sobre algún tema en específico?')
engine.runAndWait()

with mic as source:
    print('calibrando ambiente')
    recognizer.adjust_for_ambient_noise(source)
    print('habla')
    audio = recognizer.listen(source)
    mensaje = recognizer.recognize_google(audio, language="es")
    print('dijiste: ', mensaje)
    


if 'sí' in mensaje.lower():
    engine.say('Ok, dígame el tema de lo que desea saber')
    engine.runAndWait()
    

    with mic as source:
        print('calibrando ambiente')
        recognizer.adjust_for_ambient_noise(source)
        print('habla')
        audio = recognizer.listen(source)
        pregunta = recognizer.recognize_google(audio, language="es")
        print('dijiste: ', pregunta)

    
    wikipedia.set_lang("es")

    def buscador(pregunta):
        respuesta = wikipedia.summary(pregunta, sentences = 3)

        engine.say(respuesta)
        engine.runAndWait()
    
    
    buscador(pregunta)


        
elif 'no' in mensaje.lower():
    engine.say('Ok')
    engine.runAndWait()