import os
import time
import words_parser
import words_tools

word_to_guess = words_parser.return_random_word()
lives = 5
has_guessed = False

while True:
  try:
    player_letter = input("Enter your letter: ")
    has_guessed = words_tools.hidden_word(word_to_guess, player_letter)

    if not has_guessed:
      if lives > 1:
        lives -= 1
      else:
        print("You loose!\n\nYour word was: " + word_to_guess)

        again = input("Wanna try again? (y/n): ")

        if again == 'y':
          os.system("python3 main.py")
          time.sleep(0.2)
          exit()
        else:
          exit()

    print("Lives: " + str(lives))

  except:
    print()
