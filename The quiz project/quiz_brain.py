class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    
    
    def still_has_questions(self):
        return self.question_number<len(self.question_list)           #saving if else block since computer automatically evaluates 5>3 as True and 3>5 as false and given boolean (true or false) output 
                                                                        # if self.question_number>=12:
                                                                        #     return False
                                                                        # else:
                                                                        #     return True                                                                        
    def next_question(self):
        current_que=self.question_list[self.question_number]   #in our que bank list all items are in form of objects
        question=current_que.question
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}:{question}\n what is your answer? True/False: ").capitalize()
        self.check_answer(user_answer,current_que.answer)   #since in our que bank each item is in form of object made from question class we can access attribute 'answer' by tapping into each object.
        
    def check_answer(self,user_answer,correct_ans):
        if correct_ans==user_answer:
            self.score+=1
            print(f"Your answer was correct.\nCurrent Score:{self.score}/{self.question_number}")
        else:
            print(f"Wrong Answer.\nCurrent Score:{self.score}/{self.question_number}")
        print(f"The correct answer was {correct_ans}")
        print("\n")