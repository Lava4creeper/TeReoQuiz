#TimeForTeReo v1.0 was created by Thomas Gardner on the 09/07/2021

#Import random and time for later use
import random
import time

#Creating the list of Maaori Words
maaori_list = ["aroha", "awa", "haka", "hangi", "hapu", "hikoi", "hui", "iti", "iwi", "kai", "karakia", "kaumatua", "kauri", "kiwi", "koha", "kohanga reo", "mahi", "mana", "manuhiri", "maori", "marae", "maunga", "moa", "moana", "moto", "nui", "pa", "pakeha", "pounamu", "puku", "rangatira", "taihoa", "tama", "tamahine", "tamariki", "tane", "tangi", "taonga", "tapu", "te reo maaori", "tipuna", "tuatara", "wahine", "wai", "waiata", "waka", "whaikorero", "whakapapa", "whanau", "whenua"]

#Creating the list of English Words
english_list = ["love", "river", "war dance", "feast", "clan", "walk", "gathering", "small", "tribe", "food", "prayer", "elder", "native tree", "native bird", "gift", "maaori preschool", "work", "reputation", "guests", "the people of new zealand", "meeting house", "mountain", "flightless bird", "sea", "island", "large", "hill fort", "european", "greenstone", "stomach", "chief", "wait", "young man", "daughter", "children", "man", "funeral", "precious", "sacred", "the maaori language", "ancestor", "lizard", "woman", "water", "song", "canoe", "speechmaking", "genealogy", "family", "land"]

#Defining Instructions
def instructions(list_or_quiz):
  #Clearing the screen
  for item in range(1, 100):
    print()
  #Giving the user the instructions for the quiz
  print("Instructions:")
  time.sleep(0.75)
  print()
  print("The aim of the game is simple. Get the most words right! simply follow the prompts on the screen, and enter the answer when asked for it. Enter 'exit' to quit the quiz, or wait till the numbers run out when you're not in infinite mode.")
  time.sleep(0.75)
  print()
  print("Tips:")
  time.sleep(0.75)
  print()
  print("You can review the list of vocabulary words from the main menu")
  print("This program is not case-sensitive, meaning that KIA ORA and kia ora are treated the same.")
  time.sleep(0.75)
  print()
  #Letting the user leave when they're ready
  print("Press <enter> to return to main UI")
  input("►").lower()
  print()
  time.sleep(0.75)
  print("Returning to main UI")
  time.sleep(0.75)
  #Returning to main UI
  Main_UI(maaori_list, english_list, list_or_quiz)

#defining Main UI
def Main_UI(maaori_list, english_list, list_or_quiz):
  for item in range(1, 100):
   print()
  #looping the main UI
  while list_or_quiz != "exit":
    #Giving the user their options
    time.sleep(0.75)
    print("Would you like to view the instructions, view the list of vocabulary words or begin the quiz?")
    print()
    #Asking the user which option they'd like to select    
    time.sleep(0.75)
    print("Please enter 'Instructions', 'List' or 'Quiz':")
    list_or_quiz = input("►").lower()
    print()
    #If the user selects list
    if list_or_quiz == "list" or list_or_quiz == "l":
      #Tell the user that they chose list
      time.sleep(0.75)
      print("Showing list of Vocabulary")
      print()
      #Go to the vocabulary list function
      vocab_list(list_or_quiz)
    #If the user selects the quiz
    elif list_or_quiz == "quiz" or list_or_quiz == "q":
      #Tell the user that the quiz is beginning
      time.sleep(0.75)
      print("Beginning quiz")
      print()
      #Go to list
      time.sleep(0.75)
      Quiz_Start(maaori_list, english_list)
    #If the user selects instructions
    elif list_or_quiz == "instructions" or list_or_quiz == "instruction" or list_or_quiz == "i":
      #Tell the user that instructions are being displayed
      time.sleep(0.75)
      print("Showing Instructions")
      print()
      #Go to instructions
      time.sleep(0.75)
      instructions(list_or_quiz)
    #If the user inputs something else
    else:
      #Tell the user that their input was not valid
      time.sleep(0.75)
      print("'{}' is not a valid input. Please input 'Instructions', 'List' or 'Quiz'.".format(list_or_quiz))
      time.sleep(0.75)
      print()


def vocab_list(list_or_quiz):
  continue_with_list = ""
  while continue_with_list != 'xxx':
    time.sleep(0.75)
    print("You have selected the list of vocab words. They will be displayed 10 at a time, press <enter> to continue or type 'xxx' to exit")
    list_number = 0
    for item in range(0, 5):
      for item in range(1, 100):
        print()
      for item in range(0, 10):
        time.sleep(0.75)
        print("{}. Maaori Word: {}, English Translation: {}".format(list_number + 1, maaori_list[list_number], english_list[list_number]))
        list_number += 1
      time.sleep(0.75)
      print("Press <Enter> to continue")
      input("►").lower()
      print()
    time.sleep(0.75)
    print("Returning to main UI")
    print()
    time.sleep(0.75)
    Main_UI(maaori_list, english_list, list_or_quiz)
    
    
def Quiz_Start(maaori_list, english_list):
  input_rounds_to_play = ""
  while input_rounds_to_play != "exit":
    for item in range(1, 100):
      print()
    time.sleep(0.75)
    print("How many games would you like to play? please enter a whole number greater than 0 or <enter> for infinite mode")
    input_rounds_to_play = input("►").lower()
    print()
    if input_rounds_to_play == "":
      time.sleep(0.75)
      print("Infinite mode selected. you can input 'Exit' to leave at any time. Press <enter> to begin")
      time.sleep(0.75)
      input("►").lower()
      time.sleep(0.75)
      infinite_quiz()
    else:
      try:
        if int(input_rounds_to_play) > 0:
          for item in range(1, 100):
            print()
          time.sleep(0.75)
          print ("{} Game(s) Selected. Press <enter> to continue".format(input_rounds_to_play))
          time.sleep(0.75)
          input("►").lower()
          time.sleep(0.75)
          finite_quiz(input_rounds_to_play, maaori_list, english_list)
        else:
          for item in range(1, 100):
            print()
          time.sleep(0.75)
          print("Please enter a whole number greater than 0 or press <enter> for infinite mode. Press <enter> to retry.")
          time.sleep(0.75)
          input("►").lower()
      except TypeError:
        for item in range(1, 100):
          print()
        time.sleep(0.75)
        print("Please enter a whole number greater than 0 or press <enter> for infinite mode. Press <enter> to retry")
        time.sleep(0.75)
        input("►").lower()
      except ValueError:
        for item in range(1, 100):
          print()
        time.sleep(0.75)
        print("Please enter a whole number greater than 0 or press <enter> for infinite mode. Press <enter> to retry")
        time.sleep(0.75)
        input("►").lower()

def infinite_quiz():
  quiz_input_answer = ""
  while quiz_input_answer != "exit":
    for item in range(1, 100):
      print()
    quiz_number_selector = random.randint(0, 49)
    type_of_quiz = random.randint(0, 1)
    if type_of_quiz == 0:
      time.sleep(0.75)
      print("What is the english translation of {}? ".format(maaori_list[quiz_number_selector]))
      quiz_input_answer = input("►").lower()
      print()
      if quiz_input_answer == "exit":
        time.sleep(0.75)
        print()
        print("Exit code selected")
        time.sleep(0.75)
        print()
        print("Returning to main UI")
        time.sleep(0.75)
        print()
        Main_UI(maaori_list, english_list, list_or_quiz)
      elif quiz_input_answer == english_list[quiz_number_selector]:
        time.sleep(0.75)
        print("{} is the correct translation of {}! Yay!!!".format(english_list[quiz_number_selector], maaori_list[quiz_number_selector]))
        print()
        time.sleep(0.75)
        print("Press <enter> to continue")
        input("►").lower()
      else:
        time.sleep(0.75)
        print("Sorry, {} is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_answer, maaori_list[quiz_number_selector], english_list[quiz_number_selector]))
        print()
        time.sleep(0.75)
        print("Press <enter> to continue")
        input("►").lower()
    elif type_of_quiz == 1:
      time.sleep(0.75)
      print("What is the Maaori translation of {}?".format(english_list[quiz_number_selector]))
      quiz_input_answer = input("►").lower()
      if quiz_input_answer == "exit":
        time.sleep(0.75)
        print()
        print("Exit code selected")
        time.sleep(0.75)
        print()
        print("Returning to main UI")
        time.sleep(0.75)
        Main_UI(maaori_list, english_list, list_or_quiz)
      elif quiz_input_answer == maaori_list[quiz_number_selector]:
        print("{} is the correct translation of {}! Yay!!".format(maaori_list[quiz_number_selector], english_list[quiz_number_selector]))
        time.sleep(0.75)
        print()
        print("Press <enter> to continue")
        input("►").lower()
        time.sleep(0.75)
      else:
        print("Sorry, {} is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_answer, english_list[quiz_number_selector], maaori_list[quiz_number_selector]))
        time.sleep(0.75)
        print()
        print("Press <enter> to continue")
        input("►").lower()
        time.sleep(0.75)
      

#Defining the finite quiz
def finite_quiz(input_rounds_to_play, maaori_list, english_list):
  #Setting the variable quiz_input_rounds_to_play to blank
  quiz_input_rounds_to_play = ""
  #Converting answer to an integer
  input_rounds_to_play = int(input_rounds_to_play)
  #Looping the program and setting up an exit code
  while quiz_input_rounds_to_play != "exit":
    #looping the program for the desired amount of rounds
    for item in range(0, input_rounds_to_play):
      for item in range(1, 100):
        print()
      #Selecting the number for the question
      quiz_number_selector = random.randint(0, 49)
      #Selecting the number for the type of quiz
      type_of_quiz = random.randint(0, 1)
      #If the number for the type of quiz is 0, do an English to Maaori quiz
      if type_of_quiz == 0:
        #Asking the user for the English translation of the Maaori word corresponding to the quiz number question
        time.sleep(0.75)
        print("What is the english translation of {}? ".format(maaori_list[quiz_number_selector]))
        quiz_input_answer = input("►").lower()
        print()
        #Checking if the user input the correct translation
        if quiz_input_answer == english_list[quiz_number_selector]:
          #If the user got the question correct, inform them.
          time.sleep(0.75)
          print("{} is the correct translation of {}! Yay!!".format(english_list[quiz_number_selector], maaori_list[quiz_number_selector]))
          print()
        #If the user input the wrong answer
        else:
          #Inform the user that they were wrong
          time.sleep(0.75)
          print("Sorry, {} is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_answer, maaori_list[quiz_number_selector], english_list[quiz_number_selector]))
          print()
        #If the type of quiz number is 1, do a Maaori to English quiz
      elif type_of_quiz == 1:
        time.sleep(0.75)
        print("What is the Maaori Translation of {}? ".format(english_list[quiz_number_selector]))
        quiz_input_answer = input("►").lower()
        print()
        if quiz_input_answer == maaori_list[quiz_number_selector]:
          time.sleep(0.75)
          print("{} is the correct translation of {}! Yay!!".format(maaori_list[quiz_number_selector], english_list[quiz_number_selector]))
          print()
        else:
          time.sleep(0.75)
          print("Sorry, {} is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_answer, english_list[quiz_number_selector], maaori_list[quiz_number_selector]))
          print()
      #Decrease the number of rounds left
      input_rounds_to_play -= 1
      #Tell the user how many rounds they have left
      time.sleep(0.75)
      print("{} Rounds Left".format(input_rounds_to_play))
      print()
      time.sleep(0.75)
      print("Press <enter> to continue")
      time.sleep(0.75)
      input("►").lower()
    #When the number of rounds run out, inform the user they are returning to the main UI
    time.sleep(0.75)
    print("Quiz finished. Returning to main UI")
    #Returning to the main UI
    time.sleep(0.75)
    Main_UI(maaori_list, english_list, list_or_quiz)
      


list_or_quiz = ""
Main_UI(maaori_list, english_list, list_or_quiz)

#→ alt + 26
#► alt + 16
