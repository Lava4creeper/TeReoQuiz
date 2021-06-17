Maaori_List = ["Aroha", "Awa", "Haka", "Hangi", "Hapu", "Hikoi", "Hui", "Iti", "Iwi", "Kai", "Karakia", "Kaumatua", "Kauri", "Kiwi", "Koha", "Kohanga reo", "Mahi", "Mana", "Manuhiri", "Maori", "Marae", "Maunga", "Moa", "Moana", "Moto", "Nui", "Pa", "Pakeha", "Pounamu", "Puku", "Rangatira", "Taihoa", "Tama", "Tamahine", "Tamariki", "Tane", "Tangi", "Taonga", "Tapu", "Te Reo Maori", "Tipuna", "Tuatara", "Wahine", "Wai", "Waiata", "Waka", "Whaikorero", "Whakapapa", "Whanau", "Whenua"]

def instructions():
  print("*--------------------*")
  print(" Instructions go here ")
  print("*--------------------*")
  print("")
  print("Beginning Quiz")
  print()
  Main_UI()

def Main_UI(list_or_quiz):
  while list_or_quiz != "xxx":
    list_or_quiz = input("Would you like to view the instructions, view the list of vocabulary words or begin the quiz? Please enter 'Instructions', 'List' or 'Quiz'").lower()
    if list_or_quiz == "list":
      print("Showing list of Vocabulary")
      #Go to list
    elif list_or_quiz == "quiz":
      print("Beginning quiz")
      #Go to quiz
    elif list_or_quiz == "instructions":
      print("Showing Instructions")
      instructions()
    else:
      print("Invalid")
list_or_quiz = ""
Main_UI(list_or_quiz)