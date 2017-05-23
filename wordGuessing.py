import os
import sys

class Game():

    def __init__(self):
        self.filename = '\dictionary.txt';
        self.dict, self.guessedLetters, self.matchingDict = [], [], [];
        self.guessedLetter, self.secretWord = "", "";
        self.remainingGuesses, self.largestListId, self.wordLength = 0, 0, 0;
        self.showWordList, self.winner = False, False;
        self.init = True;
        self.chars = set('abcdefghijklmnopqrstuvwxyz');

    def populate_list(self):
        for n in range(30):
            self.dict.append([]);
        for i in range(100):
            self.matchingDict.append([]);

    def populate_secret_word(self):
        if self.init:
            for n in range(int(self.wordLength)):
                self.secretWord += "_ ";
        else:
            temp = self.secretWord;
            self.secretWord = "";
            for n in range(int(self.wordLength)):
                if self.dict[int(self.largestListId)][0][n] != "_" :
                    self.secretWord += self.dict[int(self.largestListId)][0][n] + " ";
                else:
                    self.secretWord += "_ ";
            for n in range(int(len(temp))):
                if temp[n] != " ":
                    if temp[n] != "_":
                        self.secretWord = self.secretWord[:n] + temp[n] + self.secretWord[n+1:];

    def load(self):
        try:
            if self.filename[1] not in self.chars:
                print("Invalid file name");
            file = open(os.getcwd() + self.filename, 'r');
            for value in file:
                word = value.rstrip();
                self.dict[len(word)].append(word);
        except FileNotFoundError:
            print("File not found");

    def get_valid_length(self):
        while True:
            wordLength = input("Enter a word length: ");
            try:
                if self.dict[int(wordLength)]:
                    return wordLength;
                else:
                    print("Invalid word length, please try again.");
            except:
                print("Invalid word length, please try again.");

    def get_valid_guesses(self):
        while True:
            guesses = input("Enter number of guesses (1 to ∞): ");
            try:
                if int(guesses) >= 1:
                    return guesses;
                else:
                    print("Invalid number of guesses, please try again.");
            except:
                print("Invalid number of guesses, please try again.");

    def get_valid_showlist(self):
        while True:
            response = input("Show word list? (Y/N)").lower();
            if response == "y":
                return True
            elif response == "n":
                return False
            else:
                print("Invalid response, please type either 'y' or 'n'.");

    def print_stats(self):
        print("Remaining Guesses: %s - Guessed Letters: %s - Secret Word: %s" % (self.remainingGuesses, self.guessedLetters, self.secretWord));
        if self.showWordList:
            if self.init:
                print(self.dict[int(self.wordLength)]);
            else:
                print(self.dict[int(self.largestListId)][1:]);

    def get_valid_guess(self):
        while True:
            guessLetter = input("Guess Letter: ");
            if guessLetter in self.chars and guessLetter not in self.guessedLetters:
                return guessLetter;
            else:
                print("Invalid guess, try again.");

    def clear_list(self):
        for index in range(len(self.matchingDict)):
            self.matchingDict[index] = [];

    def new_game(self):
        while True:
            newGame = input("Would you like to play again (Y/N)");
            if newGame.lower() == "y":
                return True;
            elif newGame.lower() == "n":
                return False;
            else:
                print("Invalid response, please type either 'y' or 'n'.");

    def split_list(self, letter):
            self.clear_list();
            if self.init:
                for wordId in range(len(self.dict[int(self.wordLength)])):
                    wordMarker = "";
                    for letters in self.dict[int(self.wordLength)][wordId]:
                        if letters == letter:
                            wordMarker += letter;
                        else:
                            wordMarker += "_";
                    for listId in range(len(self.matchingDict)):
                        if not self.matchingDict[listId]:
                            self.matchingDict[listId].append(wordMarker);
                            self.matchingDict[listId].append(self.dict[int(self.wordLength)][wordId]);
                            break;
                        else:
                            if self.matchingDict[listId][0] == wordMarker:
                                self.matchingDict[listId].append(self.dict[int(self.wordLength)][wordId]);
                                break;
                            else:
                                continue;
                self.init = False;
            else:
                for wordId in range(1, len(self.dict[int(self.largestListId)])):
                    wordMarker = "";
                    for letters in self.dict[int(self.largestListId)][wordId]:
                        if letters == letter:
                            wordMarker += letter;
                        else:
                            wordMarker += "_";
                    for listId in range(len(self.matchingDict)):
                        if not self.matchingDict[listId]:
                            self.matchingDict[listId].append(wordMarker);
                            self.matchingDict[listId].append(self.dict[int(self.largestListId)][wordId]);
                            break;
                        else:
                            if self.matchingDict[listId][0] == wordMarker:
                                self.matchingDict[listId].append(self.dict[int(self.largestListId)][wordId]);
                                break;
                            else:
                                continue;
            self.dict = list(self.matchingDict);

    def calc_big_list(self):
        listNum = 0;
        for num in range(len(self.dict)):
            if len(self.dict[num]) > len(self.dict[listNum]):
                listNum = num;
        return listNum;

while True:
    game = Game();
    game.populate_list();
    game.load();
    game.wordLength = game.get_valid_length();
    game.remainingGuesses = game.get_valid_guesses();
    game.showWordList = game.get_valid_showlist();
    while int(game.remainingGuesses) > 0:
        game.populate_secret_word();
        game.print_stats()
        if "_" not in game.secretWord:
            game.winner = True;
            break;
        game.guessedLetter = game.get_valid_guess();
        game.split_list(game.guessedLetter);
        game.largestListId = game.calc_big_list();
        game.remainingGuesses = int(game.remainingGuesses) - 1;
        game.guessedLetters.append(game.guessedLetter);
    if game.winner:
        print("Congratulations, You Win!");
    else:
        print("You ran out of guesses!");
    if(game.new_game()):
        continue;
    else:
        sys.exit();
