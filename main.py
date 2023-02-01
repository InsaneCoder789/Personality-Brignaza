import tkinter as tk
import tkinter as ttk
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
        # self.start_label = tk.Label(self, text="Welcome to the Personality Test Game!")
        # self.start_label.pack(pady=(10,30))
        self.img1 = PhotoImage(file="Images/transparentGradHat.png")

        self.labelimage = Label(
            self,
            image=self.img1,
            background="#ffffff",
        )
        self.labelimage.pack(pady=(40, 0))

        self.labeltext = Label(
            self,
            text="Personality Test",
            font=("Comic sans MS", 24, "bold"),
            background="#ffffff",
        )
        self.labeltext.pack(pady=(10, 50))

        self.img2 = PhotoImage(file="Images/Frame.png")

        self.name_label = tk.Label(self, text="Please enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=(2, 5))

        self.btnStart = Button(
            self,
            image=self.img2,
            relief=FLAT,
            border=0,
            command=self.start_questionnaire,
        )
        self.btnStart.pack()

        self.lblInstruction = Label(
            self,
            text="Read The Rules And\nClick Start Once You Are ready",
            background="#ffffff",
            font=("Consolas", 14),
            justify="center",
        )
        self.lblInstruction.pack(pady=(10, 20))

        self.lblRules = Label(
            self,
            text="This Test contains 15 questions\nOnce you select a radio button that will be a final choice\nhence think before you select",
            width=100,
            font=("Times", 14),
            background="#000000",
            foreground="#FACA2F",
        )
        self.lblRules.pack()

    def start_questionnaire(self):
        # self.start_label.destroy()
        self.labelimage.destroy()
        self.labeltext.destroy()
        self.name_label.destroy()
        self.name_entry.destroy()
        self.btnStart.destroy()
        self.lblInstruction.destroy()
        self.lblRules.destroy()

        self.questions = [
            "1. When a group of individuals are engaged in an activity, what do you do?",
            "2. Can you speak to a group of strangers without having difficulty expressing yourself ?",
            "3. Can you carry on as usual while others are watching without being uncomfortable ?",
            "4. Do you think that you are doing everything that is expected of you and that things are going well for you ?",
            "5. When something is bothering you, you :",
            "6. Do you believe that compared to other people, your life seems smoother and more gratifying ?",
            "7. Can you remain joyful even when things aren't going well ?",
            "8. Do you become irritated if someone takes your stuff from you without seeking permission ?",
            "9. If your peers exclude you from a game, you:",
            "10.What sort of friends do you prefer having ?",
            "11. Are you someone who is usually careful ?",
            "12. Do you ever have the thought that 'People are so irrational, they can't even be entrusted to care for their own good' ?",
            "13. Do you ever get the feeling that you aren't much good or that you never do anything meaningful ?",
            "14. Do you become really upset with others when something goes wrong before you begin to consider what might be done to fix it ?",
            "15. Have you ever felt as though your feelings are so bottled up, you could burst ?",
            "",
        ]

        self.options = [
            [
                "Take an active part in what they are doing",
                "in between",
                "usually only watch",
            ],
            ["Yes", "Perhaps", "No"],
            ["Yes", "Perhaps", "No"],
            ["Yes", "Perhaps", "No"],
            ["Try to ignore until you cool off ", "Uncertain", "Blow off steam"],
            ["Yes", "Perhaps", "No"],
            ["Yes", "Perhaps", "No"],
            ["Yes", "Perhaps", "No"],
            ["Feel hurt and angry", "In between ", "Believe it is by mistake"],
            ["those who are more serious", "Uncertain", "hose who kid around"],
            ["Yes", "Perhaps", "No"],
            ["Yes", "Perhaps", "No"],
            ["Yes", "Perhaps", "No"],
            ["Often", "Sometimes", "Seldom"],
            ["Often", "Sometimes", "Seldom"],
            ["", "", ""],
        ]

        self.answers = []
        self.index = 0
        self.answer_list = []

        self.title("Questionnaire")

        self.img = ImageTk.PhotoImage(Image.open("Images/QnAFrame.png"))
        self.img_label = tk.Label(self, image=self.img)
        self.img_label.pack()
        self.geometry("{}x{}".format(self.img.width(), self.img.height()))

        self.question_label = ttk.Label(
            self, text=self.questions[self.index], font=("Alegreya", 12), bg="#ffffff"
        )
        self.question_label.place(relx=0.5, rely=0.4, anchor="center")

        self.var = tk.StringVar()
        self.var.set(None)

        self.option1_button = ttk.Radiobutton(
            self,
            text=self.options[self.index][0],
            font=("Alegreya", 15),
            bg="#F8E6DF",
            variable=self.var,
            value=self.options[self.index][0],
        )
        self.option1_button.place(relx=0.5, rely=0.56, anchor="center")

        self.option2_button = ttk.Radiobutton(
            self,
            text=self.options[self.index][1],
            font=("Alegreya", 15),
            bg="#F8E6DF",
            variable=self.var,
            value=self.options[self.index][1],
        )
        self.option2_button.place(relx=0.5, rely=0.68, anchor="center")

        self.option3_button = ttk.Radiobutton(
            self,
            text=self.options[self.index][2],
            font=("Alegreya", 15),
            bg="#F8E6DF",
            variable=self.var,
            value=self.options[self.index][2],
        )
        self.option3_button.place(relx=0.5, rely=0.80, anchor="center")

        self.next_button = ttk.Button(
            self, text="Next", font=("Alegreya", 14), command=self.next_question
        )
        self.next_button.place(relx=0.5, rely=0.89, anchor="center")

    def handle_selection(self):
        selected_value = self.var.get()
        if selected_value in self.options[self.index]:
            selected_index = self.options[self.index].index(selected_value)
            if [self.index, selected_index] not in self.answers:
                self.answers.append(selected_index)

    # def select_option(self, option_index):
    # self.answers.append(self.options[self.index][option_index])

    def next_question(self):
        if self.var.get() == "None":
            return

        self.handle_selection()
        self.var.set(None)
        self.questions_index += 1
        self.index += 1
        self.question_label.config(text=self.questions[self.questions_index])
        self.option1_button.config(
            text=self.options[self.index][0], value=self.options[self.index][0]
        )
        self.option2_button.config(
            text=self.options[self.index][1], value=self.options[self.index][1]
        )
        self.option3_button.config(
            text=self.options[self.index][2], value=self.options[self.index][2]
        )

        if self.questions_index == len(self.questions) - 1:
            self.next_button.destroy()
            self.finish_button = ttk.Button(
                self, text="Finish", font=("Alegreya", 14), command=self.finish
            )
            self.finish_button.place(relx=0.5, rely=0.89, anchor="center")

    def finish(self):

        # removing all the above images and labels and questions
        self.img_label.destroy()
        self.question_label.destroy()
        self.option1_button.destroy()
        self.option2_button.destroy()
        self.option3_button.destroy()
        self.finish_button.destroy()

        # Structuring of the Answering element (Line 216 -  )

        # Credit Goes to Rehatbir Singh for helping me out in this Part
        # @MysteryCoder456
        # Copyright @ 2023

        # Personality List
        personality = []

        personality_descriptions = {
            # Architect
            "INTJA": "Hello Your a ARCHITECT PERSON !",
            "INTJT": "Hello Your a ARCHITECT PERSON !",
            # Logician
            "INTPA": "Hello Your a LOGICIAN PERSON !",
            "INTPT": "Hello Your a LOGICIAN PERSON !",
            # Commander
            "ENTJA": "Hello Your a COMMANDER PERSON !",
            "ENTJT": "Hello Your a COMMANDER PERSON !",
            # Debator
            "ENTPA": "Hello Your a DEBATOR PERSON !",
            "ENTPT": "Hello Your a DEBATOR PERSON !",
            # Advocate
            "INFJA": "Hello Your a ADVOCATE PERSON !",
            "INFJT": "Hello Your a ADVOCATE PERSON !",
            # Mediator
            "INFPA": "Hello Your a MEDIATOR PERSON !",
            "INFPT": "Hello Your a MEDIATOR PERSON !",
            # Protagonist
            "ENFJA": "Hello Your a PROTAGONIST PERSON !",
            "ENFJT": "Hello Your a PROTAGONIST PERSON !",
            # Campaigner
            "ENFPA": "Hello Your a CAMPAIGNER PERSON !",
            "ENFPT": "Hello Your a CAMPAIGNER PERSON !",
            # Logistician
            "ISTJA": "Hello Your a LOGISTICIAN PERSON !",
            "ISTJT": "Hello Your a LOGISTICAN PERSON !",
            # Defender
            "ISFJA": "Hello Your a DEFENDER PERSON !",
            "ISFJT": "Hello Your a DEFENDER PERSON !",
            # Executive
            "ESTJA": "Hello Your a EXECUTIVE PERSON !",
            "ESTJT": "Hello Your a EXECUTIVE PERSON !",
            # Consul
            "ESFJA": "Hello Your a CONSUL PERSON !",
            "ESFJT": "Hello Your a CONSUL PERSON !",
            # Virtuoso
            "ISTPA": "Hello Your a VIRTUOSO PERSON !",
            "ISTJT": "Hello Your a VIRTUOSO PERSON !",
            # Adventure
            "ISFPA": "Hello Your a ADVENTURE PERSON !",
            "ISFPT": "Hello Your a ADVENTURE PERSON !",
            # Entreprenuer
            "ESTPA": "Hello Your a ENTREPRENUER PERSON !",
            "ESTPT": "Hello Your a ENTREPRENUER PERSON !",
            # Entertainer
            "ESFPA": "Hello Your a ENTERTAINER PERSON !",
            "ESFPT": "Hello Your a ENTERTAINER PERSON !",
            # all ur 16 possible types
        }

        # 1  Introvert - Extrovert
        if self.answers[:3].count(2) >= 2:
            print("Introvert - [I]!")
            personality.append("I")
        else:
            print("Extrovert - [E]!")
            personality.append("E")

        # 2 Observant - Intuitive
        if self.answers[3:6].count(2) >= 0:
            print("Observant - [S]!")
            personality.append("S")
        else:
            print("Intuitive - [N]!")
            personality.append("N")

        # 3 Thinking - Feeling
        if self.answers[6:9].count(2) >= 0:
            print("Feeling - [F]!")
            personality.append("F")
        else:
            print("Thinking - [T]!")
            personality.append("I")

        # 4 Judging - Prospecting
        if self.answers[9:12].count(2) >= 0:
            print("Judging - [J]!")
            personality.append("J")
        else:
            print("Prospecting - [P]!")
            personality.append("P")

        # 5 Assertive - Turbulent
        if self.answers[12:15].count(2) >= 0:
            print("Turbulent - [T]!")
            personality.append("T")
        else:
            print("Assertive - [A]!")
            personality.append("A")

        personality_str = "".join(personality)
        personality_desc = personality_descriptions[personality_str]
        print(personality)
        print(personality_str)
        print(f"Your personality is {personality_str}")
        print(personality_desc)

        # GUI Design of the page
        self.title("Finale!")

        self.img4 = ImageTk.PhotoImage(Image.open("Images/FinalFrame.png"))
        self.img_label1 = tk.Label(self, image=self.img4)
        self.img_label1.pack()
        self.geometry("{}x{}".format(self.img4.width(), self.img4.height()))

        self.textbox = tk.Text(self, height=5, width=30)
        self.textbox.pack()

        personality_detail = personality_descriptions[personality_str]
        self.textbox.insert(tk.END, personality_detail)


if __name__ == "__main__":
    app = App("questions", "options", "answers")
    app.mainloop()
