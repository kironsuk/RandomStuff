import random as rand
from matplotlib import pyplot as plt

MAX_BET = 2000
MAX_WIN = 2000
MAX_LOSE = -2000
BLACK_JACK_WIN_PERCENTAGE = .495


def play_roulette(bet_amount, win_percent=.4637, reward_odds=2):
    win = win_percent > rand.random()
    reward = win * bet_amount * reward_odds
    return [win, reward]


def martingale_roulette(initial_bet, current_winnings):
    current_bet = initial_bet
    iterations = 0
    win_martingale = False
    while current_winnings < MAX_WIN and current_winnings > MAX_LOSE and current_bet < MAX_BET:
        current_winnings -= current_bet
        [win, reward] = play_roulette(current_bet, BLACK_JACK_WIN_PERCENTAGE)
        iterations += 1
        current_winnings += reward
        if win:
            win_martingale = True
            break
        else:
            current_bet *= 2
    return [current_winnings, win_martingale, iterations]


def run_simulation(initial_bet, current_winnings=0, max_games_played=1000):
    simulation_timeline = []
    games_played = 0
    while current_winnings < MAX_WIN and current_winnings > MAX_LOSE:
        [current_winnings, win, iterations] = martingale_roulette(initial_bet, current_winnings)
        simulation_timeline.append([win, iterations])
        games_played += iterations
        if games_played > max_games_played:
            break
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

def find_best_initial_bet(possible_bets, num_of_simulations):
    results = []
    for bet in possible_bets:
        [chance_to_win, average_return, average_games_played] = run_simulations(bet, num_of_simulations)
        results.append([bet, chance_to_win, average_return, average_games_played])
    return results

def graph_best_inital_bet(possible_bets, num_of_simulations):
    results = find_best_initial_bet(possible_bets, num_of_simulations)
    chances = [result[1] for result in results]
    plt.xlabel("Initial Bet")
    plt.ylabel("Win Chance")
    plt.title('Win Chance with {} Simulations'.format(num_of_simulations))
    plt.plot(possible_bets, chances)
    plt.show()

    average_final_winnings = [result[2] for result in results]
    plt.xlabel("Initial Bet")
    plt.ylabel("Average Final Winnings ($)")
    plt.title('Average Winnings with {} Simulations'.format(num_of_simulations))
    plt.plot(possible_bets, average_final_winnings)
    plt.show()

    average_games_played = [result[3] for result in results]
    plt.xlabel("Initial Bet")
    plt.ylabel("Average Roulette Games Played")
    plt.yscale('log')
    plt.title('Average Games Played with {} Simulations'.format(num_of_simulations))
    plt.plot(possible_bets, average_games_played)
    plt.show()
    return results

if __name__ == '__main__':
    # initial_bet = 15
    number_of_simulations = 1000000
    print(run_simulations(15, number_of_simulations))
    # print("Running {} simluations".format(number_of_simulations))
    # [chance_to_win, average_return, average_games_played] \
    #     = run_simulations(initial_bet, number_of_simulations)
    # print("Ran {} simulations. \n"
    #       "Won {} percent of the time. \n"
    #       "Average Return is {}. \n"
    #       "Average number of games played {}".format(number_of_simulations,
    #                                                  chance_to_win * 100,
    #                                                  average_return,
    #                                                  average_games_played))

    possible_bets = [1, 2, 5, 10, 25, 50, 100, 150, 200]
    results = graph_best_inital_bet(possible_bets, number_of_simulations)
    # print("checking wins and loses ")
    # # print(run_simulation(50, 100000))
    # win_lose = []
    # wins = 0
    # for i in range(number_of_simulations):
    #     [win, reward] = play_roulette(initial_bet)
    #     wins += win

    # print("Win percentage ", (wins * 1.0 / number_of_simulations) );


