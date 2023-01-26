import tkinter as tk
from tkinter import *
from tkinter import messagebox

scale_res = '974x968+0+0'




def personality_test():

    name = name_entry.get()
    root.destroy()
    print(name)
    if name == "":
        messagebox.showerror("Error", "Please enter your name.")
    
        

    introvert = 0 
    extrovert = 0 
    observant = 0 
    intuitive = 0 
    thinking = 0 
    feeling = 0 
    judging = 0 
    prospecting = 0 
    assertive = 0 
    turbulent = 0 
    score = 0


# Q1 to Q3 = Introvert - Extrovert Determination -- [Mind]

# Question 1
    question1 = tk.Tk()
    question1.title("Question 1")
    question1.geometry(scale_res)
    image = PhotoImage(file='Images/QnAFrame.png')
    image_label = tk.Label(question1, image=image)
    image_label.pack()

    # Heading Frame
    heading_frame = tk.Frame(question1, bg='white', width=974, height=100)
    heading_frame.place(x=0, y=0)

    #Question Frame 
    question_frame = tk.Frame(question1, bg='white', width=974, height=150)
    question_frame.place(x=0, y=100)

    #OptionFrame 
    options_frame = tk.Frame(question1, bg='white', width=974, height=150)
    options_frame.place(x=0, y=250)


    #Next Button Frame 
    button_frame = tk.Frame(question1, bg='white', width=100, height=50)
    button_frame.place(x=20, y=190)

    q1label = tk.Label(question_frame, text="When a group of individuals are engaged in an activity, what do you do?")
    q1label.pack()
    q1var = tk.StringVar(question1)
    ques1_opt1_button = tk.Radiobutton(options_frame, text="Take an active part in what they are doing",background='black', variable=q1var, value=1)
    ques1_opt1_button.pack()
    ques1_opt2_button = tk.Radiobutton(options_frame, text="in between", variable=q1var, value=2)
    ques1_opt2_button.pack()
    ques1_opt3_button = tk.Radiobutton(options_frame, text="usually only watch", variable=q1var, value=3)
    ques1_opt3_button.pack()
    submit_button = tk.Button(button_frame, text="Next", command=question1.destroy)
    submit_button.pack()
    question1.mainloop()
    if q1var.get() == 1:  # Extrovert 
        extrovert += 1 
    if q1var.get() == 2:
        extrovert += 1
    if q1var.get() == 3: # Introvert 
        introvert += 1


# Question 2
    question2 = tk.Tk()
    question2.title("Question 2")
    question2.geometry(scale_res)
    q2label = tk.Label(question2, text="Q.  Can you speak to a group of strangers without having difficulty expressing yourself ?")
    q2label.pack()
    q2var = tk.StringVar(question2)
    ques2_opt1_button = tk.Radiobutton(question2, text="Yes", variable=q2var, value=1)
    ques2_opt1_button.pack()
    ques2_opt2_button = tk.Radiobutton(question2, text="Perhaps", variable=q2var, value=2)
    ques2_opt2_button.pack()
    ques2_opt3_button = tk.Radiobutton(question2, text="No", variable=q2var, value=3)
    ques2_opt3_button.pack()
    submit_button = tk.Button(question2, text="Next", command=question2.destroy)
    submit_button.pack()
    question2.mainloop()
    if q2var.get() == 1:  # Extrovert 
        extrovert += 1 
    if q2var.get() == 2:
        extrovert += 1
    if q2var.get() == 3: # Introvert 
        introvert += 1


# Question 3
    question3 = tk.Tk()
    question3.title("Question 3")
    question3.geometry(scale_res)
    q3label = tk.Label(question3, text="Q.Can you carry on as usual while others are watching without being uncomfortable ?")
    q3label.pack()
    q3var = tk.StringVar(question3)
    ques3_opt1_button = tk.Radiobutton(question3, text="Yes", variable=q3var, value=1)
    ques3_opt1_button.pack()
    ques3_opt2_button = tk.Radiobutton(question3, text="Perhaps", variable=q3var, value=2)
    ques3_opt2_button.pack()
    ques3_opt3_button = tk.Radiobutton(question3, text="No", variable=q3var, value=3)
    ques3_opt3_button.pack()
    submit_button = tk.Button(question3, text="Next", command=question3.destroy)
    submit_button.pack()
    question3.mainloop()
    if q3var.get() == 1:  # Extrovert 
        extrovert += 1 
    if q3var.get() == 2:
        extrovert+= 1
    if q3var.get() == 3: # Introvert 
        introvert += 1



#Q4 - Q6  Observant - Intuitive Determination [Energy]


# Question 4
    question4 = tk.Tk()
    question4.title("Question 4")
    question4.geometry(scale_res)
    q4label = tk.Label(question4, text="Q. Do you think that you are doing everything that is expected of you and that things are going well for you ?")
    q4label.pack()
    q4var = tk.StringVar(question4)
    ques4_opt1_button = tk.Radiobutton(question4, text="Yes", variable=q4var, value=1)
    ques4_opt1_button.pack()
    ques4_opt2_button = tk.Radiobutton(question4, text="Perhaps", variable=q4var, value=2)
    ques4_opt2_button.pack()
    ques4_opt3_button = tk.Radiobutton(question4, text="No", variable=q4var, value=3)
    ques4_opt3_button.pack()
    submit_button = tk.Button(question4, text="Next", command=question4.destroy)
    submit_button.pack()
    question4.mainloop()
    if q4var.get() == 1:  # Extrovert 
        observant += 1 
    if q4var.get() == 2:
        intuitive += 1
    if q4var.get() == 3: # Introvert 
        intuitive += 1




# Question 5
    question5 = tk.Tk()
    question5.title("Question 5")
    question5.geometry(scale_res)
    q5label = tk.Label(question5, text="Q.Do you believe that compared to other people, your life seems smoother and more gratifying ?")
    q5label.pack()
    q5var = tk.StringVar(question5)
    ques5_opt1_button = tk.Radiobutton(question5, text="Yes", variable=q5var, value=1)
    ques5_opt1_button.pack()
    ques5_opt2_button = tk.Radiobutton(question5, text="Perhaps", variable=q5var, value=2)
    ques5_opt2_button.pack()
    ques5_opt3_button = tk.Radiobutton(question5, text="No", variable=q5var, value=3)
    ques5_opt3_button.pack()
    submit_button = tk.Button(question5, text="Next", command=question5.destroy)
    submit_button.pack()
    question5.mainloop()
    if q5var.get() == 1:  # Extrovert 
        observant += 1 
    if q5var.get() == 2:
        intuitive += 1
    if q5var.get() == 3: # Introvert 
        intuitive += 1








# Question 6
    question6 = tk.Tk()
    question6.title("Question 6")
    question6.geometry(scale_res)
    q6label = tk.Label(question6, text="Q.When something is bothering you, you : ")
    q6label.pack()
    q6var = tk.StringVar(question6)
    ques6_opt1_button = tk.Radiobutton(question6, text="Try to ignore until you cool off ", variable=q6var, value=1)
    ques6_opt1_button.pack()
    ques6_opt2_button = tk.Radiobutton(question6, text="Uncertain", variable=q6var, value=2)
    ques6_opt2_button.pack()
    ques6_opt3_button = tk.Radiobutton(question6, text="Blow off steam", variable=q6var, value=3)
    ques6_opt3_button.pack()
    submit_button = tk.Button(question6, text="Next", command=question6.destroy)
    submit_button.pack()
    question6.mainloop()
    if q6var.get() == 1:  # Extrovert 
        observant += 1 
    if q6var.get() == 2:
        intuitive += 1
    if q6var.get() == 3: # Introvert 
        intuitive += 1





# Q7 to Q9 Thinking - Feeling  Determination [Nature]



# Question 7
    question7 = tk.Tk()
    question7.title("Question 7")
    question7.geometry(scale_res)
    q7label = tk.Label(question7, text="Q.Can you remain joyful even when things aren't going well ?")
    q7label.pack()
    q7var = tk.StringVar(question7)
    ques7_opt1_button = tk.Radiobutton(question7, text="No", variable=q7var, value=1)
    ques7_opt1_button.pack()
    ques7_opt2_button = tk.Radiobutton(question7, text="Uncertain", variable=q7var, value=2)
    ques7_opt2_button.pack()
    ques7_opt3_button = tk.Radiobutton(question7, text="Yes", variable=q7var, value=3)
    ques7_opt3_button.pack()
    submit_button = tk.Button(question7, text="Next", command=question7.destroy)
    submit_button.pack()
    question7.mainloop()
    if q7var.get() == 1:  # Extrovert 
        thinking += 1 
    if q7var.get() == 2:
        feeling += 1
    if q7var.get() == 3: # Introvert 
        feeling += 1






# Question 8
    question8 = tk.Tk()
    question8.title("Question 8")
    question8.geometry(scale_res)
    q8label = tk.Label(question8, text="Q.Do you become irritated if someone takes your stuff from you without seeking permission ?")
    q8label.pack()
    q8var = tk.StringVar(question8)
    ques8_opt1_button = tk.Radiobutton(question8, text="Yes", variable=q8var, value=1)
    ques8_opt1_button.pack()
    ques8_opt2_button = tk.Radiobutton(question8, text="Perhaps", variable=q8var, value=2)
    ques8_opt2_button.pack()
    ques8_opt3_button = tk.Radiobutton(question8, text="No", variable=q8var, value=3)
    ques8_opt3_button.pack()
    submit_button = tk.Button(question8, text="Next", command=question8.destroy)
    submit_button.pack()
    question8.mainloop()
    if q8var.get() == 1:  # Extrovert 
        thinking += 1 
    if q8var.get() == 2:
        feeling += 1
    if q8var.get() == 3: # Introvert 
        feeling += 1






    # Question 9
    question9= tk.Tk()
    question9.title("Question 9")
    question9.geometry(scale_res)
    q9label = tk.Label(question9, text="Q.If your peers exclude you from a game, you:")
    q9label.pack()
    q9var = tk.StringVar(question9)
    ques9_opt1_button = tk.Radiobutton(question9, text="Feel Hurt and Angry", variable=q9var, value=1)
    ques9_opt1_button.pack()
    ques9_opt2_button = tk.Radiobutton(question9, text="In Between", variable=q9var, value=2)
    ques9_opt2_button.pack()
    ques9_opt3_button = tk.Radiobutton(question9, text="Believe it is by mistake", variable=q9var, value=3)
    ques9_opt3_button.pack()
    submit_button = tk.Button(question9, text="Next", command=question9.destroy)
    submit_button.pack()
    question9.mainloop()
    if q9var.get() == 1:  # Extrovert 
        thinking += 1 
    if q9var.get() == 2:
        feeling += 1
    if q9var.get() == 3: # Introvert 
        feeling += 1




# Q.10 to Q.12 Judging - Prospecting  Determination [Tactics]




    # Question 10
    question10 = tk.Tk()
    question10.title("Question 10")
    question10.geometry(scale_res)
    q10label = tk.Label(question10, text="Q.What sort of friends do you prefer having ?")
    q10label.pack()
    q10var = tk.StringVar(question10)
    ques10_opt1_button = tk.Radiobutton(question10, text="Those who are more serious", variable=q10var, value=1)
    ques10_opt1_button.pack()
    ques10_opt2_button = tk.Radiobutton(question10, text="Uncertain", variable=q10var, value=2)
    ques10_opt2_button.pack()
    ques10_opt3_button = tk.Radiobutton(question10, text="Those who kid Around", variable=q10var, value=3)
    ques10_opt3_button.pack()
    submit_button = tk.Button(question10, text="Next", command=question10.destroy)
    submit_button.pack()
    question10.mainloop()
    if q10var.get() == 1:  # Extrovert 
        judging += 1 
    if q10var.get() == 2:
        prospecting += 1
    if q10var.get() == 3: # Introvert 
        prospecting += 1




    # Question 11
    question11 = tk.Tk()
    question11.title("Question 11")
    question11.geometry(scale_res)
    q11label = tk.Label(question11, text="Q.Are you someone who is usually careful ?")
    q11label.pack()
    q11var = tk.StringVar(question11)
    ques11_opt1_button = tk.Radiobutton(question11, text="Yes", variable=q11var, value=1)
    ques11_opt1_button.pack()
    ques11_opt2_button = tk.Radiobutton(question11, text="In Between", variable=q11var, value=2)
    ques11_opt2_button.pack()
    ques11_opt3_button = tk.Radiobutton(question11, text="No", variable=q11var, value=3)
    ques11_opt3_button.pack()
    submit_button = tk.Button(question11, text="Next", command=question11.destroy)
    submit_button.pack()
    question11.mainloop()
    if q11var.get() == 1:  # Extrovert 
        judging += 1 
    if q11var.get() == 2:
        prospecting += 1
    if q11var.get() == 3: # Introvert 
        prospecting += 1







    # Question 12
    question12 = tk.Tk()
    question12.title("Question 12")
    question12.geometry(scale_res)
    q12label = tk.Label(question12, text="Q.  Can you speak to a group of strangers without having difficulty expressing yourself ?")
    q12label.pack()
    q12var = tk.StringVar(question12)
    ques12_opt1_button = tk.Radiobutton(question12, text="Yes", variable=q12var, value=1)
    ques12_opt1_button.pack()
    ques12_opt2_button = tk.Radiobutton(question12, text="Perhaps", variable=q12var, value=2)
    ques12_opt2_button.pack()
    ques12_opt3_button = tk.Radiobutton(question12, text="No", variable=q12var, value=3)
    ques12_opt3_button.pack()
    submit_button = tk.Button(question12, text="Next", command=question12.destroy)
    submit_button.pack()
    question2.mainloop()
    if q12var.get() == 1:  # Extrovert 
        judging += 1 
    if q12var.get() == 2:
        prospecting = 1
    if q12var.get() == 3: # Introvert 
        prospecting += 1



# Q. 13 to Q.15   Assertive - Turbulent Determination [Identity]



    # Question 13
    question13 = tk.Tk()
    question13.title("Question 13")
    question13.geometry(scale_res)
    q13label = tk.Label(question13, text="Do you ever get the feeling that you aren't much good or that you never do anything meaningful ?")
    q13label.pack()
    q13var = tk.StringVar(question2)
    ques13_opt1_button = tk.Radiobutton(question13, text="Yes", variable=q13var, value=1)
    ques13_opt1_button.pack()
    ques13_opt2_button = tk.Radiobutton(question13, text="Perhaps", variable=q13var, value=2)
    ques13_opt2_button.pack()
    ques13_opt3_button = tk.Radiobutton(question13, text="No", variable=q13var, value=3)
    ques13_opt3_button.pack()
    submit_button = tk.Button(question13, text="Next", command=question13.destroy)
    submit_button.pack()
    question13.mainloop()
    if q13var.get() == 1:  # Extrovert 
        turbulent += 1 
    if q13var.get() == 2:
        assertive += 1
    if q13var.get() == 3: # Introvert 
        assertive += 1







    # Question 14
    question14 = tk.Tk()
    question14.title("Question 14")
    question14.geometry(scale_res)
    q14label = tk.Label(question14, text="Q. Do you become really upset with others when something goes wrong before you begin to consider what might be done to fix it ?")
    q14label.pack()
    q14var = tk.StringVar(question14)
    ques14_opt1_button = tk.Radiobutton(question14, text="Yes", variable=q14var, value=1)
    ques14_opt1_button.pack()
    ques14_opt2_button = tk.Radiobutton(question14, text="Perhaps", variable=q14var, value=2)
    ques14_opt2_button.pack()
    ques14_opt3_button = tk.Radiobutton(question14, text="No", variable=q14var, value=3)
    ques14_opt3_button.pack()
    submit_button = tk.Button(question14, text="Next", command=question14.destroy)
    submit_button.pack()
    question14.mainloop()
    if q14var.get() == 1:  # Extrovert 
        turbulent += 1 
    if q14var.get() == 2:
        assertive += 1
    if q14var.get() == 3: # Introvert 
        assertive += 1





    # Question 15
    question15 = tk.Tk()
    question15.title("Question 15")
    question15.geometry(scale_res)
    q15label = tk.Label(question15, text="Q.Have you ever felt as though your feelings are so bottled up, you could burst ?")
    q15label.pack()
    q15var = tk.StringVar(question15)
    ques15_opt1_button = tk.Radiobutton(question15, text="Yes", variable=q15var, value=1)
    ques15_opt1_button.pack()
    ques15_opt2_button = tk.Radiobutton(question15, text="Perhaps", variable=q15var, value=2)
    ques15_opt2_button.pack()
    ques15_opt3_button = tk.Radiobutton(question15, text="No", variable=q15var, value=3)
    ques15_opt3_button.pack()
    submit_button = tk.Button(question15, text="Submit", command=question15.destroy)
    submit_button.pack()
    question15.mainloop()
    if q15var.get() == 1:  # Extrovert 
        turbulent += 1 
    if q15var.get() == 2:
        assertive += 1
    if q15var.get() == 3: # Introvert 
        assertive += 1




# HERE IS THE STRUCTURING OF THE ANSWER PART !!!! 

    # Results
    results = tk.Tk()
    results.title("Results")
    results.geometry("200x100")
    name = name_entry.get()

    if introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect") #INTJ 

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if prospecting >= 2 :
                    result_label = tk.Label(results, text="You are an Architect") #INTP

    elif extrovert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect") #ENTJ

    elif extrovert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")
    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect") 

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")
    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")
    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    elif introvert >= 2:
        if intuitive >= 2 :
            if thinking >= 2 :
                if judging >= 2 :
                    result_label = tk.Label(results, text="You are an Architect")

    else:
        result_label = tk.Label(results, text= "Hello "+name+" is not a human if you have none of the 16 personalities")
    result_label.pack()
    results.mainloop()



# Create the main window
root = tk.Tk()
root.title("Personality Test")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

start_label = tk.Label(root, text="Welcome to the Personality Test Game!")
start_label.pack(pady=(10,30))
img1 = PhotoImage(file="Images/transparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Personality Test",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Images/Frame.png")

name_label = tk.Label(root, text="Please enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=(2,5))

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = personality_test,
)
btnStart.pack()




lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,20))

lblRules = Label(
    root,
    text = "This Test contains 15 questions\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()

