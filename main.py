import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("jarvis loadaing")
    while True:
        with sr.Microphone() as source:
            print('Listening...')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio)
                print('Sophie thinks: ' + command)

                # Add some basic commands
                if 'open Google' in command:
                    webbrowser.open('https://www.google.com')
                    speak('Opening Google')
                elif 'open code' in command.lower():
                    webbrowser.open('https://codeforces.com/')
                    speak('Opening codeforces')
                elif 'play music' in command.lower():
                    webbrowser.open('https://www.youtube.com/watch?v=4jKkT3d8gdI')
                    speak('sason ki mala p instrumental')
                elif 'play' in command.lower():
                    webbrowser.open('https://www.youtube.com/watch?v=-E2qhkUNKZY')
                    speak('playing phonk')
                elif 'lit' in command.lower():
                    webbrowser.open('https://www.leetcode.com')
                elif 'hello' in command:
                    speak('hii tanushree i am fine ,how is your day today')
                elif 'how are you' in command:
                    speak('I am just a program, but I am functioning as expected.')
                elif command.lower()=='jarvis':
                    speak("yes i am there")
                elif 'stop' in command:
                    speak('Goodbye!')
                    break
                else:
                    speak('You said: ' + command)
            except sr.UnknownValueError:
                print('Sophie could not understand the audio')
            except sr.RequestError as e:
                print(f'Sophie error: {e}')
