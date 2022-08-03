
import pyttsx3
import speech_recognition
import csv
print(csv.__file__)


engine = pyttsx3.init()
recognizer = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()


engine.say('Hola, ¿Desea registrar sus datos a la base?')
engine.runAndWait()

with mic as source:
  print('calibrando ambiente')
  recognizer.adjust_for_ambient_noise(source)
  print('habla')
  audio = recognizer.listen(source)
  mensaje = recognizer.recognize_google(audio, language="es")
  print('dijiste: ', mensaje)



if 'sí' in mensaje.lower():
    
  engine.say('Okay, ¿Existe la base de datos en la que estos van a ser ingresados?')
  engine.runAndWait()
    
  with mic as source:
    print('calibrando ambiente')
    recognizer.adjust_for_ambient_noise(source)
    print('habla')
    audio = recognizer.listen(source)
    respuesta = recognizer.recognize_google(audio, language="es")
    print('dijiste: ', respuesta)
    
    if 'no' in respuesta.lower():
        
      f = open("base.csv", "x")
      with open("base.csv","a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Nombre  ", "  Apellido  " , "  Edad  "])
    
    engine.say('Ok, dícteme su Nombre')
    engine.runAndWait()
    
    print('calibrando ambiente')
    recognizer.adjust_for_ambient_noise(source)
    print('habla')
    audio = recognizer.listen(source)
    Nombre = recognizer.recognize_google(audio, language="es")
    print('dijiste: ', Nombre)
    
    engine.say('Ok, dícteme su Apellido')
    engine.runAndWait()
    
    
    print('calibrando ambiente')
    recognizer.adjust_for_ambient_noise(source)
    print('habla')
    audio = recognizer.listen(source)
    Apellido = recognizer.recognize_google(audio, language="es")
    print('dijiste: ', Apellido)
    
    engine.say('Ok, dícteme su Edad')
    engine.runAndWait()
    

    print('calibrando ambiente')
    recognizer.adjust_for_ambient_noise(source)
    print('habla')
    audio = recognizer.listen(source)
    Edad = int(recognizer.recognize_google(audio, language="es"))
    print('dijiste: ', Edad)
    
          
    with open("base.csv","a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow([Nombre , Apellido , Edad])
    
    engine.say('Los datos han sido ingresados')
    engine.runAndWait()
       
    
elif 'no' in mensaje.lower():
    engine.say('entendido')
    engine.runAndWait()
