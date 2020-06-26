import random


class Hangman:

    def __init__(self, no_of_turns):
        print(*'HANGMAN')
        self.word_list = ['python', 'java', 'kotlin', 'javascript']
        self.no_of_turns = no_of_turns

    def select_random_word(self):
        return random.choice(self.word_list)

    def mask_word(self, word, character):
        return len(word) * character

    def display(self, word):
        print(word)

    def play(self, no_of_turns, selected_word):
        mask_word = self.mask_word(selected_word, '-')
        character_set = set(selected_word)
        self.display("\n" + mask_word)
        mask_word_list = list(mask_word)
        turn = 0
        while no_of_turns > 0:
            guessed_character = input('Input a letter:')
            if guessed_character not in character_set:
                self.display('No such letter in the word')
                no_of_turns -= 1
            elif guessed_character in mask_word_list:
                self.display('No improvements')
                no_of_turns -= 1
            else:
                index = -1
                for count in range(selected_word.count(guessed_character)):
                    index = selected_word.find(guessed_character, index + 1)
                    mask_word_list[index] = guessed_character
            # to display
            if no_of_turns != 0:
                self.display("\n" + "".join(mask_word_list))
            if "".join(mask_word_list) == selected_word:
                self.display('You guessed the word!\nYou survived!')
                break
        else:
            self.display('You are hanged!')

    def run(self):
        selected_word = self.select_random_word()
        self.play(self.no_of_turns, selected_word)


hangman = Hangman(8)
hangman.run()
