from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 14, "italic")


class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.quiz = quiz_brain
        self.canva = Canvas(bg='white', height=250, width=300)
        self.question_text = self.canva.create_text(150, 125, font=FONT, fill=THEME_COLOR,width=280)
        
        self.canva.grid(column=0, columnspan=2, row=1, padx=20, pady=20)
        correct_image = PhotoImage(file=r'images\true.png')
        wrong_image = PhotoImage(file=r'images\false.png')

        self.correct_button = Button(image=correct_image, highlightthickness=0,command=self.true_pressed)
        self.correct_button.grid(column=0, row=2, padx=20, pady=20)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)

        self.scoretext = Label(font=FONT,bg=THEME_COLOR, fg='white')
        self.scoretext.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg='white')
        if self.quiz.still_has_questions():
            self.scoretext.config(text =f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text,text = q_text)
        else:
            self.canva.itemconfig(self.question_text,text="You have completed the Quiz.")
            self.correct_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canva.config(bg='green')
        else:
            self.canva.config(bg='red')
        self.window.after(1000,self.get_next_question)