
#TimeForTeReo v1.0 was created by Thomas Gardner on the 09/07/2021
import random

#Creating the list of Maaori Words
Maaori_List = ["Aroha", "Awa", "Haka", "Hangi", "Hapu", "Hikoi", "Hui", "Iti", "Iwi", "Kai", "Karakia", "Kaumatua", "Kauri", "Kiwi", "Koha", "Kohanga reo", "Mahi", "Mana", "Manuhiri", "Maori", "Marae", "Maunga", "Moa", "Moana", "Moto", "Nui", "Pa", "Pakeha", "Pounamu", "Puku", "Rangatira", "Taihoa", "Tama", "Tamahine", "Tamariki", "Tane", "Tangi", "Taonga", "Tapu", "Te Reo Maori", "Tipuna", "Tuatara", "Wahine", "Wai", "Waiata", "Waka", "Whaikorero", "Whakapapa", "Whanau", "Whenua", "i broke it lol"]

#Creating the list of English Words
English_List = ["love", "river", "dance", "feast", "clan", "walk", "gathering", "small", "tribe", "food", "prayer", "elder", "native tree", "native bird", "gift", "maaori preschool", "work", "reputation", "guests", "the people of new zealand", "meeting house", "mountain", "flightless bird", "sea", "island", "large", "hill fort", "european", "greenstone", "stomach", "chief", "wait", "young man", "daughter", "children", "man", "funeral", "precious", "sacred", "the maaori language", "ancestor", "lizard", "woman", "water", "song", "canoe", "speechmaking", "genealogy", "family", "land"]

#Defining Instructions
def instructions(list_or_quiz):
  #Print Instructions
  print("*--------------------*")
  print(" Instructions go here ")
  print("*--------------------*")
  print()
  print("Returning to main UI")
  print()
  #Returning to main UI
  Main_UI(Maaori_List, English_List, list_or_quiz)

#defining Main UI
def Main_UI(Maaori_List, English_List, list_or_quiz):
  #looping the main UI
  while list_or_quiz != "xxx":
    #Giving the user their options
    print("Would you like to view the instructions, view the list of vocabulary words or begin the quiz?")
    print()
    
    list_or_quiz = input("Please enter 'Instructions', 'List' or 'Quiz': ").lower()
    print()
    if list_or_quiz == "list":
      print("Showing list of Vocabulary")
      print()
      vocab_list(list_or_quiz)
    elif list_or_quiz == "quiz":
      print("Beginning quiz")
      print()
      Quiz_Start(Maaori_List, English_List)
    elif list_or_quiz == "instructions":
      print("Showing Instructions")
      print()
      instructions(list_or_quiz)
    else:
      print("'{}' is not a valid input. Please input 'Instructions', 'List' or 'Quiz'.".format(list_or_quiz))
      print()

def vocab_list(list_or_quiz):
  continue_with_list = ""
  while continue_with_list != 'xxx':
    print("You have selected the list of vocab words. They will be displayed 10 at a time, press <enter> to continue or type 'xxx' to exit")
    list_number = 0
    for item in range(0, 5):
      for item in range(0, 10):
        print("{}. Maaori Word: {}, English Translation: {}".format(list_number + 1, Maaori_List[list_number], English_List[list_number]))
        list_number += 1
      input("Press <Enter> to continue")
      print()
    print("Returning to main UI")
    print()
    Main_UI(Maaori_List, English_List, list_or_quiz)
    
    
def Quiz_Start(Maaori_List, English_List):
  User_answer = ""
  while User_answer != "exit":
    User_answer = input("How many games would you like to play? please enter a whole number greater than 0 or <enter> for infinite mode: ").lower()
    print()
    if User_answer == "":
      print("Infinite mode selected. input 'Exit' to leave")
      print()
      infinite_quiz()
    else:
      try:
        if int(User_answer) > 0:
          print ("{} Game(s) Selected".format(User_answer))          
          print()
          finite_quiz(User_answer, Maaori_List, English_List)
        else:
          print("Please enter a whole number greater than 0 or press <enter> for infinite mode")
          print()
      except TypeError:
        print("Please enter a whole number greater than 0 or press <enter> for infinite mode")
        print()
      except ValueError:
        print("Please enter a whole number greater than 0 or press <enter> for infinite mode")
        print()

def infinite_quiz():
  quiz_user_answer = ""
  while quiz_user_answer != "exit":
      quiz_number_selector = random.randint(0, 49)
      quiz_user_answer = input("What is the english translation of {}? ".format(Maaori_List[quiz_number_selector])).lower()
      if quiz_user_answer == "exit":
        print()
        print("Exit code selected")
        print()
        print("Returning to main UI")
        print()
        Main_UI(Maaori_List, English_List, list_or_quiz)
      elif quiz_user_answer == English_List[quiz_number_selector]:
        print("{} is the correct translation of {}! Let's do another question!".format(English_List[quiz_number_selector], Maaori_List[quiz_number_selector]))
      else:
        print("Sorry, {} is incorrect. The translation of {} is {}. Let's try a different question!".format(quiz_user_answer, Maaori_List[quiz_number_selector], English_List[quiz_number_selector]))

def finite_quiz(User_answer, Maaori_List, English_List):
  quiz_user_answer = ""
  User_answer = int(User_answer)
  while quiz_user_answer != "exit":
    for item in range(0, User_answer):
      quiz_number_selector = random.randint(0, 49)
      quiz_user_answer = input("What is the english translation of {}? ".format(Maaori_List[quiz_number_selector])).lower()
      print()
      if quiz_user_answer == English_List[quiz_number_selector]:
        print("{} is the correct translation of {}! Let's do another question!".format(English_List[quiz_number_selector], Maaori_List[quiz_number_selector]))
        print()
      else:
        print("Sorry, {} is incorrect. The translation of {} is {}. Let's forget that happened.".format(quiz_user_answer, Maaori_List[quiz_number_selector], English_List[quiz_number_selector]))
        print()
      User_answer -= 1
      print("{} Rounds Left".format(User_answer))
      print()
    print("Quiz finished. Returning to main UI")
    Main_UI(Maaori_List, English_List, list_or_quiz)
      


list_or_quiz = ""
Main_UI(Maaori_List, English_List, list_or_quiz)