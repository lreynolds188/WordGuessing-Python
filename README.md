# WordGuessingGame

In this part of the assignment, you will build a program that bends the rules to trounce its human opponent time and time again. In case you aren't familiar with the Word Guessing game, the rules are as follows:
1. One player chooses a secret word, then writes out a number of dashes equal to the word length.
2. The other player begins guessing letters. Whenever they guess a letter contained in the hidden word, the first player reveals each instance of that letter in the word. Otherwise, the guess is wrong.
3. The game ends either when all the letters in the word have been revealed or when the guesser has run out of guesses.
Fundamental to the game is the fact the first player accurately represents the word they have chosen. That way, when the other players guess letters, they can reveal whether that letter is in the word. But what happens if the player doesn't do this? Suppose that you are playing Word Guessing and it's your turn to choose a word, which we'll assume is of length four. Rather than committing to a secret word, you instead compile a list of every four-letter word in the English language. For simplicity, let's assume that English only has a few four-letter words, all of which are reprinted here:
ALLY BETA COOL DEAL ELSE FLEW GOOD HOPE IBEX
Now, suppose that your opponent guesses the letter 'E.' You now need to tell your opponent which letters in the word you've “picked” are E's. Of course, you haven't picked a word, and so you have multiple options about where you reveal the E's. Here's the above word list, with E's highlighted in each word:
ALLY BETA COOL DEAL ELSE FLEW GOOD HOPE IBEX
Every word in the word list falls into one of five “word categories:”
 ----, containing the word ALLY, COOL, and GOOD.
 -E--, containing BETA and DEAL.
 --E-, containing FLEW and IBEX.
 E--E, containing ELSE.
 ---E, containing HOPE.
Since the letters you reveal have to correspond to some word in the word list, you can choose to reveal any one of the above five categories. There are many ways to pick which category to reveal – perhaps you want to steer your opponent toward a smaller category with more obscure words, or toward a larger category in the hopes of keeping your options open. If we adopt the larger category approach and always choose the largest of the remaining word categories you would pick the category ----. This reduces your word list down to ALLY COOL GOOD and since you didn't reveal any letters, you would tell your opponent that their guess was wrong.
