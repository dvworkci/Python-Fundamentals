from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n (b) Purple\n (c) Orange (d) Black\n\n",
    "What color are bananas?\n (a) Teal (b) Yellow (c) Orange (d) Blue\n\n",
    "What color are strawberries?\n (a) Yellow (b) Green (c) Red (d) White\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if(answer == question.answer):
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)