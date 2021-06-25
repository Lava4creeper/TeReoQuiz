import random

Maaori_List = ["Aroha", "Awa", "Haka", "Hangi", "Hapu", "Hikoi", "Hui", "Iti", "Iwi", "Kai", "Karakia", "Kaumatua", "Kauri", "Kiwi", "Koha", "Kohanga reo", "Mahi", "Mana", "Manuhiri", "Maori", "Marae", "Maunga", "Moa", "Moana", "Moto", "Nui", "Pa", "Pakeha", "Pounamu", "Puku", "Rangatira", "Taihoa", "Tama", "Tamahine", "Tamariki", "Tane", "Tangi", "Taonga", "Tapu", "Te Reo Maori", "Tipuna", "Tuatara", "Wahine", "Wai", "Waiata", "Waka", "Whaikorero", "Whakapapa", "Whanau", "Whenua"]

English_List = ["Love", "River", "Dance", "Feast", "Clan", "Walk", "Gathering", "Small", "Tribe", "Food", "Prayer", "Elder", "Native Tree", "Native Bird", "Gift", "Maaori Preschool", "Work", "Reputation", "Guests", "The people of New Zealand", "Meeting House", "Mountain", "Flightless Bird", "Sea", "Island", "Large", "Hill Fort", "European", "Greenstone", "Stomach", "Chief", "Wait", "Young Man", "Daughter", "Children", "Man", "Funeral", "Precious", "Sacred", "The Maaori Language", "Ancestor", "Lizard", "Woman", "Water", "Song", "Canoe", "Speechmaking", "Genealogy", "Family", "Land"]
def instructions(list_or_quiz):
  print("*--------------------*")
  print(" Instructions go here ")
  print("*--------------------*")
  print()
  print("Returning to main UI")
  print()
  Main_UI(list_or_quiz)

def Main_UI(list_or_quiz):
  while list_or_quiz != "xxx":
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
      Main_Quiz()
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
    Main_UI(list_or_quiz)
    
def Main_Quiz():
  User_Answer = ""
  number_of_games = ""
  while number_of_games != "xxx":
    number_of_games = input("How many games would you like to play? Please enter a whole number or press <Enter> to enter infinite mode: ").lower()
    try:
      if int(number_of_games) > 0:
        print("{} Games selected".format(number_of_games))
      else:
        print("Please enter a number greater than 0 or press <enter>")
    except ValueError:
      if number_of_games == "":
       print("Infinite mode selected")
    for item in range(1, number_of_games):
      quiz_number = random.randint(1, 50)
      User_Answer = input('What is the Maaori translation of "{}"?: '.format(Maaori_List(quiz_number)))
      if User_Answer == English_List(quiz_number):
        print('"{}" is correct! Next round.')
      else:
        print("Sorry, that's incorrect. The correct answer was '{}'. Let's move onto the next question!")
    


list_or_quiz = ""
Main_UI(list_or_quiz)