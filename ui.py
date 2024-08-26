from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.title("Think You Know?")
        self.window.configure(bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(padx=(20, 20), pady=(20, 20), row=1, column=0, columnspan=2)

        self.q_text = self.canvas.create_text(150, 125, width=280,
                                              text="Question", font=("Arial", 20, "italic"))

        self.score_label = Label(pady=20, bg=THEME_COLOR, text="Score: 0 ", fg="white")
        self.score_label.grid(row=0, column=1)

        check = PhotoImage(file="images/true.png")
        self.true = Button(image=check, borderwidth=0, highlightthickness=0, command=self.true_pressed)
        self.true.grid(row=2, column=0, pady=(20, 20))

        cross = PhotoImage(file="images/false.png")
        self.false = Button(image=cross, borderwidth=0, highlightthickness=0, command=self.false_pressed)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text=f"You've reached the end")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)






