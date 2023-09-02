import tkinter as tk
from tkinter import Radiobutton
from tkinter import messagebox
class QuizApp:
    def __init__(self):
        self.quiz = [ {
            "Question" : "Which planet is known as the Red Planet?",
            "Options": ["Venus","Mars","Saturn","Jupiter"],
            "answer" : 1
                },
                {
            "Question" : "Who wrote the famous play Romeo and Juliet?",
            "Options" : ["William Shakespeare","Jane Austen","Charles Dickens","Mark Twain"],
            "answer": 0
                },
                {
           "Question" : "What is the chemical symbol for water?",
            "Options" : ["WO","HO","H2O","O2H"],
            "answer": 2
                },
                {
            "Question": "Which mammal can fly and navigate using echolocation?",
            "Options" : ["Bat","Squirrel","Fox","Rabbit"],
            "answer": 0
                },
                {
            "Question": "What is the capital city of Japan?",
            "Options": ["Tokyo","Beijing","Seoul","Bangkok"],
            "answer": 0
                }]
        
        self.current_Qindex = 0
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Quiz Questions")

        self.Qlabel = tk.Label(self.window, text="", font=("Open Sans", 18))
        self.Qlabel.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="w")

        self.options_frame = tk.Frame(self.window)
        self.options_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="w")

        self.Options=[]
        self.selected_option = tk.IntVar()
        for i in range(4):
            option = Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value=i,
                command=self.check,
                font=("Open Sans", 12)  # Set the font for the option text
            )
            option.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            self.Options.append(option)

        self.answered = [False] * len(self.quiz)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=20, command=self.nextQ)
        self.next_question_button.grid(row=2, column=0, padx=20, pady=15, sticky="w")

    def start(self):
        self.loadQ()
        self.window.mainloop()

    def check(self):
        if self.answered[self.current_Qindex]:
            messagebox.showerror("Already Answered", "You've already answered this question.")
            return

        selected = self.selected_option.get()

        if selected == -1:
            messagebox.showerror("No Answer", "Please select an answer.")
            return

        self.answered[self.current_Qindex] = True
        answer = self.quiz[self.current_Qindex]["answer"]

        if selected == answer:
            self.score += 1
            messagebox.showinfo("Correct", "You're right")
        else:
            self.score -= 0.25
            messagebox.showerror("Incorrect", "Your answer is Incorrect")

        for option in self.Options:
            option.config(state=tk.DISABLED)
        self.next_question_button.config(state=tk.NORMAL)

    def loadQ(self):
        Qdata = self.quiz[self.current_Qindex]
        self.Qlabel.config(text = Qdata["Question"])
        Options = Qdata["Options"]
        for i in range(4):
            self.Options[i].config(text=Options[i], state=tk.NORMAL)
        self.selected_option.set(-1)

    def nextQ(self):
        self.current_Qindex+= 1
        if self.current_Qindex == len(self.quiz):
            messagebox.showinfo("You have completed the Quiz", f" Your score : {self.score}/{len(self.quiz)}")
            self.window.destroy()
        else:
            self.loadQ()

cysec_quiz = QuizApp()
cysec_quiz.start()