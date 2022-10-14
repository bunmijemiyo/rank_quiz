"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.

Example
scores = [12,24, 10, 24]

Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
Given the scores for a season, determine the number of times Maria breaks her records for most
and least points scored during the season.

Function Description
Complete the breakingRecords function in the editor below.
breakingRecords has the following parameter(s):
int scores[n]: points scored per game

Returns
int[2]: An array with the numbers of times she broke her records. 
Index 0 is for breaking most points records, and index 1 is for breaking least points records.

Input Format
The first line contains an integer n, the number of games.
The second line contains  space-separated integers describing the respective values of score1,
score2,... score n-1
"""


def breakingRecords(scores):
    # Write your code here
    # set max and min score to the score of game 1
    max_score, min_score = scores[0], scores[0]
    records = [0, 0]
    
    # iterate thr no_rep to find records
    for score in scores[1:]:
        if score > max_score:
            records[0] += 1
            max_score = score
            
        elif score < min_score:
            records[1] += 1
            min_score = score
    return records


scores = [12,24, 10, 24]

print(breakingRecords(scores))
