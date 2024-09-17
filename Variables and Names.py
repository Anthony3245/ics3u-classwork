# team is storing the text "Toronto Blue Jays"
team = "Toronto Blue Jays"
# current_date is storing the text" July 18,2021"
current_date = "July 18, 2021"
# player is storing the text Vladimir Guerrero Jr.
player = "Vladimir Guerrero Jr."
# home_runs_to_date is storing the interger 31
home_runs_to_date = 31
# games_played is storing the interger 88 
games_played = 88
# total_season_games is storing the interger 162 
total_season_games = 162
# home_run_record is storing the interger 73
home_run_record = 73
#games_remaining is storing 162-88 = 74
games_remaining = total_season_games - games_played
# games_remaining is storing 31/88 which is about 0.35
home_runs_per_game = round((home_runs_to_date / games_played),2)
# projected_home_runs is storing 0.35 * 162 which is about 56.7
projected_home_runs = round((home_runs_per_game * total_season_games),2)
# can_break_record is storing that its false that he will break the home run record
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {home_runs_per_game} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {projected_home_runs} home runs this season.")
