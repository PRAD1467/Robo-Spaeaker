import os

if __name__ == '__main__':
    print("WELCOME TO ROBO SPEAKER 1.1")
    while(True):
        voice = input("Enter the text you want to speak: ")
        if(voice == 'q'):
            os.system("PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('BYE BYE FRIEND');\"")
            break
        os.system(f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{voice}');\"")






