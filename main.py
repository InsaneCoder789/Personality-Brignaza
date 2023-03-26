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
      #name entry of the person!
        self.name_label = tk.Label(self, text="Please enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=(2, 5))
      #Email entry of the person 
        self.email_label = tk.Label(self,text="Please Enter your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=(2,6))


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
        name = self.name_entry.get()
        email = self.email_entry.get()
        if not name :
            return
        elif not email :
            return 
        else :
            print("Name:- ",name)
            print("Email:- ",email)
        # self.start_label.destroy()
        self.labelimage.destroy()
        self.labeltext.destroy()
        self.name_label.destroy()
        self.name_entry.destroy()
        self.email_label.destroy()
        self.email_entry.destroy()
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
            "Press Finish to Submit Your response!",
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
        self.geometry("600x600")
#Questions in Label
        #self.question_label = ttk.Label(
        #    self, text=self.questions[self.index], font=("Alegreya", 10), bg="#ffffff",fg='black')
        #self.question_label.place(relx=0.5, rely=0.3, anchor="center")

        self.var = tk.StringVar()
        self.var.set(None)

#Questions in Textbox 
        self.QsBox1 = tk.Text(
            self,
            font=("Alegreya", 20),
            height=5,
            width=31,
            wrap=tk.WORD,
            fg="black",
            bg="#ffffff"
            )
        self.QsBox1.place(relx=0.150,rely=0.2)
        self.QsBox1.insert(tk.END,self.questions[0])


        self.option1_button = ttk.Radiobutton(
            self,
            text=self.options[self.index][0],
            font=("Alegreya", 16),
            bg="#F8E6DF",
            variable=self.var,
            value=self.options[self.index][0],
        )
        self.option1_button.place(relx=0.5, rely=0.47, anchor="center")

        self.option2_button = ttk.Radiobutton(
            self,
            text=self.options[self.index][1],
            font=("Alegreya", 16 ),
            bg="#F8E6DF",
            variable=self.var,
            value=self.options[self.index][1],
        )
        self.option2_button.place(relx=0.5, rely=0.60, anchor="center")

        self.option3_button = ttk.Radiobutton(
            self,
            text=self.options[self.index][2],
            font=("Alegreya", 16),
            bg="#F8E6DF",
            variable=self.var,
            value=self.options[self.index][2],
        )
        self.option3_button.place(relx=0.5, rely=0.73, anchor="center")

        self.next_button = ttk.Button(
            self, text="Next", font=("Alegreya", 14), command=self.next_question
        )
        self.next_button.place(relx=0.5, rely=0.825, anchor="center")

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
        self.QsBox1.delete("1.0", "end")
        self.QsBox1.insert(END,self.questions[self.questions_index])
        #self.question_label.config(text=self.questions[self.questions_index])
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
        self.QsBox1.destroy()
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
            "INTJA": "Logic-driven and quick-witted, architects take pleasure in their independence of thought and in their remarkable ability to spot hypocrisy and phoniness.But because architects' minds are constantly working, it may be difficult to find people who can keep up with their constant analysis of their surroundings.These skilled strategists are detail-oriented perfectionists who approach all they do with creativity and reason. They frequently have a complex, secretive inner life.",
            "INTJT": "Logic-driven and quick-witted, architects take pleasure in their independence of thought and in their remarkable ability to spot hypocrisy and phoniness.But because architects' minds are constantly working, it may be difficult to find people who can keep up with their constant analysis of their surroundings.These skilled strategists are detail-oriented perfectionists who approach all they do with creativity and reason. They frequently have a complex, secretive inner life.",
            # Logician
            "INTPA": "Logicians take great satisfaction in their distinctive viewpoints and sharp intelligence. These adaptable brains relish approaching many facets of life in an unusual way. They are compelled to ponder the universe's mysteries, which may help to explain why some of the greatest thinkers and scientists in history were logicians. Despite being a relatively uncommon personality type, Logicians aren't scared to stand out from the crowd thanks to their originality and inventiveness. They frequently take unconventional turns, fusing openness to trying new things with individual ingenuity.",
            "INTPT": "Logicians take great satisfaction in their distinctive viewpoints and sharp intelligence. These adaptable brains relish approaching many facets of life in an unusual way. They are compelled to ponder the universe's mysteries, which may help to explain why some of the greatest thinkers and scientists in history were logicians. Despite being a relatively uncommon personality type, Logicians aren't scared to stand out from the crowd thanks to their originality and inventiveness. They frequently take unconventional turns, fusing openness to trying new things with individual ingenuity.",
            # Commander
            "ENTJA": "Commanders are natural-born leaders. This personality type is an epitome of charisma and self-assurance, and they project authority in a way that unites people around a shared cause. However, Commanders also exhibit a callous level of reasoning that they frequently employ in order to accomplish whatever goals they have set for themselves.They are incisive individuals that cherish forward motion and success. To build their imaginative visions, they absorb facts, but they rarely ponder them for very long before acting on them.",
            "ENTJT": "Commanders are natural-born leaders. This personality type is an epitome of charisma and self-assurance, and they project authority in a way that unites people around a shared cause. However, Commanders also exhibit a callous level of reasoning that they frequently employ in order to accomplish whatever goals they have set for themselves.They are incisive individuals that cherish forward motion and success. To build their imaginative visions, they absorb facts, but they rarely ponder them for very long before acting on them.",
            # Debator
            "ENTPA": "Debaters don't hesitate to challenge the established quo. With a light sense of humor, this personality type's members are knowledgeable, inquisitive, and can be very entertaining. They only have an eccentric, divergent conception of enjoyment that includes a healthy serving of lively discussion.They frequently take risks and are highly creative, capable of quickly analyzing and reconstructing concepts. Regardless of any opposition they may experience, they persistently pursue their goals.",
            "ENTPT": "Debaters don't hesitate to challenge the established quo. With a light sense of humor, this personality type's members are knowledgeable, inquisitive, and can be very entertaining. They only have an eccentric, divergent conception of enjoyment that includes a healthy serving of lively discussion.They frequently take risks and are highly creative, capable of quickly analyzing and reconstructing concepts. Regardless of any opposition they may experience, they persistently pursue their goals.",
            # Advocate
            "INFJA": "Even though advocates (INFJs) are the least common personality type of all, they create a lasting impression on society. They want to stand upand change the world because they are idealistic and have strong morals. Success for Advocate personalities comes from finding satisfaction, helping others, and becoming a force for good in the world rather than from wealth or position.Although they have high ideals and desires, advocates are not idle daydreamers. Integrity is important to people with this personality type, and they are rarely happy until they have followed their moral convictions. They are deeply moral people who make decisions in life based on their own wisdom and intuition.!",
            "INFJT": "Even though advocates (INFJs) are the least common personality type of all, they create a lasting impression on society. They want to stand upand change the world because they are idealistic and have strong morals. Success for Advocate personalities comes from finding satisfaction, helping others, and becoming a force for good in the world rather than from wealth or position.Although they have high ideals and desires, advocates are not idle daydreamers. Integrity is important to people with this personality type, and they are rarely happy until they have followed their moral convictions. They are deeply moral people who make decisions in life based on their own wisdom and intuition.",
            # Mediator
            "INFPA": "Although Mediators may come out as reserved or unassuming, they actually have a vibrant, passionate inner life. They cheerfully lose themselves indaydreams, constructing all kinds of stories and discussions in their imaginative and creative brains. These individuals are renowned for theirsensitivity; mediators are capable of experiencing intense emotional reactions to music, art, the natural world, and others around them.Idealistic and compassionate, Mediators want for meaningful connections with people and feel compelled to lend a hand.",
            "INFPT": "Although Mediators may come out as reserved or unassuming, they actually have a vibrant, passionate inner life. They cheerfully lose themselves indaydreams, constructing all kinds of stories and discussions in their imaginative and creative brains. These individuals are renowned for theirsensitivity; mediators are capable of experiencing intense emotional reactions to music, art, the natural world, and others around them.Idealistic and compassionate, Mediators want for meaningful connections with people and feel compelled to lend a hand.",
            # Protagonist
            "ENFJA": "The protagonists are driven to fulfill a higher calling in life. These personality types are thoughtful and idealistic, and they want to make the world a better place for everyone. Even when it is extremely difficult to do the right thing, they rarely hesitate to do it.Protagonists are natural leaders, which explains why so many eminent politicians, coaches, and educators have personalities like this. Their enthusiasm and charm enable them to motivate people not only in their professional lives but also in all facets of their personal lives, also including their relationships.",
            "ENFJT": "The protagonists are driven to fulfill a higher calling in life. These personality types are thoughtful and idealistic, and they want to make the world a better place for everyone. Even when it is extremely difficult to do the right thing, they rarely hesitate to do it.Protagonists are natural leaders, which explains why so many eminent politicians, coaches, and educators have personalities like this. Their enthusiasm and charm enable them to motivate people not only in their professional lives but also in all facets of their personal lives, also including their relationships.",
            # Campaigner
            "ENFPA": "True free spirits, campaigners are extroverted, kind hearted, and open-minded. They distinguish themselves from the throng by their vibrant, positive outlook on life. These people frequently support radical concepts and take steps that show their feeling of optimism and compassion toward others.Their vibrant energy can flow in many multiple directions. However, despite the fact that they can be the life of the party, campaigners aren't only interested in having fun. The desire for profound, emotional relationships with others runs deep within this personality type.",
            "ENFPT": "True free spirits, campaigners are extroverted, kind hearted, and open-minded. They distinguish themselves from the throng by their vibrant, positive outlook on life. These people frequently support radical concepts and take steps that show their feeling of optimism and compassion toward others.Their vibrant energy can flow in many multiple directions. However, despite the fact that they can be the life of the party, campaigners aren't only interested in having fun. The desire for profound, emotional relationships with others runs deep within this personality type.",
            # Logistician
            "ISTJA": "Logisticians take great pride in their honesty. When they make a commitment to doing something, people with this personality type make sure to follow through. These folks typically have a restrained yet determined demeanor and a realistic attitude on life. Despite not being particularly showy or attention-seeking, logisticians contribute significantly to maintaining society's solid, secure foundation. Because of their dependability, practicality, and capacity to remain rational and grounded under pressure, logisticians frequently gain the respect of their families and communities. They carefully plan out their actions and execute them with a systematic purpose.",
            "ISTJT": "Logisticians take great pride in their honesty. When they make a commitment to doing something, people with this personality type make sure to follow through. These folks typically have a restrained yet determined demeanor and a realistic attitude on life. Despite not being particularly showy or attention-seeking, logisticians contribute significantly to maintaining society's solid, secure foundation. Because of their dependability, practicality, and capacity to remain rational and grounded under pressure, logisticians frequently gain the respect of their families and communities. They carefully plan out their actions and execute them with a systematic purpose.",
            # Defender
            "ISFJA": "Defenders contribute to the smooth operation of the world in their quiet, unobtrusive way. People with this personality type are dedicated and hardworking, and they have a strong feeling of duty to those under their care. Defenders can be relied upon to keep appointments, remember birthdays and other important dates, protect customs, and show their loved ones compassion and support. But despite everything they accomplish, they hardly ever take credit for it, preferring to work in the background. This personality type is capable, self-sufficient, and endowed with many flexible talents.Defenders are compassionate and empathetic, but they also have a keen analytical mind and attention to detail. In addition, despite their reserve, they frequently possess strong interpersonal abilities. Defenders are truly greater than the sum of their parts, and even in the most mundane areas of their everyday life, their diverse abilities are evident",
            "ISFJT": "Defenders contribute to the smooth operation of the world in their quiet, unobtrusive way. People with this personality type are dedicated and hardworking, and they have a strong feeling of duty to those under their care. Defenders can be relied upon to keep appointments, remember birthdays and other important dates, protect customs, and show their loved ones compassion and support. But despite everything they accomplish, they hardly ever take credit for it, preferring to work in the background. This personality type is capable, self-sufficient, and endowed with many flexible talents.Defenders are compassionate and empathetic, but they also have a keen analytical mind and attention to detail. In addition, despite their reserve, they frequently possess strong interpersonal abilities. Defenders are truly greater than the sum of their parts, and even in the most mundane areas of their everyday life, their diverse abilities are evident",
            # Executive
            "ESTJA": "Executives serve as stewards of tradition and law, using their knowledge of right and wrong and what is socially acceptable to unite families andcommunities. People with the Executive personality type embrace the virtues of integrity, commitment, and dignity. They are regarded for their precise advice and guidance, and they gladly take the lead on tough pathways. Executives, who take satisfaction in bringing people together, frequently take on roles as community organizers, working hard to unite everyone in support of the traditional values that keep families and communities together or in celebration of beloved local events.They have a strong will and steadfastly rely on their own common sense. They frequently act as a calming influence among others, able to provide firm guidance in the face of difficulty.!",
            "ESTJT": "Executives serve as stewards of tradition and law, using their knowledge of right and wrong and what is socially acceptable to unite families andcommunities. People with the Executive personality type embrace the virtues of integrity, commitment, and dignity. They are regarded for their precise advice and guidance, and they gladly take the lead on tough pathways. Executives, who take satisfaction in bringing people together, frequently take on roles as community organizers, working hard to unite everyone in support of the traditional values that keep families and communities together or in celebration of beloved local events.They have a strong will and steadfastly rely on their own common sense. They frequently act as a calming influence among others, able to provide firm guidance in the face of difficulty.",
            # Consul
            "ESFJA": "Life is sweetest for Consuls when it is shared with others. Many communities are built on the backs of people of this personality type who welcome friends, family, and neighbors into their homes and hearts. This does not imply that Consuls are saints or that they are tolerant of all people.However, consuls have a tendency to feel a feeling of obligation to those around them and do believe in the power of hospitality and politeness.Generous and trustworthy, those who fit this personality type frequently take it upon themselves to keep their families and communities together in both big and small ways.",
            "ESFJT": "Life is sweetest for Consuls when it is shared with others. Many communities are built on the backs of people of this personality type who welcome friends, family, and neighbors into their homes and hearts. This does not imply that Consuls are saints or that they are tolerant of all people.However, consuls have a tendency to feel a feeling of obligation to those around them and do believe in the power of hospitality and politeness.Generous and trustworthy, those who fit this personality type frequently take it upon themselves to keep their families and communities together in both big and small ways.",
            # Virtuoso
            "ISTPA": "Virtuosos enjoy exploring and examining their surroundings with a combination of enthusiastic curiosity and logic and rationality. This personality type is naturally creative, jumping from project to project, creating the required and superfluous just for pleasure, and absorbing information from their surroundings. They investigate concepts through creation, problem-solving, trial and error, and first-hand experience. They take pleasure in having others show an interest in their work and occasionally don't mind someone invading their personal space.Virtuosos take pleasure in helping others and imparting their knowledge, especially to those they care about. They frequently have an autonomousoutlook and pursue their goals with little help from others. They approach life with curiosity and individual skill, changing their strategy asnecessary.",
            "ISTJT": "Virtuosos enjoy exploring and examining their surroundings with a combination of enthusiastic curiosity and logic and rationality. This personality type is naturally creative, jumping from project to project, creating the required and superfluous just for pleasure, and absorbing information from their surroundings. They investigate concepts through creation, problem-solving, trial and error, and first-hand experience. They take pleasure in having others show an interest in their work and occasionally don't mind someone invading their personal space.Virtuosos take pleasure in helping others and imparting their knowledge, especially to those they care about. They frequently have an autonomousoutlook and pursue their goals with little help from others. They approach life with curiosity and individual skill, changing their strategy asnecessary.",
            # Adventure
            "ISFPA": "Adventurers are real artists, but perhaps not always in the traditional sense. Life itself serves as the canvas for this personality type's artistic expression. They behave in a way that vividly reflects who they are as distinct individuals, from what they wear to how they use their free time.And each Adventurer is undoubtedly different. People with this mentality tend to have a wide variety of passions and interests since they are driven by curiosity and eager to experience new things.They typically embrace life, new experiences, and people with an open mind and a grounded friendliness. They discover intriguing possibilities thanksto their capacity for mindfulness. Adventurers might be among the most fascinating individuals you'll ever meet thanks to their curiosity and capacity for joy.",
            "ISFPT": "Adventurers are real artists, but perhaps not always in the traditional sense. Life itself serves as the canvas for this personality type's artistic expression. They behave in a way that vividly reflects who they are as distinct individuals, from what they wear to how they use their free time.And each Adventurer is undoubtedly different. People with this mentality tend to have a wide variety of passions and interests since they are driven by curiosity and eager to experience new things.They typically embrace life, new experiences, and people with an open mind and a grounded friendliness. They discover intriguing possibilities thanksto their capacity for mindfulness. Adventurers might be among the most fascinating individuals you'll ever meet thanks to their curiosity and capacity for joy.",
            # Entreprenuer
            "ESTPA": "The best way to identify an entrepreneur at a party is to look for the swirling whirlpool of individuals flying about them as they travel from group to group. Entrepreneurs always have an impact on their immediate surroundings. Entrepreneur personalities enjoy making people laugh and smile with their candid, down-to-earth humor. They also enjoy being the center of attention. Entrepreneurs offer to go on stage if requested, or they offer to bring a shy buddy.They keep the discourse lively and intelligent, yet they prefer to talk about the present rather than simply acting on it. Entrepreneurs don't wait around, planning backup plans and escape routes; they leap before they look and correct their flaws as they go.",
            "ESTPT": "The best way to identify an entrepreneur at a party is to look for the swirling whirlpool of individuals flying about them as they travel from group to group. Entrepreneurs always have an impact on their immediate surroundings. Entrepreneur personalities enjoy making people laugh and smile with their candid, down-to-earth humor. They also enjoy being the center of attention. Entrepreneurs offer to go on stage if requested, or they offer to bring a shy buddy.They keep the discourse lively and intelligent, yet they prefer to talk about the present rather than simply acting on it. Entrepreneurs don't wait around, planning backup plans and escape routes; they leap before they look and correct their flaws as they go.",
            # Entertainer
            "ESFPA": "The Entertainer personality type is the one most likely to break into song and dance on their own. When something exciting happens, entertainers become engrossed in it and want everyone else to share their excitement. When it comes to motivating others, no personality type gives as much of their time and energy as Entertainers do, and no personality type does it with such enticing style.These people like exciting adventures, live life to the fullest, and relish learning new things.",
            "ESFPT": "The Entertainer personality type is the one most likely to break into song and dance on their own. When something exciting happens, entertainers become engrossed in it and want everyone else to share their excitement. When it comes to motivating others, no personality type gives as much of their time and energy as Entertainers do, and no personality type does it with such enticing style.These people like exciting adventures, live life to the fullest, and relish learning new things.",
            # all ur 16 possible types
        }

        personality_list = {
            # Architect
            "INTJA": "ARCHITECT",
            "INTJT": "ARCHITECT",
            # Logician
            "INTPA": "LOGICIAN",
            "INTPT": "LOGICIAN",
            # Commander
            "ENTJA": "COMMANDER",
            "ENTJT": "COMMANDER",
            # Debator
            "ENTPA": "DEBATOR",
            "ENTPT": "DEBATOR",
            # Advocate
            "INFJA": "ADVOCATE",
            "INFJT": "ADVOCATE",
            # Mediator
            "INFPA": "MEDIATOR",
            "INFPT": "MEDIATOR",
            # Protagonist
            "ENFJA": "PROTAGONIST",
            "ENFJT": "PROTAGONIST",
            # Campaigner
            "ENFPA": "CAMPAIGNER",
            "ENFPT": "CAMPAIGNER",
            # Logistician
            "ISTJA": "LOGISTICIAN",
            "ISTJT": "LOGISTICIAN",
            # Defender
            "ISFJA": "DEFENDER",
            "ISFJT": "DEFENDER",
            # Executive
            "ESTJA": "EXECUTIVE",
            "ESTJT": "EXECUTIVE",
            # Consul
            "ESFJA": "CONSULTANT",
            "ESFJT": "CONSULTANT",
            # Virtuoso
            "ISTPA": "VIRTUOSO",
            "ISTJT": "VIRTUOSO",
            # Adventure
            "ISFPA": "ADVENTURE",
            "ISFPT": "ADVENTURE",
            # Entreprenuer
            "ESTPA": "ENTREPRENUER",
            "ESTPT": "ENTREPRENUER",
            # Entertainer
            "ESFPA": "ENTERTAINER",
            "ESFPT": "ENTERTAINER",
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
        if self.answers[3:6].count(0) >= 2:
            print("Observant - [S]!")
            personality.append("S")
        else:
            print("Intuitive - [N]!")
            personality.append("N")

        # 3 Thinking - Feeling
        if self.answers[6:9].count(0) >= 2:
            print("Feeling - [F]!")
            personality.append("F")
        else:
            print("Thinking - [T]!")
            personality.append("T")

        # 4 Judging - Prospecting
        if self.answers[9:12].count(0) >= 2:
            print("Judging - [J]!")
            personality.append("J")
        else:
            print("Prospecting - [P]!")
            personality.append("P")

        # 5 Assertive - Turbulent
        if self.answers[12:15].count(0) >= 2:
            print("Turbulent - [T]!")
            personality.append("T")
        else:
            print("Assertive - [A]!")
            personality.append("A")

        personality_str = "".join(personality)
        personality_desc = personality_descriptions[personality_str]
        personality_name = personality_list[personality_str]
        print(personality)
        print(personality_str)
        print(f"Your personality is {personality_str}")
        print(personality_name)
        print(personality_desc)

        # GUI Design of the page
        self.title("Result!")

        self.img4 = ImageTk.PhotoImage(Image.open("Images/FinalFrame.png"))
        self.img_label1 = tk.Label(self, image=self.img4)
        self.img_label1.pack()
        self.geometry("1000x768")
        self.font1 = ('arial',80)
        self.font2 = ('arial',24)

        self.TextBox1 = tk.Text(self,font=self.font1, height=1, width=15,wrap=tk.WORD,fg="black", bg="#C1E7E3")
        self.TextBox1.place(x=230,y=300)
        self.TextBox1.insert(tk.END,personality_name)

        self.TextBox2 = tk.Text(self,font=self.font2, height=10, width=50,wrap=tk.WORD,fg="black", bg="#E6FCFA")
        self.TextBox2.place(x=130,y=425)
        self.TextBox2.insert(tk.END,personality_desc)
    

        


if __name__ == "__main__":
    app = App("questions", "options", "answers")
    app.mainloop()
