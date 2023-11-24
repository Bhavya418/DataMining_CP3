# DataMining_CP3 - ICC WORLD CUP PREDICTION

# Overview of the project 
> This project is about the prediction of the ICC Cricket World 2023. It provides a statistical analysis of different details about the ICC Cricket World Cup 2023.

# Installation
> To run the model on your local machine,
> 1. Clone the repository
> 2. Install the Python notebooks and required datasets
> 3. Run the file main.py and open localhost:7000 in the browser


# Task 1

Problem 1:

We have used the following datasets:
1. deliveries.csv
2. other data were scraped from the ESPN's website the URLs are given below:
   - 'https://www.espncricinfo.com/records/tournament/bowling-best-career-economy-rate/icc-cricket-world-cup-2023-24-15338'
   - 'https://www.espncricinfo.com/records/tournament/batting-highest-career-batting-average/icc-cricket-world-cup-2023-24-15338'

Features :

match_id: A unique identifier for each cricket match. Each match would have a different match_id.

season: The season in which the cricket match was played. In cricket, seasons are often defined by the year or specific tournament seasons.

start_date: The date when the cricket match took place.

venue: The location or stadium where the match was played.

innings: Represents the innings of the match (first innings, second innings, etc.). Cricket matches consist of multiple innings for each team.

ball: Indicates the ball number within an over during the match. It could range from 1 to 6 in a standard cricket over.

batting_team: The team that is currently batting during the specified ball.

bowling_team: The team that is currently bowling during the specified ball.

striker: The batsman who is currently facing the ball.

non_striker: The batsman who is at the non-striker end (not facing the ball).

bowler: The player who is currently bowling the ball.

runs_off_bat: The number of runs scored by the batsman off the bat (without extras like wides, no-balls, etc.).

extras: Extra runs scored in that particular ball, such as wides, no-balls, byes, leg-byes, and penalties.

wides: The number of wides bowled in that particular ball.

noballs: The number of no-balls bowled in that particular ball.

byes: Runs scored due to byes (when the ball goes past the batsman without touching the bat and no runs were scored).

legbyes: Runs scored as leg-byes (when the ball hits the batsman's body or gear).

penalty: Represents penalty runs awarded for various reasons during the match.

wicket_type: Describes the type of wicket taken in that ball (e.g., caught, bowled, lbw, etc.).

player_dismissed: Name of the player dismissed on that ball.

other_wicket_type: Additional information regarding the type of wicket (if applicable).

other_player_dismissed: Additional information regarding the player dismissed (if applicable).


And have joined the datasets as per the requirement.

In this task, we have trained the neural network.

a) Predicting the most dot balls by a batsman 

In this we have predicted the most dot balls played by a batsmen by using the regression method where we have taken and mapping the result of highest dot balls with the name to get the output.

b) Predicting the most dot balls by a bowler

In this we have predicted the most dot balls bowled by a bowler by using the regression method where we have taken and mapping the result of highest dot balls with the name to get the output


c) Predicting the most run scored by a batsman 
In this we have predicted the most runs scored by a batsmen by using the regression method where we have taken and mapping the result of highest dot balls with the name to get the output

# Task 2 

*Final Team Prediction* 

We have used the following datasets: 

1. deliveries.csv

2. matches.csv

3. players_list.csv

To generate the final teams, we have created the 3 models 
toss_decision.ipynb, run_prediction_innings_1.ipynb, run_prediction_innings_2.ipynb
for the 4 teams that have qualified into semi-finals and then based on the runs scored decided the final two teams 

Team 11 for the two final teams:

In this task, we have 

# Task 3 

  Winner Prediction
  
  We have used the following datasets: 

1. ICC_rankings.csv:

2. results.csv

3. world_cup_2023.csv

4. Fixtures.csv

Here, we have used the recent form of the teams where we have considered the results of the teams and their opponents with venue from 2019 and encoded them to predict the winner of the world cup

# Contributions 

Task 1 : 
 Naman Modi (202101421) and Yash Kodwani (202101418)

 Task 2,3 
 Bhavya Shah (202101426) and Vedant Shah (202101507)

 API Creation 
 Naman Modi (202101421), Yash Kodwani (202101418)
 Bhavya Shah (202101426), Vedant Shah (202101507)

 We have taken help from our batchmates
Sakshi Patadiya, Dhruv Shah
