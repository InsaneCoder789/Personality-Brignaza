import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import FLAT



class App(tk.Tk):
    def __init__(self, questions, options, answers, *args, **kwargs):
        super().__init__()
        self.questions = questions
        self.options = options
        self.answers = answers
        self.questions_index = 0
        self.title("Personality Test!")
        self.create_start_page()

    def create_start_page(self):
        self.start_label = tk.Label(self, text="Welcome to the Personality Test Game!")
        self.start_label.pack(pady=(10,30))
        self.img1 = PhotoImage(file="Images/transparentGradHat.png")

        self.labelimage = Label(
    self,
    image = self.img1,
    background = "#ffffff",
)
        self.labelimage.pack(pady=(40,0))

        self.labeltext = Label(
    self,
    text = "Personality Test",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
        self.labeltext.pack(pady=(0,50))

        self.img2 = PhotoImage(file="Images/Frame.png")

        self.name_label = tk.Label(self, text="Please enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=(2,5))

        self.btnStart = Button(
    self,
    image = self.img2,
    relief = FLAT,
    border = 0,
    command = self.start_questionnaire)
        self.btnStart.pack()




        self.lblInstruction = Label(
    self,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
        self.lblInstruction.pack(pady=(10,20))

        self.lblRules = Label(
    self,
    text = "This Test contains 15 questions\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
        self.lblRules.pack()

    def start_questionnaire(self):
        self.start_label.destroy()
        self.labelimage.destroy()
        self.labeltext.destroy()
        self.name_label.destroy()
        self.name_entry.destroy()
        self.btnStart.destroy()
        self.lblInstruction.destroy()
        self.lblRules.destroy()
        
        
        
        self.questions = [
        '1. When a group of individuals are engaged in an activity, what do you do?',
        '2. Can you speak to a group of strangers without having difficulty expressing yourself ?',
        '3. Can you carry on as usual while others are watching without being uncomfortable ?',
        '4. Do you think that you are doing everything that is expected of you and that things are going well for you ?',
        '5. When something is bothering you, you :',
        '6. Do you believe that compared to other people, your life seems smoother and more gratifying ?',
        "7. Can you remain joyful even when things aren't going well ?",
        "8. Do you become irritated if someone takes your stuff from you without seeking permission ?",
        "9. If your peers exclude you from a game, you:”,”What sort of friends do you prefer having ?",
        "10. Are you someone who is usually careful ?",
        "11. Do you ever have the thought that 'People are so irrational, they can't even be entrusted to care for their own good' ?",
        "12. Do you ever get the feeling that you aren't much good or that you never do anything meaningful ?",
        "13. Do you become really upset with others when something goes wrong before you begin to consider what might be done to fix it ?",
        "14. Have you ever felt as though your feelings are so bottled up, you could burst ?"

]



        self.options = [


            ["Take an active part in what they are doing", "in between", "usually only watch"],
            ["Yes","Perhaps","No"],
            ["Yes","Perhaps","No"],
            ["Yes","Perhaps","No"],
            ["Try to ignore until you cool off ","Uncertain","Blow off steam"],
            ["Yes","Perhaps","No"],
            ["Yes","Perhaps","No"],
            ["Yes","Perhaps","No"],
            ["Feel hurt and angry","In between ","Believe it is by mistake"],
            ["those who are more serious","Uncertain","hose who kid around"],
            ["Yes","Perhaps","No"],
            ["Yes","Perhaps","No"],
            ["Yes","Perhaps","No"],
            ["Often","Sometimes","Seldom"],
            ["Often","Sometimes","Seldom"],


            ]
        
        


        self.answers = []
        self.index = 0
        self.answer_list = []

        self.title("Questionnaire")

        self.img = ImageTk.PhotoImage(Image.open("Images/QnAFrame.png"))
        self.img_label = tk.Label(self, image=self.img)
        self.img_label.pack()
        self.geometry("{}x{}".format(self.img.width(), self.img.height()))

        self.question_label = tk.Label(self, text=self.questions[self.index])
        self.question_label.place(relx=0.5, rely=0.4, anchor="center")

        self.option1_button = tk.Button(self, text=self.options[self.index][0], command=lambda: self.select_option(0))
        self.option1_button.pack(padx=150, pady=250, anchor="center")

        self.option2_button = tk.Button(self, text=self.options[self.index][1], command=lambda: self.select_option(1))
        self.option2_button.pack(padx=250, pady=250, anchor="center")

        self.option3_button = tk.Button(self, text=self.options[self.index][2], command=lambda: self.select_option(2))
        self.option3_button.pack(padx=350, pady=250, anchor="center")

        self.next_button = tk.Button(self, text="Next", font=("Helvetica", 14), command=self.next_question)
        self.next_button.place(relx=0.5, rely=0.92, anchor="center")

    def select_option(self, option_index):
        self.answers.append(self.options[self.index][option_index])

    def next_question(self):
        self.questions_index += 1
        self.index += 1
        self.question_label.config(text=self.questions[self.questions_index])
        self.option1_button.config(text=self.options[self.index][0])
        self.option2_button.config(text=self.options[self.index][1])
        self.option3_button.config(text=self.options[self.index][2])

        if self.questions == self.questions[-1]:
            self.next_button.config(text="Finish", command=self.finish)
            self.next_button.pack()

    def finish(self):
        correct = 0
        for i in range(len(self.answers)):
            if self.output[i] == self.answers[i]:
                correct += 1
        print(f"You got {correct} out of {len(self.answers)} correct.")


if __name__ == "__main__":
    app = App('questions', 'options', 'answers')
    app.mainloop()
