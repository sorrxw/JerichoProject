# Made by Sorrxw
# Secret Message Translator - Name: Jericho
# Circa 08/27/2023

def main():
    
    # Title
    print('------------------------------------------')
    print("      _           _      _  ")         
    print("     | |         (_)    | |      ")   
    print("     | | ___ _ __ _  ___| |__   ___ ") 
    print(" _   | |/ _ \ '__| |/ __| '_ \ / _ \ ") 
    print("| |__| |  __/ |  | | (__| | | | (_) |")
    print(" \____/ \___| _|  |_|\___|  _|\|_|/  ")
                                      
                                      
    print('------------------------------------------')
    print(" ")
    
    # Dictionary of Translatative References
    jerichoDict = {
  " ": "<>",
  "q": "и",
  "Q": "и",
  "W": "文",
  "w": "文",
  "E": "يا",
  "e": "يا"
    }
    
    # Alias Selection Prompt
    userAlias = input("Hello! Welcome to the Jericho Secret Message Translator. What alias would you like to use?")
    print(" ")
    print("Welcome, " + userAlias + ". Please refer to the controls below for the following question. Type the corresponding number to the path that you would like to take.")
    
    # Introduction to main program
    print("1: Encode a secret message")
    print("2: Decode a secret message")
    print(" ")
    initialQuestion = input("Would you like to decode or encode a secret message, " + str(userAlias) + "?")
    
    print(" ")
    
    if initialQuestion == "1":
        encodeInput = input("Type or copy and paste the message you would like to encode.")
        print(" ")
        encodeOutput = ""
        for i in encodeInput:
            encodeOutput = encodeOutput + jerichoDict[i]
        print("Here is your encoded message: " + encodeOutput)
        
    if initialQuestion == "2":
        decodeInput = input("Type or copy and paste the message you would like to decode.")
        decodeOutput = ""
        for i in decodeInput:
            decodeOutput = decodeOutput + jerichoDict[i]
        print("Here is your decoded message: " + decodeOutput)
    
main()