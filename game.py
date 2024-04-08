import random
import math
from pprint import pprint

TIMESTAMPS_COUNT = 10

PROBABILITY_SCORE_CHANGED = 0.5

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    if not isinstance(offset, int) or offset < 0:
        return "Invalid offset. Offset should be a number greater than or equal to 0."

    max_offset = game_stamps[-1]['offset']
    if offset > max_offset:
        return f"The score is {game_stamps[-1]['score']['home']}:{game_stamps[-1]['score']['away']} at the end of the game"

    current_offset = None
    for item in game_stamps:
        if item['offset'] <= offset:
            current_offset = item
        else:
            break
    return current_offset['score']['home'], current_offset['score']['away']




