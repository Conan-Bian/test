"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""

TEAM_NAME = 'Bc' # Change this line!

def final_strategy(score, opponent_score):
    if score==0:
        return 6
    elif opponent_score==0:
        return 9
    elif score%opponent_score==0 :
        return 3
    elif opponent_score%score==0:
        return 8
    else:
        return 5