import random as rand

MAX_BET = 2000
MAX_WIN = 2000
MAX_LOSE = -2000


def play_roulette(bet_amount, win_percent=.4637, reward_odds=2):
    win = win_percent < rand.random()
    reward = win * bet_amount * reward_odds
    return [win, reward]


def martingale_roulette(initial_bet, current_winnings):
    current_bet = initial_bet
    iterations = 0
    win_martingale = False
    while current_winnings < MAX_WIN and current_winnings > MAX_LOSE and current_bet < MAX_BET:
        current_winnings -= current_bet
        [win, reward] = play_roulette(current_bet)
        iterations += 1
        current_winnings += reward
        if win:
            win_martingale = True
            break
        else:
            current_bet *= 2
    return [current_winnings, win_martingale, iterations]


def run_simulation(initial_bet, current_winnings=0):
    simulation_timeline = []
    games_played = 0
    while current_winnings < MAX_WIN and current_winnings > MAX_LOSE:
        [current_winnings, win, iterations] = martingale_roulette(initial_bet, current_winnings)
        simulation_timeline.append([win, iterations])
        games_played += 1
    return [current_winnings, games_played, current_winnings >= MAX_WIN, simulation_timeline]


def run_simulations(initial_bet, num_of_simulations):
    total_wins = 0
    total_winnings = 0
    total_games_played = 0
    for i in range(num_of_simulations):
        [final_winnnings, games_played, win, simulation_timeline] = run_simulation(initial_bet)
        total_wins += win
        total_winnings += final_winnnings
        total_games_played += games_played
    chance_to_win = total_wins * 1.0 / num_of_simulations
    average_return = total_winnings * 1.0 / num_of_simulations
    average_games_played = total_games_played * 1.0 / num_of_simulations
    return [chance_to_win, average_return, average_games_played]




if __name__ == '__main__':
    initial_bet = 100
    number_of_simulations = 10
    print("Running {} simluations".format(number_of_simulations))
    [chance_to_win, average_return, average_games_played] \
        = run_simulations(initial_bet, number_of_simulations)
    print("Ran {} simulations. \n"
          "Won {} percent of the time. \n"
          "Average Return is {}. \n"
          "Average number of games played {}".format(number_of_simulations,
                                                     chance_to_win * 100,
                                                     average_return,
                                                     average_games_played))
