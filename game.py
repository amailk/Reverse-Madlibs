
# Taken from http://harrypotter.wikia.com
easy = '''Harry James Potter (b. 31 July, 1980) was a half-blood wizard, the only child and son of James and Lily Potter, 
and one of the most famous wizards of modern times. In what proved to be a vain attempt to circumvent a prophecy that stated 
a boy born at the end of July of 1980 could be able to defeat him, Lord Voldemort attempted to murder him when he was only a 
year and three months old. Voldemort murdered Harry's parents as they tried to protect him shortly before attacking Harry himself. 
This early, unsuccessful attempt to vanquish Harry led to Voldemort's first downfall, marking the end of the First Wizarding War 
and to Harry henceforth being known as " The Boy Who Lived "'''

medium = ''' The Patronus Charm (Expecto Patronum) is the most famous and one of the most powerful defensive charms known to wizardkind.
It is an immensely complicated and extremely difficult spell that evokes a partially-tangible positive energy force known as a Patronus 
or spirit guardian.It is the primary protection against Dementors and Lethifolds, to which there is no other protection. During a Quidditch 
match against Ravenclaw in 1994 Harry cast his very first corporal Patronus and again in June when he along with Hermione Granger and Sirius 
Black were being attacked by over a hundred Dementors , he cast a corporal Patronus powerful enough to drive them all away.

Harry: "What does a Patronus look like?"
Lupin: "Each one is unique to the wizard who conjures it."'''

hard = '''An invisibility cloak is a magical garment which renders whatever it covers unseeable. They may be made from hair of Demiguise, 
a magical creature that possesses the power to become invisible . This property is used to make the wearer of the cloak invisible . However, 
as Xenophilius Lovegood tells Harry , Ron , and Hermione , such a cloak will gradually lose its effectiveness as the hair becomes more and more opaque. 
The cloak can also be formed from an ordinary travelling cloak, enchanted with an exceptionally strong disillusionment charm or a bedazzling hex. 
The cloak is also mentioned by being one of the entities in the Deathly Hallows. In the story the third brother asked for a way to hide from Death 
so Death himself gave the brother the cloak of invisibility . There are ways of making one's self invisible by using magic other than invisibility 
cloaks. An example is the Disillusionment Charm. Harry Potter used his father 's cloak many times throughout his years at Hogwarts. He received it from 
Albus Dumbledore anonymously in 1991 as a Christmas present. Dumbledore once remarked to Harry that he didn't need a cloak to become invisible.'''

paragraphs = [easy, medium, hard]

blanks = [["James", "Voldemort", "Lived", "July"], # blanks for easy
          ["Patronus","Quidditch", "Harry", "Hermione" , "Dementors"], # blanks for medium
          ["invisibility", "invisible", "Deathly", "Disillusionment", "father", "Christmas", "Dumbledore"]] # blanks for hard

# Take the steps to play the game, prompt to advance to the next level when a level is completed
def main():
    print "~~~ Welcome to Ama's Harry Potter Reverse-Mad-Libs ~~~"

    level = choose_level()

    while level < 3:
        play_game(level)
        
        # If we're at easy or medium, prompt to advance
        if level < 2: 
            proceed = raw_input("Do you want to proceed to the next level?(Y/N)")
            if proceed == "Y":
                level += 1
            else:
                break
        else:
            break

    print "~~~ Thank you for playing ~~~"

# play the game for the given level
def play_game(level):
    blank = 0

    # while not all blanks are filled, keep asking to guess the blanks until the correct word is guessed
    while blank < len(blanks[level]):
        print process_paragraph(level, blank)
        
        question = "\nWhat should go in blank number " + str(blank+1) + "?"
        answer = raw_input(question).lower()

        correct_answer = blanks[level][blank].lower()
        if correct_answer == answer:
            print "You got it!"
            blank += 1
        else:
            print "Try again!"

    print paragraphs[level]
    print "\n~~~ Congratulations, you win! ~~~" 

# Process the paragraph for the given level
# Replace the words in blanks for the level, from the given blank
def process_paragraph(level, blank):

    paragraph = paragraphs[level]

    # replace all the blanks from current blank to the last one
    while blank < len(blanks[level]):
        word_to_replace = blanks[level][blank]
        list_of_words = paragraph.split(" ")
        index = 0
        # Replace the word_to_replace with ___number___
        while index < len(list_of_words):
            if list_of_words[index] == word_to_replace:
                list_of_words[index] = "___" + str(blank+1) + "___"
            index += 1

        blank += 1
        paragraph = " ".join(list_of_words)

    return paragraph

# Prompt the user to choose a level until they choose a valid one
def choose_level():

    level = raw_input("Enter your difficulty level (easy/medium/hard): ")

    if level == "easy":
        print "Easy level selected"
        return 0
    elif level == "medium":
        print "Medium level selected"
        return 1
    elif level == "hard":
        print "Hard level selected"
        return 2
    else:
        print "Invalid level selected"
        return choose_level() # if the level is invalid, choose a level again, and return that value

main()