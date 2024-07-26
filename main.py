import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

API_KEY = 'b1448eafb3144b1a8600dd4016ac29f0' 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def fetch_news():
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            top_headlines = [article['title'] for article in articles[:7]]  
            return top_headlines
        else:
            return ["Sorry, I couldn't fetch the news right now."]
    except Exception as e:
        return [f"Error fetching news: {str(e)}"]

if __name__ == "__main__":
    speak("intellibot loading")
    while True:
        with sr.Microphone() as source:
            print('Listening...')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio)
                print('User thinks: ' + command)

                if 'open Google' in command:
                    webbrowser.open('https://www.google.com')
                    speak('Opening Google')
                elif 'open code' in command.lower():
                    webbrowser.open('https://codeforces.com/')
                    speak('Opening Codeforces')
                elif 'play' in command.lower():
                    webbrowser.open('https://www.youtube.com/watch?v=-E2qhkUNKZY')
                    speak('Playing phonk')
                elif 'lit' in command.lower():
                    webbrowser.open('https://www.leetcode.com')
                    speak('Opening LeetCode')
                elif 'hello' in command:
                    speak('Hi user, I am fine. How is your day today?')
                elif 'how are you' in command:
                    speak('I am just a program, but I am functioning as expected.')
                elif command.lower() == 'intellibot':
                    speak("Yes, I am here.")
                elif 'news' in command.lower():
                    speak("Fetching the latest news headlines.")
                    news_headlines = fetch_news()
                    for headline in news_headlines:
                        speak(headline)
                elif 'stop' in command:
                    speak('Goodbye!')
                    break
                else:
                    speak('You said: ' + command)
            except sr.UnknownValueError:
                print('Sophie could not understand the audio')
            except sr.RequestError as e:
                print(f'Sophie error: {e}')
