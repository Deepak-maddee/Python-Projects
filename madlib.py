#madlibs using string concatenation

story = "The [adj1] [noun1] was having a very beautiful day. He decided to go for a walk in the [adj2] [place]. As he walked, he saw a [adj3] [animal] wearing a [adj4] [article of clothing]. The [animal] was trying to [verb] a [adj5] [noun2] out of a [adj6] tree. The [noun2] couldn't believe his [body part]!  He quickly [verb ending in -ed] to help the [animal]. Together, they [verb ending in -ed] the [noun2] out of the tree and the [animal] was very [adj7] to the [noun2] for his help. The [noun1] was so happy about his good deed that he decided to go for a [adj8] [activity] to celebrate.  He had a very good time, and went to sleep that night feeling very [adj9]"

play = input("Wanna play a Madlibs game: (Y/N)").upper()
if play == "Y":
    print(f"Alright. Here's the story. Fill in the story with your own words.\n {story}")

    print()
    adj1 = input("Enter the adjective 1: ")
    print('--------------------')
    noun1 = input("Enter the noun1: ")
    print('--------------------')
    adj2 = input("Enter the adjective 2: ")
    print('--------------------')
    place = input("Enter the place: ")
    print('--------------------')
    adj3 = input("Enter the adjective 3: ")
    print('--------------------')
    animal = input("Enter the animal: ")
    print('--------------------')
    adj4 = input("Enter the adjective 4: ")
    print('--------------------')
    article_of_clothing = input("Enter the article of clothing: ")
    print('--------------------')
    verb = input("Enter the verb: ")
    print('--------------------')
    adj5 = input("Enter the adjective 5: ")
    print('--------------------')
    noun2 = input("enter the noun 2: ")
    print('--------------------')
    adj6 = input("Enter the adjective 6: ")
    print('--------------------')
    body_part = input("enter the body part: ")
    print('--------------------')
    verb_ending_in_ed = input("Enter the verb ending in -ed: ")
    print('--------------------')
    adj7 = input("Enter the adjective 7: ")
    print('--------------------')
    adj8 = input("Enter the adjective 8: ")
    print('--------------------')
    activity = input("Enter the activity: ")
    print('--------------------')
    adj9 = input("Enter the adjective 9: ")
    print('--------------------')

    print("You have completed to fill in the story with your own words. Now hear it out.")
    print('--------------------')
    print("THE STORY - BY USER")

    print(f"The {adj1} {noun1} was having a very beautiful day. He decided to go for a walk in the {adj2} {place}. As he walked, he saw a {adj3} {animal} wearing a {adj4} {article_of_clothing}. The {animal} was trying to {verb} a {adj5} {noun2} out of a {adj6} tree. The {noun2} couldn't believe his {body_part}!  He quickly {verb_ending_in_ed} to help the {animal}. Together, they {verb_ending_in_ed} the {noun2} out of the tree and the {animal} was very {adj7} to the {noun2} for his help. The {noun1} was so happy about his good deed that he decided to go for a {adj8} {activity} to celebrate.  He had a very good time, and went to sleep that night feeling very {adj9}.")

else:
    print("Play when you wish!")
