import os
import time
known_letters = []
used_letters = []

def hidden_word(word, letter):
  has_guessed = True
  used_letters.append(letter)

  if (letter in word):
    known_letters.append(letter)
  else:
    has_guessed = False

  word_to_show = ""
  for i in range(len(word)):
    if word[i] in known_letters:
      word_to_show = word_to_show + word[i]
    else:
      word_to_show = word_to_show + "*"

  if not '*' in word_to_show:
    print('You win!')

    again = input("Wanna try again? (y/n): ")

    if again == 'y':
      os.system("python3 main.py")
      time.sleep(0.2)
      exit()
    else:
      exit()


  print('\n\n' + word_to_show + '\n\n')
  print('Used letters: ' + str(used_letters))
  return (has_guessed)
