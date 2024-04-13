#########################
########
#Tashi Dorji
#BE ELECTRICAL ENGG. 1YEAR
#02230083
##########################
#######
#REFERANCE
#@CHAT_GPT
#@GEMINI_AI
#@DQ_LOGO
##########################
########
#SOLUTION
# My solution:49801
#02230082
#input_2_cap1.txt()
##########################
#######

def read_input(file_name):
    #Reads the game data from a file.
    
    rounds = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                opponent_play, outcome = line.strip().split()  # Remove leading/trailing spaces
                rounds.append((opponent_play, outcome))
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return rounds

def calculate_score(rounds):
    score = 0
    for opponent_play, outcome in rounds:
        if outcome == 'X':
            if opponent_play == 'A':
                score += 3
            elif opponent_play == 'B':
                score += 1
            elif opponent_play == 'C':
                score += 2
        elif outcome == 'Y':
            if opponent_play == 'A':
                score += 4
            elif opponent_play == 'B':
                score += 5
            elif opponent_play == 'C':
                score += 6
        elif outcome == 'Z':
            if opponent_play == 'A':
                score += 8
            elif opponent_play == 'B':
                score += 9
            elif opponent_play == 'C':
                score += 7
    print(f"The total score is: {score}")

# To run the code:
file_name = "input_2_cap1.txt"
calculate_score(read_input(file_name))

