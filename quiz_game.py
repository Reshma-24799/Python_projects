print("Welcome to my AI quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("1. Which of the following is a type of machine learning?\n"
               "A) Supervised Learning\nB) Unsupervised Learning\n"
               "C) Reinforcement Learning\nD) All of the above\nYour answer: ")
if answer.lower() == "d":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is D) All of the above.")

answer = input("2. What is the primary purpose of a neural network in AI?\n"
               "A) To store large amounts of data\nB) To simulate human brain functions for pattern recognition\n"
               "C) To manage databases efficiently\nD) To generate random numbers\nYour answer: ")
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is B) To simulate human brain functions for pattern recognition.")

answer = input("3. Which algorithm is commonly used for natural language processing (NLP)?\n"
               "A) Decision Trees\nB) Support Vector Machines\n"
               "C) Transformer Models\nD) K-Means Clustering\nYour answer: ")
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is C) Transformer Models.")

answer = input("4. In AI, what does 'GAN' stand for?\n"
               "A) General AI Network\nB) Generative Adversarial Network\n"
               "C) Graphical Artificial Neural\nD) Genetic Algorithm Network\nYour answer: ")
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is B) Generative Adversarial Network.")

answer = input("5. Which of the following is NOT a common application of AI?\n"
               "A) Fraud detection\nB) Image recognition\n"
               "C) Space travel\nD) Weather forecasting\nYour answer: ")
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is C) Space travel.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

