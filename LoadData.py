import pandas as pd
import os
import csv
import sys
import numpy as np
from CardObject import *


def get_persistent_path(filename):
    # Save in user's home directory under a folder "LittleAlchemist"
    base_path = os.path.join(os.path.expanduser("~"), "LittleAlchemist")
    os.makedirs(base_path, exist_ok=True)  # Create folder if it doesn’t exist
    return os.path.join(base_path, filename)


def initial_load_data(filename):
    # Check if running in a PyInstaller bundle
    if getattr(sys, 'frozen', False):
        # If in a bundle, get the directory where the app is running
        base_path = sys._MEIPASS
    else:
        # If running in a normal Python environment, use the current working directory
        base_path = os.path.dirname(__file__)
    filename = os.path.join(base_path, filename)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    df_result = pd.read_excel(filename)
    selected_columns = df_result[['CC_A', 'CC_B', 'Res', 'Res_Rare', 'BA_0O', 'BD_0O']]
    data_as_list = selected_columns.iloc[0:].values.tolist()
    base_cards = set()
    combos = set()
    resulting_combo = dict()
    for combination in data_as_list:
        combo_card = combination[0]
        result = combination[2]
        if combo_card not in combos:
            combos.add(combo_card)
        if result not in resulting_combo:
            resulting_combo[result] = Card(combination[4], combination[5], combination[3])
        if combo_card not in base_cards:
            base_cards.add(combo_card)
        if result not in base_cards:
            base_cards.add(result)
    return resulting_combo, combos, base_cards, data_as_list


def second_load_data(filename, combo_cards, base_card_stats):
    # Check if running in a PyInstaller bundle
    if getattr(sys, 'frozen', False):
        # If in a bundle, get the directory where the app is running
        base_path = sys._MEIPASS
    else:
        # If running in a normal Python environment, use the current working directory
        base_path = os.path.dirname(__file__)
    filename = os.path.join(base_path, filename)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df_result = pd.read_excel(filename)
    selected_columns = df_result[['C_Name', 'C_Rare', 'C_Atk', 'C_Def']]
    filtered = selected_columns.dropna(subset=['C_Name', 'C_Rare', 'C_Atk', 'C_Def'])
    base_cards_as_list = filtered.values.tolist()

    combo_card_stats = dict()
    for card in base_cards_as_list:
        name = card[0]
        if name in combo_cards:
            combo_card_stats[name] = ComboCard(card[2], card[3], determineRarity(card[1]))
            if name not in base_card_stats:
                base_card_stats[name] = Card(card[2], card[3], determineRarity(card[1]))
        else:
            if name not in base_card_stats:
                base_card_stats[name] = Card(card[2], card[3], determineRarity(card[1]))

    return combo_card_stats, base_card_stats


def third_load_data(data_as_list, combo_card_stats):
    for combination in data_as_list:
        combo_card_1 = combination[0]
        combo_card_2 = combination[1]
        result = combination[2]
        combo_card_stats[combo_card_1].addCombo(combo_card_2, result)
        combo_card_stats[combo_card_2].addCombo(combo_card_1, result)

    return combo_card_stats


def add_onyx_combos(combo_card_names, combo_cards):
    card_names = list(combo_card_names)
    for i in range(0, len(card_names)):
        onyx_name = card_names[i] + ":Onyx"
        combo_card_names.add(onyx_name)
        attack = combo_cards[card_names[i]].attack
        defense = combo_cards[card_names[i]].defense
        rarity = combo_cards[card_names[i]].rarity
        if rarity == 3:
            attack = attack + 2
            defense = defense + 2
        elif rarity == 2:
            attack = attack + 3
            defense = defense + 3
        elif rarity == 1:
            attack = attack + 4
            defense = defense + 4
        combo_cards[onyx_name] = ComboCard(attack, defense, 5)
        combo_cards[onyx_name].setCombinations(combo_cards[card_names[i]].combinations)
        names_list = list(combo_cards[card_names[i]].combinations.keys())
        result_list = list(combo_cards[card_names[i]].combinations.values())
        for j in range(0, len(names_list)):
            x = names_list[j] + ":Onyx"
            combo_cards[card_names[i]].addCombo(x, result_list[j])
        names_list = list(combo_cards[onyx_name].combinations.keys())
        result_list = list(combo_cards[onyx_name].combinations.values())
        for j in range(0, len(names_list)):
            x = names_list[j] + ":Onyx"
            combo_cards[onyx_name].addCombo(x, result_list[j])
    return combo_card_names, combo_cards


def load_user_library():
    user_library = []
    try:
        filename = get_persistent_path('user_card_library.txt')
        file = open(filename, 'r')
    except FileNotFoundError:
        print("User's card library does not exist")
        return user_library
    try:
        content = file.read()
        content = content.split('\n')
        for card in content:
            card_attributes = card.split("%next%")
            if len(card_attributes) == 4:
                try:
                    user_library.append(
                        [card_attributes[0], int(card_attributes[1]), card_attributes[2], int(card_attributes[3])])
                except ValueError:
                    user_library = False
                    break
                except IndexError:
                    user_library = False
                    break
                except TypeError:
                    user_library = False
                    break
    except IOError:
        user_library = False
    finally:
        file.close()

    return user_library


def save_user_library(user_library):
    filename = get_persistent_path('user_card_library.txt')
    file = open(filename, 'w')
    for card in user_library:
        file.write(card[0] + "%next%" + str(card[1]) + "%next%" + card[2] + "%next%" + str(card[3]))
        file.write("\n")
    file.close()
    return


def load_andersam_optimizer_library(filename):
    user_library = []
    try:
        df = pd.read_excel(filename, sheet_name='USER')
        result = df[['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']]
        result = result.iloc[0:].values.tolist()
        result = result[10:]
        for card in result:
            if type(card[0]) != float:
                user_library.append([card[0], int(card[1]), card[2], int(card[3])])
    except FileNotFoundError:
        user_library = False
    except KeyError:
        user_library = False
    except IndexError:
        user_library = False
    except TypeError:
        user_library = False
    except pd.errors.EmptyDataError:
        user_library = False
    except pd.errors.ParserError:
        user_library = False
    except ValueError:
        user_library = False
    except IOError:
        user_library = False
    return user_library


def save_user_deck(deck, deck_library, filename):
    deck_filename = get_persistent_path(filename + '.txt')
    deck_library_filename = get_persistent_path(filename + '_library.txt')
    deck_file = open(deck_filename, 'w')
    deck_library_file = open(deck_library_filename, 'w')
    for card in deck:
        deck_file.write(card[0] + "%next%" + str(card[1]) + "%next%" + card[2])
        deck_file.write("\n")
    deck_file.close()
    for card in deck_library:
        deck_library_file.write(card[0] + "%next%" + str(card[1]) + "%next%" + card[2] + "%next%" + str(card[3]))
        deck_library_file.write("\n")
    deck_library_file.close()
    return


def load_user_deck(filename):
    deck = []
    deck_library = []
    deck_filename = get_persistent_path(filename + '.txt')
    deck_library_filename = get_persistent_path(filename + '_library.txt')
    try:
        deck_file = open(deck_filename, 'r')
        deck_library_file = open(deck_library_filename, 'r')
    except FileNotFoundError:
        print(f"User's card library does not exist for {filename}")
        return [], []
    try:
        content = deck_file.read()
        content = content.split('\n')
        for card in content:
            card_attributes = card.split("%next%")
            if len(card_attributes) == 3:
                try:
                    deck.append(
                        [card_attributes[0], int(card_attributes[1]), card_attributes[2]])
                except ValueError:
                    deck = False
                    break
                except IndexError:
                    deck = False
                    break
                except TypeError:
                    deck = False
                    break
    except IOError:
        deck = False
    finally:
        deck_file.close()

    try:
        content = deck_library_file.read()
        content = content.split('\n')
        for card in content:
            card_attributes = card.split("%next%")
            if len(card_attributes) == 4:
                try:
                    deck_library.append(
                        [card_attributes[0], int(card_attributes[1]), card_attributes[2], int(card_attributes[3])])
                except ValueError:
                    deck_library = False
                    break
                except IndexError:
                    deck_library = False
                    break
                except TypeError:
                    deck_library = False
                    break
    except IOError:
        deck_library = False
    finally:
        deck_library_file.close()
    return deck, deck_library


def export_deck_csv(filename, directory, deck, deck_names, deck_statistics):
    filename = filename + '.csv'
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Deck Statistics:"])
        writer.writerow([""] + deck_names)
        lvl_average = 0
        fused_average = 0
        ts_average = 0
        a_average = 0
        d_average = 0
        for i in range(0, len(deck)):
            lvl_average += deck[i][1]
            if deck[i][2] == "Yes": fused_average += 1
            ts_average += deck[i][3]
            a_average += deck[i][4]
            d_average += deck[i][5]
        for row, data in zip(deck_names, deck_statistics):
            writer.writerow([row] + data)

        # Write 5 empty rows to create a gap
        for _ in range(4):
            writer.writerow([])
        writer.writerow(["Deck:"])

        writer.writerow(["", "Level", "Fusion", "Average Total Stat", "Average Attack", "Average Defense"])
        for row in deck:
            writer.writerow(row)
        writer.writerow(["Averages", str(float(lvl_average)/len(deck)), str(float(fused_average)/len(deck)),
                         str(float(ts_average) / len(deck)), str(float(a_average) / len(deck)),
                         str(float(d_average) / len(deck))])
    return


def export_simulation_results_csv(filename, directory, test_deck, simulation_results):
    filename = filename + '.csv'
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Deck:"])
        writer.writerow(["Cards"] + [str(i+1) for i in range(len(test_deck))])

        writer.writerow(["Card Name"] + [card[0] for card in test_deck])
        writer.writerow(["Level"] + [str(card[1]) for card in test_deck])
        writer.writerow(["Fusion"] + [card[2] for card in test_deck])

        # Write 5 empty rows to create a gap
        for _ in range(4):
            writer.writerow([])

        writer.writerow(["Simulation Results:"])
        writer.writerow(["Turns"] + [str(i + 1) for i in range(len(simulation_results))])

        temp_ts = []
        temp_atk = []
        temp_def = []
        temp_orbs = []
        temp_health = []
        temp_percentage = []
        for i in range(0, len(simulation_results)):
            temp_ts.append(simulation_results[i][0][1])
            temp_atk.append(simulation_results[i][1][1])
            temp_def.append(simulation_results[i][2][1])
            temp_orbs.append(simulation_results[i][3][1])
            temp_health.append(simulation_results[i][4][1])
            temp_percentage.append(simulation_results[i][5][1])
        overall = [temp_ts, temp_atk, temp_def, temp_orbs, temp_health, temp_percentage]
        for i in range(0, len(overall)):
            for j in range(0, len(overall[i])):
                overall[i][j] = str(overall[i][j])

        result_labels = ["Average TS", "Average Atk", "Average Def", "Average Orbs", "Average Health", "% No Combo"]
        for i, label in enumerate(result_labels):
            writer.writerow([label] + overall[i])

