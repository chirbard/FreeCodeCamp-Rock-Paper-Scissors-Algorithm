import random

def reset_history_after_1000_games(opponent_history):
    if len(opponent_history) > 3000:
        return opponent_history[3000:]
    if len(opponent_history) > 2000:
        return opponent_history[2000:]
    if len(opponent_history) > 1000:
        return opponent_history[1000:]
    return opponent_history

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    opponent_history = reset_history_after_1000_games(opponent_history)
    
    history_string = ''.join(opponent_history)
    history_length = len(history_string)

    number_of_moves_to_inspect = 5

    if history_length == 0:
        return 'S'
    if history_length == 1:
        return 'R'
    if history_length < number_of_moves_to_inspect:
        return 'S'

    opponent_last_moves = history_string[-number_of_moves_to_inspect:]
    number_of_occurrences = history_string[:-1].count(opponent_last_moves)
    if number_of_occurrences == 0:
        return 'S'

    exceeding_char_occurances_in_history = {
        "R": 0,
        "P": 0,
        "S": 0 
    }
    last_loop_index = 0
    for i in range(number_of_occurrences):
        case_start_index = history_string.find(opponent_last_moves, last_loop_index)
        last_loop_index = case_start_index
        exceeding_char = history_string[case_start_index + number_of_moves_to_inspect]
        exceeding_char_occurances_in_history[exceeding_char] += 1
    
    exceeding_char_probabilities = {
        "R": 0.0,
        "P": 0.0,
        "S": 0.0 
    }
    for key in exceeding_char_occurances_in_history:
        probability = exceeding_char_occurances_in_history[key]/number_of_occurrences
        exceeding_char_probabilities[key] = probability

    max_key = max(exceeding_char_probabilities, key=exceeding_char_probabilities.get)
    best_match = {'R': 'P', 'P': 'S', 'S': 'R'}
    return best_match[max_key]
