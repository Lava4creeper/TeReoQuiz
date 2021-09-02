#TimeForTeReo v1.0 was created by Thomas Gardner on the 01/09/2021

#Import random and time
import random
import time

#Creating the list of Maaori Words
maaori_list = ["aroha", "awa", "haka", "haangi", "hapuu", "hikoi", "hui", "iti", "iwi", "kai", "karakia", "kaumaatua", "kauri", "kiwi", "koha", "koohanga reo", "mahi", "mana", "manuhiri", "maaori", "marae", "maunga", "moa", "moana", "motu", "nui", "paa", "paakehaa", "pounamu", "puku", "rangatira", "taihoa", "tama", "tamahine", "tamariki", "tane", "tangi", "taonga", "tapu", "te reo maaori", "tipuna", "tuatara", "waahine", "wai", "waiata", "waka", "whaikoorero", "whakapapa", "whanau", "whenua"]

#Creating the list of English Words
english_list = ["love", "river", "war dance", "feast", "clan", "walk", "gathering", "small", "tribe", "food", "prayer", "elder", "native tree", "native bird", "gift", "maaori preschool", "work", "reputation", "guests", "the people of new zealand", "meeting house", "mountain", "flightless bird", "sea", "island", "large", "hill fort", "european", "greenstone", "stomach", "chief", "wait", "young man", "daughter", "children", "man", "funeral", "precious", "sacred", "the maaori language", "ancestor", "lizard", "woman", "water", "song", "canoe", "speechmaking", "genealogy", "family", "land"]

#creating the main menu function
def main_menu(maaori_list, english_list, main_menu_user_choice_input):
  #looping the main menu and setting up an exit code
  while main_menu_user_choice_input != "exit":
    #clearing the screen
    for item in range(0, 100):
      print()
    #Giving the user their options to select the instructions, vocabulary words or the quiz
    time.sleep(0.75)
    print("Would you like to view the instructions, view the list of vocabulary words or begin the quiz?")
    print()
    #Asking the user which option they'd like to select    
    time.sleep(0.75)
    print("Please enter 'Instructions', 'List' or 'Quiz':")
    #Let the user input their choice
    main_menu_user_choice_input = input("►").lower()
    print()
    #If the user selects the vocabulary list
    if main_menu_user_choice_input == "list" or main_menu_user_choice_input == "l":
      time.sleep(0.75)
      #Tell the user that they chose vocabulary list
      print("Showing list of Vocabulary")
      print()
      #Go to the vocabulary list function
      vocabulary_list(main_menu_user_choice_input)
    #If the user selects the quiz
    elif main_menu_user_choice_input == "quiz" or main_menu_user_choice_input == "q":
      time.sleep(0.75)
      #Tell the user that they chose the main quiz
      print("Beginning quiz")
      print()
      #Go to the quiz function
      time.sleep(0.75)
      quiz_selector_input(maaori_list, english_list)
    #If the user selects instructions
    elif main_menu_user_choice_input == "instructions" or main_menu_user_choice_input == "instruction" or main_menu_user_choice_input == "i":
      time.sleep(0.75)
      #Tell the user that they chose instructions
      print("Showing Instructions")
      print()
      #Go to  the instructions function
      time.sleep(0.75)
      instructions(main_menu_user_choice_input)
    #If the user inputs the exit code
    elif main_menu_user_choice_input == "exit":
      time.sleep(0.75)
      #tell the user they entered the exit code
      print("Exit code selected. Shutting down program")
      print()
      time.sleep(0.75)
      #Exit the program
      exit()
    #If the user inputs an invalid value
    else:
      time.sleep(0.75)
      #Tell the user the input they have entered is not valid
      print("'{}' is not a valid input. Please input 'Instructions', 'List' or 'Quiz'. press <enter> to continue.".format(main_menu_user_choice_input))
      exit_or_continue = input("►")
      if exit_or_continue == 'exit':
        time.sleep(0.75)
        #tell the user they entered the exit code
        print("Exit code selected. Shutting down program")
        print()
        time.sleep(0.75)
        #Exit the program
        exit()
      time.sleep(0.75)
      print()
  
#creating the instructions function
def instructions(main_menu_user_choice_input):
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
  print("This program uses the double vowel in place of the macron, so take that into account with your answers.")
  time.sleep(0.75)
  print()
  #Letting the user leave when they're ready
  print("Press <enter> to return to main menu")
  input("►").lower()
  print()
  time.sleep(0.75)
  #telling the user they are returning to the main menu
  print("Returning to main menu")
  time.sleep(0.75)
  #Returning to main menu
  main_menu(maaori_list, english_list, main_menu_user_choice_input)

#creating the vocabulary List function
def vocabulary_list(main_menu_user_choice_input):
  #Defining the variable exit_or_continue
  exit_or_continue = ''
  #Looping the code and establishing an exit code
  while exit_or_continue != 'exit':
    #Clearing the screen
    for item in range(0, 100):
      print()
    time.sleep(0.75)
    #Telling the user they have selected the vocabulary list, and telling them how this function works
    print("You have selected the list of vocabulary words. They will be displayed 10 at a time, press <enter> to continue or type 'exit' to exit")
    #letting the user continue when ready
    exit_or_continue = input("►").lower()
    print()
    #if the user entered the exit code, tell them and go back to the main menu
    if exit_or_continue == "exit":
      time.sleep(0.75)
      #Telling the user the exit code was entered
      print("Exit code detected. Returning to main menu.")
      print()
      time.sleep(0.75)
      #Returning the user to the main menu
      main_menu(maaori_list, english_list, main_menu_user_choice_input)
    #Setting the word number to 0
    list_word_number = 0
    #Looping the printouts 5 times to display all 50 words
    for item in range(0, 5):
      #Clearing the screen
      for item in range(1, 100):
        print()
      #If the user entered the exit code, send them to the Main menu
      if exit_or_continue == "exit":
        time.sleep(0.75)
        #Tell the user they entered the exit code
        print("Exit code detected")
        time.sleep(0.75)
        print()
        #Tell the user they're returning to the main menu
        print("Returning to main menu")
        time.sleep(0.75)
        #Returning to the main menu
        main_menu(maaori_list, english_list, main_menu_user_choice_input)
      #Making the words print 10 at a time
      for item in range(0, 10):
        time.sleep(0.75)
        #Telling the user the word's number, its Maaori translation and its English translation
        print("{}. Maaori Word: {}, English Translation: {}".format(list_word_number + 1, maaori_list[list_word_number], english_list[list_word_number]))
        #adding 1 to the list number
        list_word_number += 1
      time.sleep(0.75)
      #allowing the user to exit when they're ready
      print("Press <Enter> to continue")
      exit_or_continue = input("►").lower()
      print()
    time.sleep(0.75)
    #Telling the user they are returning to the Main menu
    print("Returning to main menu")
    print()
    time.sleep(0.75)
    #Returning to the main menu
    main_menu(maaori_list, english_list, main_menu_user_choice_input)

#creating the quiz_selector_input function    
def quiz_selector_input(maaori_list, english_list):
  #Creating the variable input_rounds_to_play
  input_rounds_to_play = ""
  #Looping the code and setting up an exit code
  while input_rounds_to_play != "exit":
    #Clearing the screen
    for item in range(1, 100):
      print()
    time.sleep(0.75)
    #Asking the user how many games they'd like to play, or if they want to play infinite mode
    print("How many games would you like to play? please enter a whole number greater than 0 or <enter> for infinite mode")
    #Letting the user input their answer
    input_rounds_to_play = input("►").lower()
    print()
    #If the user selects infinite mode
    if input_rounds_to_play == "":
      time.sleep(0.75)
      #Inform the user they have selected infinite mode and let them start when ready
      print("Infinite mode selected. you can input 'Exit' to leave at any time. Press <enter> to begin")
      time.sleep(0.75)
      #let the user continue when ready
      exit_or_continue = input("►").lower()
      print()
      #If the user entered the exit code, tell them and go back to main menu
      if exit_or_continue == "exit":
        time.sleep(0.75)
        #Tell the user they entered the exit code
        print("exit code detected")
        print()
        time.sleep(0.75)
        #tell the user they are returning to the main menu
        print("returning to main menu")
        time.sleep(0.75)
        #return to the main menu
        main_menu(maaori_list, english_list, main_menu_user_choice_input)
      time.sleep(0.75)
      #Send the user to the infinite_quiz function
      infinite_quiz()
    #If the user enters the exit code
    elif input_rounds_to_play == "exit":
      time.sleep(0.75)
      #Tell the user they entered the exit code
      print("Exit code detected.")
      time.sleep(0.75)
      print()
      #Tell the user they are returning to the main menu
      print("Returning to main menu")
      time.sleep(0.75)
      #Return to the main menu
      main_menu(maaori_list, english_list, main_menu_user_choice_input)
    #If the user doesn't select infinite mode
    else:
      #Try to make the variable input_rounds_to_play an integer
      try:
        #If the variable input_rounds_to_play is an integer and greater than 0
        if int(input_rounds_to_play) > 0:
          #Clear the screen
          for item in range(1, 100):
            print()
          time.sleep(0.75)
          #Tell the user how many games have been selected and let them start when ready
          print ("{} Game(s) Selected. Press <enter> to continue".format(input_rounds_to_play))
          time.sleep(0.75)
          #Let the user continue when ready
          exit_or_continue = input("►").lower()
          print()
          #If the user enters the exit code
          if exit_or_continue == "exit":
            time.sleep(0.75)
            #Tell the user they entered the exit code
            print("exit code detected")
            print()
            time.sleep(0.75)
            #Tell the user they are returning to the main menu
            print("returning to main menu")
            time.sleep(0.75)
            #Return to the main menu
            main_menu(maaori_list, english_list, main_menu_user_choice_input)
          time.sleep(0.75)
          #Go to the function finite_quiz 
          finite_quiz(input_rounds_to_play, maaori_list, english_list)
        #If the variable input_rounds_to_play isn't an integer greater than 0
        else:
          #Clear the screen
          for item in range(1, 100):
            print()
          time.sleep(0.75)
          #Tell the user they have entered an invalid input, and let them try again when they're ready
          print("'{}' is an invalid input. Please enter a whole number greater than 0 or press <enter> for infinite mode. Press <enter> to retry.".format(input_rounds_to_play))
          time.sleep(0.75)
          #Let the user continue when ready
          exit_or_continue = input("►").lower()
          #If the user entered the exit code
          if exit_or_continue == "exit":
            time.sleep(0.75)
            #Tell the user they entered the exit code
            print("exit code detected")
            print()
            time.sleep(0.75)
            #Tell the user they're are returning to the main menu
            print("returning to main menu")
            time.sleep(0.75)
            #returning to the main menu
            main_menu(maaori_list, english_list, main_menu_user_choice_input)
      #If the variable input_rounds_to_play is a TypeError when converted to an integer  
      except TypeError:
        #Clear the screen
        for item in range(1, 100):
          print()
        time.sleep(0.75)
        #Tell the user they have entered an invalid input, and let them try again when they're ready
        print("Please enter a whole number greater than 0 or press <enter> for infinite mode. Press <enter> to retry")
        time.sleep(0.75)
        #let the user continue when ready
        exit_or_continue = input("►").lower()
        #If the user entered the exit code
        if exit_or_continue == "exit":
          time.sleep(0.75)
          #Tell the user they entered the exit code
          print("exit code detected")
          print()
          time.sleep(0.75)
          #Tell the user they're returning to the main menu
          print("returning to main menu")
          time.sleep(0.75)
          #Return to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)
      #If the variable input_rounds_to_play is a ValueError when converted to an integer
      except ValueError:
        #Clear the screen
        for item in range(1, 100):
          print()
        time.sleep(0.75)
        #Tell the user they have entered an invalid input, and let them try again when they're ready
        print("Please enter a whole number greater than 0 or press <enter> for infinite mode. Press <enter> to retry")
        time.sleep(0.75)
        #Let the user continue when ready
        exit_or_continue = input("►").lower()
        #If the user entered the exit code
        if exit_or_continue == "exit":
          time.sleep(0.75)
          #Tell the user they entered the exit code
          print("exit code detected")
          print()
          time.sleep(0.75)
          #Tell the user they're returning to the main menu
          print("returning to main menu")
          time.sleep(0.75)
          #Return to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)

#creating the function infinite_quiz
def infinite_quiz():
  #Creating the variable quiz_input_user_answer
  quiz_input_user_answer = ""
  #Looping the code and setting up an exit code
  while quiz_input_user_answer != "exit":
    #Clearing the screen
    for item in range(1, 100):
      print()
    #Choosing a random number between 0 and 49 and assigning it to quiz_question_number_selector
    quiz_question_number_selector = random.randint(0, 49)
    #Choosing a random number between 0 and 1 and assigning it to type_of_quiz_number_selector
    type_of_quiz_number_selector = random.randint(0, 1)
    #If type_of_quiz_number_selector is equal to 0, run a Maaori to English list
    if type_of_quiz_number_selector == 0:
      time.sleep(0.75)
      #Ask the user what the english translation of the maaori word corresponding to the variable quiz_question_number_selector is
      print("What is the english translation of {}? ".format(maaori_list[quiz_question_number_selector]))
      #let the user input their answer
      quiz_input_user_answer = input("►").lower()
      print()
      #If the user entered the exit code
      if quiz_input_user_answer == "exit":
        time.sleep(0.75)
        print()
        #tell the user they selected the exit code
        print("Exit code selected")
        time.sleep(0.75)
        print()
        #Tell the user they are returning to the main menu
        print("Returning to main menu")
        time.sleep(0.75)
        #Return to main menu
        main_menu(maaori_list, english_list, main_menu_user_choice_input)
      #If the user enters the correct translation of the Maaori word corresponding to the variable quiz_question_number_selector
      elif quiz_input_user_answer == english_list[quiz_question_number_selector]:
        time.sleep(0.75)
        #Tell the user they have entered the correct translation
        print("{} is the correct translation of {}! Yay!!!".format(english_list[quiz_question_number_selector], maaori_list[quiz_question_number_selector]))
        print()
        time.sleep(0.75)
        #Let the user continue when ready
        print("Press <enter> to continue")
        exit_or_continue = input("►").lower()
        print()
        #If the user input the exit code
        if exit_or_continue == "exit":
          time.sleep(0.75)
          #Tell the user they entered the exit code
          print("exit code detected")
          print()
          time.sleep(0.75)
          #Tell the user they're returning to the main menu
          print("returning to main menu")
          time.sleep(0.75)
          #Returning to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)
      #If the user entered the incorrect translation of the Maaori word corresponding to the variable quiz_question_number_selector
      else:
        time.sleep(0.75)
        #Tell the user they have entered an incorrect translation, and tell them what the translation is.
        print("Sorry, '{}' is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_user_answer, maaori_list[quiz_question_number_selector], english_list[quiz_question_number_selector]))
        print()
        time.sleep(0.75)
        #Let the user continue when ready
        print("Press <enter> to continue")
        exit_or_continue = input("►").lower()
        print()
        #If the user entered the exit code
        if exit_or_continue == "exit":
          time.sleep(0.75)
          #Tell the user they entered the exit code
          print("exit code detected")
          print()
          time.sleep(0.75)
          #Tell the user they're returning to the main menu
          print("returning to main menu")
          time.sleep(0.75)
          #returning to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)
    #If the variable type_of_quiz_number_selector is equal to 1 run an english to Maaori quiz
    elif type_of_quiz_number_selector == 1:
      time.sleep(0.75)
      #Ask the user for the Maaori translation of the english word corresponding to the variable quiz_question_number_selector
      print("What is the Maaori translation of {}?".format(english_list[quiz_question_number_selector]))
      quiz_input_user_answer = input("►").lower()
      #If the user inputs the exit code
      if quiz_input_user_answer == "exit":
        time.sleep(0.75)
        print()
        #Tell the user they have entered the exit code
        print("Exit code selected")
        time.sleep(0.75)
        print()
        #Tell the user they are returning to the main menu
        print("Returning to main menu")
        time.sleep(0.75)
        #Return to main menu
        main_menu(maaori_list, english_list, main_menu_user_choice_input)
      #If the user input the correct translation of the english word corresponding to the variable quiz_question_number_selector
      elif quiz_input_user_answer == maaori_list[quiz_question_number_selector]:
        #Tell the user they entered the correct translation of the english word corresponding to the variable quiz_question_number_selector
        print("{} is the correct translation of {}! Yay!!".format(maaori_list[quiz_question_number_selector], english_list[quiz_question_number_selector]))
        time.sleep(0.75)
        print()
        #Let the user continue when they want to
        print("Press <enter> to continue")
        exit_or_continue = input("►").lower()
        #If the user input the exit code
        if exit_or_continue == "exit":
          time.sleep(0.75)
          #Tell the user they entered the exit code
          print("exit code detected")
          print()
          time.sleep(0.75)
          #Tell the user they're returning to the main menu
          print("returning to main menu")
          time.sleep(0.75)
          #Returning to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)
        time.sleep(0.75)
      #If the user input an incorrect translation of the Maaori word corresponding to the variable quiz_question_number_selector
      else:
        #Tell the user they input the wrong answer
        print("Sorry, '{}' is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_user_answer, english_list[quiz_question_number_selector], maaori_list[quiz_question_number_selector]))
        time.sleep(0.75)
        print()
        #Let the user continue when they want to
        print("Press <enter> to continue")
        exit_or_continue = input("►").lower()
        #If the user entered the exit code
        if exit_or_continue == "exit":
          time.sleep(0.75)
          #Tell the user they entered the exit code
          print("exit code detected")
          print()
          time.sleep(0.75)
          #Tell the user they are returning to the main menu
          print("returning to main menu")
          time.sleep(0.75)
          #Returning to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)
        time.sleep(0.75)
      
#creating the finite quiz function
def finite_quiz(input_rounds_to_play, maaori_list, english_list):
  #Setting the variable quiz_input_user_answer to blank
  quiz_input_user_answer = ""
  #Converting answer to an integer
  input_rounds_to_play = int(input_rounds_to_play)
  #Looping the program and setting up an exit code
  while quiz_input_user_answer != "exit":
    #looping the program for the desired amount of rounds
    for item in range(0, input_rounds_to_play):
      #Clear the screen
      for item in range(1, 100):
        print()
      #Selecting the number for the question
      quiz_question_number_selector = random.randint(0, 49)
      #Selecting the number for the type of quiz
      type_of_quiz_number_selector = random.randint(0, 1)
      #If the number for the type of quiz is 0, do an English to Maaori quiz
      if type_of_quiz_number_selector == 0:
        time.sleep(0.75)
        #Asking the user for the English translation of the Maaori word corresponding to the quiz number question
        print("What is the english translation of {}? ".format(maaori_list[quiz_question_number_selector]))
        quiz_input_user_answer = input("►").lower()
        print()
        #If the user input the exit code, return to main menu
        if quiz_input_user_answer == 'exit':
          time.sleep(0.75)
          #Tell the user they entered the exit code
          print("Exit code detected")
          time.sleep(0.75)
          print()
          #Tell the user they're returning to the main menu
          print("returning to main menu")
          time.sleep(0.75)
          #Returning to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)
        #Checking if the user input the correct translation
        elif quiz_input_user_answer == english_list[quiz_question_number_selector]:
          time.sleep(0.75)
          #If the user got the question correct, tell them.
          print("{} is the correct translation of {}! Yay!!".format(english_list[quiz_question_number_selector], maaori_list[quiz_question_number_selector]))
          print()
        #If the user input the wrong answer
        else:
          time.sleep(0.75)
          #Inform the user that they were wrong
          print("Sorry, '{}' is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_user_answer, maaori_list[quiz_question_number_selector], english_list[quiz_question_number_selector]))
          print()
        #If the type of quiz number is 1, do a Maaori to English quiz
      elif type_of_quiz_number_selector == 1:
        time.sleep(0.75)
        #Ask the user for the Maaaori translation of the english word corresponding to the variable quiz_question_number_selector
        print("What is the Maaori Translation of {}? ".format(english_list[quiz_question_number_selector]))
        quiz_input_user_answer = input("►").lower()
        print()
        #If the user enters the exit code
        if quiz_input_user_answer == 'exit':
          time.sleep(0.75)
          #tell the user they entered the exit code
          print("Exit code detected")
          time.sleep(0.75)
          print()
          #tell the user they are returning to the main menu
          print("Returning to main menu")
          time.sleep(0.75)
          #Returning to the main menu
          main_menu(maaori_list, english_list, main_menu_user_choice_input)
        #If the user enters the correct translation of the english word corresponding to the variable quiz_question_number_selector
        if quiz_input_user_answer == maaori_list[quiz_question_number_selector]:
          time.sleep(0.75)
          #Inform the user they have entered the correct answer
          print("{} is the correct translation of {}! Yay!!".format(maaori_list[quiz_question_number_selector], english_list[quiz_question_number_selector]))
          print()
        #If the user input the wrong translation of the Maaori word 
        else:
          time.sleep(0.75)
          #Tell the user they entered the incorrect translation
          print("Sorry, '{}' is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_input_user_answer, english_list[quiz_question_number_selector], maaori_list[quiz_question_number_selector]))
          print()
      #Decrease the number of rounds left
      input_rounds_to_play -= 1
      #Tell the user how many rounds they have left
      time.sleep(0.75)
      #Tell the user how many rounds they have left
      print("{} Rounds Left".format(input_rounds_to_play))
      print()
      time.sleep(0.75)
      #Let the user continue when ready
      print("Press <enter> to continue")
      exit_or_continue = input("►").lower()
      print()
      #If the user entered the exit code
      if exit_or_continue == "exit":
        time.sleep(0.75)
        #tell the user they entered the exit code
        print("exit code detected")
        print()
        time.sleep(0.75)
        #Tell the user they're returning to the main menu
        print("returning to main menu")
        time.sleep(0.75)
        #returning to the main menu
        main_menu(maaori_list, english_list, main_menu_user_choice_input)
    #When the number of rounds run out, inform the user they are returning to the main menu
    time.sleep(0.75)
    #Tell the user they finished the quiz
    print("Quiz finished. Returning to main menu")
    time.sleep(0.75)
    #Returning to the main menu
    main_menu(maaori_list, english_list, main_menu_user_choice_input)
      
#Creating the variable main_menu_user_choice_input
main_menu_user_choice_input = ""
#Starting the code
main_menu(maaori_list, english_list, main_menu_user_choice_input)

#► alt + 16
