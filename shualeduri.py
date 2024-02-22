import random    

# ვქმნით  ჩამოხრჩობანის კლასს
class Hangman:
    def __init__(self):
        self.word_list = self.load_word_list()
        self.secret_word = self.choose_word()
        self.guesses_left = 6
        self.guessed_letters = []

    def load_word_list(self):
# try error ფუნქციით ვამოწემებთ არსებობს თარა ასეთი ფაილი ამ სახელით, ხოლო იმ შემთვევაში თუ არარსებობს, გვიწერს რო არარსებობსა და ამატებს ამ ფაილს მითითებული სიტყვებით,
#  რომლის ჩანაცვლებაც შეგვიძლია.
        try:
            with open("word_list.txt", "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Word list file not found. Creating a new one...")
            with open("word_list.txt", "w") as file:
                default_words = ["hangman", "python", "game", "computer", "programming"]
                file.write("\n".join(default_words))
            return default_words

# ეს ფუნქცია აბრუნებს რანდომ პრინციპით ამორჩულ ერთ სიტყვას ზემოთხსენებული ფაილიდან.
    def choose_word(self):
        return random.choice(self.word_list)

# ეს ფუნქცია გამოიტანს ასოების გამოსაცნობ დეფისებს სადაც შე მდეგ გამოცნობილი ასოები ჩაჯდება.
    def display_word(self):
        displayed = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                displayed += letter
            else:
                displayed += "_"
        return displayed


    def guess(self, letter):
# თუ ასო არარის სიტყვის შემადგენლობაში, გვაკლდება 1 გამოცნობა
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter not in self.secret_word:
                self.guesses_left -= 1
 # სიტყვის გამოცნობის შემთვევაში ამ სიტყვას ფაილიდან ამოვშლით, რათა არ განმეორდეს მეორეჯერ და იგივე სიტყვის გამოცნობა არმოგვიწიოს. 
        if self.secret_word == self.display_word():
            self.word_list.remove(self.secret_word)
            with open("word_list.txt", "w") as file:
                file.write("\n".join(self.word_list))
        #თუ იგივე ასოს შევიყვანთ დაგვიწერს რომ ეს ასო უკვე შევიყვანეთ, მაგრამ ცდად არ ჩაითვლება. 
        else:
            print("You already guessed that letter.")
# ამ ფუნქციით კი შევძლებთ ნებისმიერი სიტყვა ჩავწეროთ ფაილში, პროგრამა კი ამ სიტყვას გამოიყენებს და მოგვიწევს მისი გამოცნობაც 
    def add_word(self, word):
        self.word_list.append(word)
        with open("word_list.txt", "a") as file:
            file.write("\n" + word)

    def is_win(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)
# წაგების შემთხვევაში როცა ცდები აღარ გვექნება.
    def is_loss(self):
        return self.guesses_left == 0

# ვიწყებთ თამაშის გაშებას და გამოგვაქ ტერმინალში ვიზუალურად
    def play(self):
        print("Welcome to Hangman!")
        while not self.is_win() and not self.is_loss():
            print("\nWord:", self.display_word())
            print("Guesses left:", self.guesses_left)
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                self.guess(guess)
            else:
                print("Please enter a valid single letter.")
        if self.is_win():
            print("\nCongratulations! You guessed the word:", self.secret_word)
        else:
            print("\nSorry, you ran out of guesses. The word was:", self.secret_word)

def main():
    game = Hangman()
    game.play()

if __name__ == "__main__":
    main()
