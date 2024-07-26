#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you :https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:/Users/snatl/Documents/Coding/100 Days of Python/Mail Merger/"
              "Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.read().split('\n')

with open("C:/Users/snatl/Documents/Coding/100 Days of Python/Mail Merger/"
          "Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_file:
    starting_letter = starting_file.read()

    for name in names:
        new_letter = starting_letter.replace("[name]", name)

        with open(f"C:/Users/snatl/Documents/Coding/100 Days of Python/Mail Merger/"
                  "Mail Merge Project Start/Output/ReadyToSend/" + name + ".txt", mode="w") as new_file:
            new_file.write(new_letterdf)