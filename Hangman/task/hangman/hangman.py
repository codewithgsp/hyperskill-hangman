# Write your code here
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
        for i in range(no_of_turns):
            guessed_character = input('Input a letter:')
            if guessed_character not in character_set:
                self.display('No such letter in the word')
            else:
                index = -1
                for count in range(selected_word.count(guessed_character)):
                    index = selected_word.find(guessed_character, index + 1)
                    mask_word_list[index] = guessed_character
            self.display("\n" + "".join(mask_word_list))

    def run(self):
        selected_word = self.select_random_word()
        self.play(self.no_of_turns, selected_word)
        self.display("\nThanks for playing!\nWe'll see how well you did in the next stage")


hangman = Hangman(8)
hangman.run()
