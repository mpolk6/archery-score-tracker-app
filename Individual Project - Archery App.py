# Individual Project (BUS472) - Archery Scoring and Tracking App

import csv  # allows me to save the inputted data to a file (can open in excel)
import os   # allows me to check if a file exists

# Source - Classwork
# importing everything from the library called tkinter
from tkinter import *

# Source - External (Geeks for Geeks)
# importing the library needed to add the image I want to the background
from PIL import Image, ImageTk

# Source - Classwork
# these lines are basically formatting the window
root = Tk()    # creates the main application window
root.title("Archery Score & Tracking App")  #title of the window
root.geometry("550x600")  # size of the window


# Source - External (Geeks for Geeks)
# these lines of code are for the background of the app (the image)
background_image = Image.open("archeryimg.jpg")  # gets the image that is saved
background_image = background_image.resize((700, 600))   # resizes the image to fit
background_photo = ImageTk.PhotoImage(background_image)  # puts the photo as the background

background_label = Label(root, image=background_photo)     # creates label for image
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # position of image
background_label.lower() # keeps the photo in the back so it doesnt accidentally go on top (makes sure you can see text)

# Source - Classwork / modified
# These variables store the dropdown choices
bowtype_variable = StringVar()
bowtype_variable.set("Select the bow type")

distance_variable = StringVar()
distance_variable.set("Select a distance")

# Source - Classwork / modified
# these lines creates variables that will save the text that was entered by the user in the entry boxes
name_variable = StringVar()
score1_variable = StringVar()
score2_variable = StringVar()
score3_variable = StringVar()
score4_variable = StringVar()
score5_variable = StringVar()
score6_variable = StringVar()

average = 0 # creates average before anything runs so the varible will exist before team_placement runs


# Source - Classwork / modified slightly to fit my concept
# creating a function that will run when the user clicks the button (calculate score) at the bottom and will get values
def calculate_score():
    name = name_variable.get()  #gets the name the user entered
    bow_type = bowtype_variable.get()  #gets the bow type the user selected from dropdown
    distance = distance_variable.get()  #gets the distance the user selected from dropdown

    # Source - My code
    # these lines make sure the user picked a bow type and distance from the dropdown menu; if not a message pops up
    if bow_type == "Select the bow type":
        result_label.config(text="Please select a bow type.")
        return

    if distance == "Select a distance":
        result_label.config(text="Please select a valid distance.")
        return

    # Source - External (W3 Schools) ; modified for my work
    # Try to turn the score entries into numbers
    try:
        s1 = int(score1_variable.get())
        s2 = int(score2_variable.get())
        s3 = int(score3_variable.get())
        s4 = int(score4_variable.get())
        s5 = int(score5_variable.get())
        s6 = int(score6_variable.get())
    except:
        result_label.config(text="Please enter a valid number.")
        return

    # Source - My work
    # Validation for score entry boxes to make sure the scores are not above 30 (not a valid or realisitic score)
    if (s1 > 30 or s2 > 30 or s3 > 30 or
        s4 > 30 or s5 > 30 or s6 > 30):
        result_label.config(text="End score can't be higher than 30. Enter a valid score.")
        return

    # Source - My work
    # Validation for score entry boxes to make sure the entered scores are not a negative number
    if (s1 < 0 or s2 < 0 or s3 < 0 or
        s4 < 0 or s5 < 0 or s6 < 0):
        result_label.config(text="End score can't be a negative number. Enter a valid score.")
        return

    # Source - My work
    # calculates the total score and also the average score per end (will be used in results section)
    total = s1 + s2 + s3 + s4 + s5 + s6
    global average  # the averages are saved everywhere (not just inside one function) so other functions can use it
    average = total / 6

    # Source - Classwork (if/elif/else logic) & my work (messages)
    # these lines use if/elif/else to determine the users skill level based on their average score and gives message)
    if average < 10:
        level = "Beginner"
        message = "Keep practicing!"
    elif average <= 20:
        level = "Intermediate"
        message = "Nice job!"
    elif average <= 29:
        level = "Advanced"
        message = "Awesome shooting!"
    else:
        level = "Master"
        message = "Perfect Score!"

    # Source - Classwork / My code (modified & layout of message)
    # this shows the results after pressing the calculate score button (name & total scorem distance, etc)
    result_label.config(
        text="NAME:              " + name +
             "\nBOW TYPE:        " + bow_type +
             "\nDISTANCE:        " + distance +
             "\nTOTAL SCORE:     " + str(total) +
             "\nAVERAGE SCORE:   " + str(round(average, 2)) +
             "\nSKILL LEVEL:     " + level +
             "\n\n" + message)

    result_label.grid(row=12, column=1, columnspan=2, pady=20)

    # Source - External (Google - AskPython); modified to my project
    # these lines let me save the data the user inputs into a csv file
    file_exists = os.path.isfile("archery_score_tracker_app.csv")

    with open("archery_score_tracker_app.csv", "a", newline="") as file:   # this line opens the csv file
        writer = csv.writer(file)   # creates the writer so I can write data in the csv file

        if not file_exists:    # creates headings for the file and all data entered will go under headers
            writer.writerow(["Archer's Name", "Bow Type", "Distance",
                             "End 1 Score", "End 2 Score", "End 3 Score",
                             "End 4 Score", "End 5 Score", "End 6 Score",
                             "Total Score", "Average Score (per end)", "Skill Level"])

        archery_csvfile_data = [  # creates a list that will store the inputted data that will be saved
            [name, bow_type, distance,
             s1, s2, s3, s4, s5, s6,
             total, round(average,2), level]
        ]
        writer.writerows(archery_csvfile_data)  # writes the data into the csv file in a new row

# Source - My work (layout from other button but modified for new concept) & External
# creating a function that will find which team the current archer should be placed on depending on the data entered
# would be used if an instructor were sorting students (for example)
def team_placement():
    try:
        with open("archery_score_tracker_app.csv", "r") as file:  # opens the csv file with all past data
            reader = csv.reader(file)   # reads the file
            next(reader)                # skips the header

            averages = []     # creates empty list to store all previous averages

            for row in reader:   # creates a loop for it to go through each row
                averages.append(float(row[10]))  # adds the average score from each row in the list

        current_average = float(round(average, 2))   # gets the current user's average score

        # below code puts the archer in a team depending on current average
        if current_average < 15:
            team = "Beginner Team"
        elif current_average <= 22:
            team = "Intermediate Team"
        else:
            team = "Advanced Team"

        # updates the results and adds team placement
        result_label.config(text=result_label.cget("text") + "\nSuggested Team Placement: " + team)
        result_label.grid(row=12, column=1, columnspan=2, pady=20)

    #if the file doesnt exist then it will show this message
    except:
        result_label.config(text="Error. No data found.")
        result_label.grid(row=12, column=1, columnspan=2, pady=20)


# Source - Classwork (creating labels, placing them with rows/columns) / modified
# the lines of code below are the labels (like the titles) of each entry box so it tells the user what to enter)
lb1_score = Label(root, text="Archer Name", bg="white", fg="black")
lb1_score.grid(row=1, column=1, padx=20, pady=5)

lb2_bow = Label(root, text="Bow Type", bg="white", fg="black")  #the background white and words black - easier to see
lb2_bow.grid(row=2, column=1, padx=20, pady=5)  #placement of label in row 2 and column 1 (same to all labels below)

lb3_distance = Label(root, text="Distance (meters)", bg="white", fg="black")
lb3_distance.grid(row=3, column=1, padx=20, pady=5)

lb4_score = Label(root, text="End 1 Score", bg="white", fg="black")
lb4_score.grid(row=4, column=1, padx=20, pady=5)

lb5_score = Label(root, text="End 2 Score", bg="white", fg="black")
lb5_score.grid(row=5, column=1, padx=20, pady=5)

lb6_score = Label(root, text="End 3 Score", bg="white", fg="black")
lb6_score.grid(row=6, column=1, padx=20, pady=5)

lb7_score = Label(root, text="End 4 Score", bg="white", fg="black")
lb7_score.grid(row=7, column=1, padx=20, pady=5)

lb8_score = Label(root, text="End 5 Score", bg="white", fg="black")
lb8_score.grid(row=8, column=1, padx=20, pady=5)

lb9_score = Label(root, text="End 6 Score", bg="white", fg="black")
lb9_score.grid(row=9, column=1, padx=20, pady=5)

# Source - Classwork (tkinter, GUI, etc) / modified
# this is the dropdown menu with different bow types
bow_options = ["Olympic Recurve", "Barebow Recurve", "Compound"]
bow_dropdown = OptionMenu(root, bowtype_variable, *bow_options)
bow_dropdown.grid(row=2, column=2)

# Source - My work (layout from previous) and Classwork / modified
# the dropdown menu to pick distance options
distance_options = ["10m", "20m", "30m", "50m", "70m"]
distance_dropdown = OptionMenu(root, distance_variable, *distance_options)
distance_dropdown.grid(row=3, column=2)

# Source - Classwork (Entry boxes); customized for my work
# all lines of code below are the entry boxes & placement of boxes ; where user types in the data (name, score, etc)
entry_name = Entry(root, textvariable=name_variable)
entry_name.grid(row=1, column=2)

entry_score1 = Entry(root, textvariable=score1_variable)
entry_score1.grid(row=4, column=2)

entry_score2 = Entry(root, textvariable=score2_variable)
entry_score2.grid(row=5, column=2)

entry_score3 = Entry(root, textvariable=score3_variable)
entry_score3.grid(row=6, column=2)

entry_score4 = Entry(root, textvariable=score4_variable)
entry_score4.grid(row=7, column=2)

entry_score5 = Entry(root, textvariable=score5_variable)
entry_score5.grid(row=8, column=2)

entry_score6 = Entry(root, textvariable=score6_variable)
entry_score6.grid(row=9, column=2)

# Source - Classwork (code for button); customized for my work (only slightly - title, placement)
# this creates the button at the bottom the user will click and it will calculate their total scores/overall results
button1_calculatescore = Button(root, text="Calculate Score", width=15, command=calculate_score)
button1_calculatescore.grid(row=10, column=1, padx=10, pady=15, sticky="e")

# Source - My work (button layout but modified)
button2_teamplacement = Button(root, text="Place in a Team", width=15, command=team_placement)
button2_teamplacement.grid(row=10, column=2, padx=10, pady=15, sticky="w")

# Source - My code (label that will display the final results)
# This is the results label that shows all of the calculated scores, averages, etc (shows up when button is clicked)
# formatting: bd=border thickness; relief=makes it look like a card; padx=space left/right; pady=space top/bottom
result_label = Label(root, text="", justify=LEFT, anchor="w", bg="#90D5FF", fg="black",
                     bd=2, relief="solid", padx=15, pady=10)

# this line keeps window open so user can continue to use it
root.mainloop()