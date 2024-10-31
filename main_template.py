import pandas as pd
import numpy as np
import random
import copy
import re
import wx
from DeckFrame import DeckFrame as DeckFrame
from OptimizeDeckFrame import OptimizeDeckFrame as OptimizeDeckFrame
from ExportCSVFrame import ExportCSVFrame as ExportCSVFrame
from TestDeckFrame import TestDeckFrame as TestDeckFrame
from CardObject import *
from LoadData import *


class LittleAlchemistAnalyst(DeckFrame):
    def __init__(self):
        super().__init__(None)
        self.frames = [self, OptimizeDeckFrame(None), TestDeckFrame(None)]
        self.export_csv_frame = ExportCSVFrame(None)

        # Loads all base and combo cards
        self.all_base_cards, self.all_combo_card_names, self.all_base_card_names, data = initial_load_data('LA_v5-06 '
                                                                                                           '300x60.xlsx')
        self.all_combo_cards, self.all_base_cards = second_load_data('Wiki-Card-Research_2.6.xlsx',
                                                                     self.all_combo_card_names, self.all_base_cards)
        self.all_combo_cards = third_load_data(data, self.all_combo_cards)

        self.all_combo_card_names, self.all_combo_cards = add_onyx_combos(self.all_combo_card_names,
                                                                          self.all_combo_cards)

        # Users Current Available Cards
        self.user_library = load_user_library()
        if self.user_library == False:
            wx.MessageBox("Incorrect or corrupted file", "Error Loading File", wx.OK | wx.ICON_ERROR)
            self.user_library = []

        self.current_deck = 1
        # Users Deck 1
        self.deck_1, self.deck_1_user_library = load_user_deck("deck_1")
        self.deck_stat_names_1 = [name[0] for name in self.deck_1]
        self.deck_stats_1 = [[0 for _ in range(len(self.deck_1))] for _ in range(len(self.deck_1))]
        for i in range(0, len(self.deck_1)):
            self.deck_1[i], self.deck_stats_1 = self.determine_statistics(i, self.deck_1, self.deck_stats_1)
        # Users Deck 2
        self.deck_2, self.deck_2_user_library = load_user_deck("deck_2")
        self.deck_stat_names_2 = [name[0] for name in self.deck_2]
        self.deck_stats_2 = [[0 for _ in range(len(self.deck_2))] for _ in range(len(self.deck_2))]
        for i in range(0, len(self.deck_2)):
            self.deck_2[i], self.deck_stats_2 = self.determine_statistics(i, self.deck_2, self.deck_stats_2)
        # Users Deck 3
        self.deck_3, self.deck_3_user_library = load_user_deck("deck_3")
        self.deck_stat_names_3 = [name[0] for name in self.deck_3]
        self.deck_stats_3 = [[0 for _ in range(len(self.deck_3))] for _ in range(len(self.deck_3))]
        for i in range(0, len(self.deck_3)):
            self.deck_3[i], self.deck_stats_3 = self.determine_statistics(i, self.deck_3, self.deck_stats_3)

        self.current_test_deck = 1
        # Users Test Deck 1
        self.test_deck_1 = copy.deepcopy(self.deck_1)
        self.simulation_1 = []

        # Users Test Deck 2
        self.test_deck_2 = copy.deepcopy(self.deck_2)
        self.simulation_2 = []

        # Users Test Deck 3
        self.test_deck_3 = copy.deepcopy(self.deck_3)
        self.simulation_3 = []

        self.sync_libraries()

        self.currently_optimizing = True

        self.initialise_frames()

        # Bind close and maximize events to all frames
        for frame in self.frames:
            frame.Bind(wx.EVT_CLOSE, self.on_close_all_frames)

        self.Show()

    def initialise_frames(self):
        self.card_library_button.Bind(wx.EVT_BUTTON, self.switch_to_deck_frame)
        self.optimized_deck_button.Bind(wx.EVT_BUTTON, self.switch_to_optimize_deck_frame)
        self.test_deck_button.Bind(wx.EVT_BUTTON, self.switch_to_test_deck_frame)

        # Background
        # Bind the EVT_PAINT event to draw the background image
        self.Bind(wx.EVT_PAINT, lambda event: self.OnPaint(event, self))
        self.Bind(wx.EVT_SIZE, lambda event: self.OnResize(event, self))

        self.initialise_deck_frame()
        self.initialise_optimize_frame()
        self.initialise_test_deck_frame()
        self.initialise_export_csv_frame()

        # Binds the buttons in the other frames
        for i, frame in enumerate(self.frames[1:], start=1):  # Skip the first frame (self)
            frame.Bind(wx.EVT_PAINT, lambda event: self.OnPaint(event, frame))
            frame.Bind(wx.EVT_SIZE, lambda event: self.OnResize(event, frame))
            frame.card_library_button.Bind(wx.EVT_BUTTON, self.switch_to_deck_frame)
            frame.optimized_deck_button.Bind(wx.EVT_BUTTON, self.switch_to_optimize_deck_frame)
            frame.test_deck_button.Bind(wx.EVT_BUTTON, self.switch_to_test_deck_frame)

    def initialise_deck_frame(self):
        self.card_name_choice.Set(self.card_names_list())
        self.card_level_choice.Set([str(i) for i in range(1, 6)])
        fusion_bool = ["Yes", "No"]
        self.fusion_choice.Set(fusion_bool)
        self.refresh_user_card_library_grid()
        self.refresh_delete_card_choice()

    def initialise_optimize_frame(self):
        self.frames[1].mode_choice.Set(['Total Stat', 'Attack', 'Defense', 'Custom'])
        self.refresh_add_card_choice(self.deck_1, self.deck_1_user_library)
        self.refresh_delete_card_from_deck_choice(self.deck_1)
        self.refresh_optimize_deck_grids(self.deck_1, self.deck_stat_names_1, self.deck_stats_1)
        self.frames[1].optimize_deck_button.Bind(wx.EVT_BUTTON, self.optimize_deck)
        self.frames[1].deck_1_button.Bind(wx.EVT_BUTTON, self.switch_to_deck_1)
        self.frames[1].deck_2_button.Bind(wx.EVT_BUTTON, self.switch_to_deck_2)
        self.frames[1].deck_3_button.Bind(wx.EVT_BUTTON, self.switch_to_deck_3)
        self.frames[1].add_card_to_deck_button.Bind(wx.EVT_BUTTON, self.add_card_to_deck)
        self.frames[1].delete_card_from_deck_button.Bind(wx.EVT_BUTTON, self.delete_card_from_deck)
        self.frames[1].clear_deck_button.Bind(wx.EVT_BUTTON, self.clear_deck)
        self.frames[1].save_deck_button.Bind(wx.EVT_BUTTON, self.save_deck)
        self.frames[1].export_decks_button.Bind(wx.EVT_BUTTON, self.switch_to_export_csv_frame_deck)

    def initialise_test_deck_frame(self):
        self.frames[2].ability_choice.Set(["Pierce", "Crushing Blow", "Block", "Protection", "Reflect",
                                           "Counter Attack", "Siphon", "Absorb", "Amplify", "Critical Strike",
                                           "Weaken", "Curse", "Pillage", "Plunder"])
        self.frames[2].mode_choice.Set(["Total Stat", "Attack", "Defense"])
        self.frames[2].final_preference_choice.Set(["Total Stat", "Attack", "Defense", "Health"])
        self.frames[2].level_choice.Set(["1", "2", "3", "4", "5"])
        self.frames[2].fusion_choice.Set(["Yes", "No"])
        self.refresh_test_deck_grids(self.deck_1, [])
        self.frames[2].deck_1_button.Bind(wx.EVT_BUTTON, self.switch_to_test_deck_1)
        self.frames[2].deck_2_button.Bind(wx.EVT_BUTTON, self.switch_to_test_deck_2)
        self.frames[2].deck_3_button.Bind(wx.EVT_BUTTON, self.switch_to_test_deck_3)
        self.frames[2].add_final_button.Bind(wx.EVT_BUTTON, self.add_final_form)
        self.frames[2].remove_final_button.Bind(wx.EVT_BUTTON, self.remove_final_form)
        self.frames[2].simulation_button.Bind(wx.EVT_BUTTON, self.simulate_deck)
        self.frames[2].export_csv_button.Bind(wx.EVT_BUTTON, self.switch_to_export_csv_frame_deck)

    def initialise_export_csv_frame(self):
        self.export_csv_frame.cancel_button.Bind(wx.EVT_BUTTON, self.close_export_csv_frame)
        self.export_csv_frame.save_button.Bind(wx.EVT_BUTTON, self.save_csv)

    def save_csv(self, event):
        filename = self.export_csv_frame.csv_filename_txtctrl.GetValue()
        if filename == "":
            wx.MessageBox("Proper filename required", "Error", wx.OK | wx.ICON_ERROR)
            return
        directory = self.export_csv_frame.directory_picker.GetPath()
        if directory == "":
            wx.MessageBox("Proper directory required", "Error", wx.OK | wx.ICON_ERROR)
            return
        if self.currently_optimizing:
            if self.current_deck == 1:
                export_deck_csv(filename, directory, self.deck_1, self.deck_stat_names_1, self.deck_stats_1)
            elif self.current_deck == 2:
                export_deck_csv(filename, directory, self.deck_2, self.deck_stat_names_2, self.deck_stats_2)
            else:
                export_deck_csv(filename, directory, self.deck_3, self.deck_stat_names_3, self.deck_stats_3)
        else:
            if self.current_test_deck == 1:
                export_simulation_results_csv(filename, directory, self.test_deck_1, self.simulation_1)
            elif self.current_test_deck == 2:
                export_simulation_results_csv(filename, directory, self.test_deck_2, self.simulation_2)
            else:
                export_simulation_results_csv(filename, directory, self.test_deck_3, self.simulation_3)
        wx.MessageBox("CSV File Created", "Success", wx.OK | wx.ICON_INFORMATION)
        self.export_csv_frame.Hide()

    def refresh_user_card_library_grid(self):
        self.card_library_grid.ClearGrid()
        self.set_rows_cols(self, self.card_library_grid, 3, len(self.user_library))

        # Set column labels
        self.card_library_grid.SetColLabelValue(0, "Level")
        self.card_library_grid.SetColLabelValue(1, "Fusion")
        self.card_library_grid.SetColLabelValue(2, "Amount")

        card_names = []
        for card in self.user_library:
            card_names.append(card[0])

        # Populate grid with nutrient field names and values
        for row, field in enumerate(card_names):
            self.card_library_grid.SetRowLabelValue(row, field)
        # Populate the grid with the array data
        for row, data in enumerate(self.user_library):
            for col, value in enumerate(data[1:]):
                self.card_library_grid.SetCellValue(row, col, str(value))

        self.card_library_grid.SetRowLabelSize(150)
        self.card_library_grid.ForceRefresh()
        self.Layout()

    def refresh_optimize_deck_grids(self, deck, deck_statistics_names, deck_statistics):
        self.frames[1].deck_summary_grid.ClearGrid()
        self.frames[1].deck_statistics_grid.ClearGrid()
        self.set_rows_cols(self.frames[1], self.frames[1].deck_summary_grid, 5, len(deck))
        self.set_rows_cols(self.frames[1], self.frames[1].deck_statistics_grid, len(deck_statistics_names),
                           len(deck_statistics_names))
        # Set column labels
        self.frames[1].deck_summary_grid.SetColLabelValue(0, "Level")
        self.frames[1].deck_summary_grid.SetColLabelValue(1, "Fusion")
        self.frames[1].deck_summary_grid.SetColLabelValue(2, "Avg TS")
        self.frames[1].deck_summary_grid.SetColLabelValue(3, "Avg Atk")
        self.frames[1].deck_summary_grid.SetColLabelValue(4, "Avg Def")

        for i, field in enumerate(deck_statistics_names):
            self.frames[1].deck_statistics_grid.SetColLabelValue(i, field)
            self.frames[1].deck_statistics_grid.SetRowLabelValue(i, field)

        deck_names = []
        for card in deck:
            deck_names.append(card[0])
        for row, field in enumerate(deck_names):
            self.frames[1].deck_summary_grid.SetRowLabelValue(row, field)

        # Populate the grid with the array data
        for row, data in enumerate(deck):
            for col, value in enumerate(data[1:]):
                self.frames[1].deck_summary_grid.SetCellValue(row, col, str(value))

        # Populate the grid with the array data
        for row, data in enumerate(deck_statistics):
            for col, value in enumerate(data):
                self.frames[1].deck_statistics_grid.SetCellValue(row, col, str(value))

        self.frames[1].deck_summary_grid.SetRowLabelSize(150)
        self.adjust_column_row_sizes(self.frames[1], self.frames[1].deck_statistics_grid, 150, 150,
                                     len(deck_statistics_names))
        self.frames[1].deck_summary_grid.ForceRefresh()
        self.frames[1].deck_statistics_grid.ForceRefresh()
        self.frames[1].Layout()

    def refresh_test_deck_grids(self, deck, simulation):
        self.frames[2].deck_grid.ClearGrid()
        self.frames[2].simulation_grid.ClearGrid()

        self.set_rows_cols(self.frames[2], self.frames[2].deck_grid, len(deck), 3)
        self.set_rows_cols(self.frames[2], self.frames[2].simulation_grid, len(simulation), 6)

        self.frames[2].deck_grid.SetRowLabelValue(0, "Card Name")
        self.frames[2].deck_grid.SetRowLabelValue(1, "Level")
        self.frames[2].deck_grid.SetRowLabelValue(2, "Fusion")

        self.frames[2].simulation_grid.SetRowLabelValue(0, "Average TS")
        self.frames[2].simulation_grid.SetRowLabelValue(1, "Average Atk")
        self.frames[2].simulation_grid.SetRowLabelValue(2, "Average Def")
        self.frames[2].simulation_grid.SetRowLabelValue(3, "Average Orbs")
        self.frames[2].simulation_grid.SetRowLabelValue(4, "Average Health")
        self.frames[2].simulation_grid.SetRowLabelValue(5, "% Combo")

        for col, data in enumerate(deck):
            for row, value, in enumerate(data[:3]):
                self.frames[2].deck_grid.SetCellValue(row, col, str(value))
        for i in range(0, len(deck)):
            self.frames[2].deck_grid.SetColLabelValue(i, str(i + 1))

        self.adjust_column_row_sizes(self.frames[2], self.frames[2].deck_grid, 150, 100, len(deck))
        for col, data in enumerate(simulation):
            for row, value in enumerate(data):
                self.frames[2].simulation_grid.SetCellValue(row, col, str(value[1]))
        for i in range(0, len(simulation)):
            self.frames[2].simulation_grid.SetColLabelValue(i, str(i + 1))
        self.frames[2].simulation_grid.SetRowLabelSize(100)

    def add_card_to_library(self, event):
        card_name = self.card_name_choice.GetStringSelection()
        card_level = int(self.card_level_choice.GetStringSelection())
        card_fusion = self.fusion_choice.GetStringSelection()
        amount = self.card_amount.GetValue()
        if not amount.isnumeric():
            wx.MessageBox(f"'{amount}' is invalid\nEnter a valid amount", "Error", wx.OK | wx.ICON_WARNING)
            return
        amount = int(amount)
        if card_fusion == 'Yes' and card_level != 5:
            wx.MessageBox("Card must be level 5 to be fused", "Error", wx.OK | wx.ICON_WARNING)
            return
        for i in range(0, len(self.user_library)):
            if card_name == self.user_library[i][0]:
                if card_level == self.user_library[i][1]:
                    if card_fusion == self.user_library[i][2]:
                        self.user_library[i][3] = self.user_library[i][3] + amount
                        self.refresh_user_card_library_grid()
                        self.refresh_delete_card_choice()
                        return
        self.user_library.append([card_name, card_level, card_fusion, amount])
        self.refresh_user_card_library_grid()
        self.refresh_delete_card_choice()

    def delete_card_from_library(self, event):
        card_name = self.delete_card_choice.GetStringSelection()
        pattern = ':L|:F'
        attributes = re.split(pattern, card_name)
        for i in range(0, len(self.user_library)):
            if attributes[0] == self.user_library[i][0]:
                if int(attributes[1]) == self.user_library[i][1]:
                    if attributes[2] == self.user_library[i][2]:
                        self.user_library.pop(i)
                        break
        self.refresh_user_card_library_grid()
        self.refresh_delete_card_choice()

    def save_user_card_library(self, event):
        save_user_library(self.user_library)
        wx.MessageBox("Card Library Successfully Saved", "Save", wx.OK | wx.ICON_INFORMATION)

    def load_andersam_optimizer(self, event):
        andersam_file = self.file_picker.GetPath()
        test = load_andersam_optimizer_library(andersam_file)
        if test == False:
            wx.MessageBox("Incorrect or corrupted file\nTry Again", "Error Loading Andersam File",
                          wx.OK | wx.ICON_ERROR)
        else:
            self.user_library = test
        self.refresh_user_card_library_grid()
        self.refresh_delete_card_choice()

    def optimize_deck(self, event):
        choice = self.frames[1].mode_choice.GetStringSelection()
        if choice == 'Custom':
            if not self.frames[1].custom_percentage.GetValue().isnumeric() \
                    or int(self.frames[1].custom_percentage.GetValue()) > 100 \
                    or int(self.frames[1].custom_percentage.GetValue()) < 0:
                wx.MessageBox("Incorrect custom percentage value\nCustom percentage must be between (0 - 100)\nTry "
                              "Again", "Incorrect Custom Input", wx.OK | wx.ICON_ERROR)
                return
        if not self.frames[1].deck_size.GetValue().isnumeric():
            wx.MessageBox("Incorrect deck size value\nTry Again", "Incorrect Deck Size Input", wx.OK | wx.ICON_ERROR)
            return
        deck_size = int(self.frames[1].deck_size.GetValue())
        number_cards = 0
        if self.current_deck == 1:
            number_cards = len(self.deck_1)
            if deck_size > (self.deck_size_counter(self.deck_1_user_library) + number_cards):
                wx.MessageBox("Deck size value is greater than number of available cards\nTry Again",
                              "Incorrect Deck Size Input", wx.OK | wx.ICON_ERROR)
                return
            if deck_size <= number_cards:
                wx.MessageBox("Deck size value is smaller than current deck size\nTry reducing the number of cards in "
                              "your current deck", "Incorrect Deck Size Input", wx.OK | wx.ICON_ERROR)
                return
        elif self.current_deck == 2:
            number_cards = len(self.deck_2)
            if deck_size > (self.deck_size_counter(self.deck_2_user_library) + number_cards):
                wx.MessageBox("Deck size value is greater than number of available cards\nTry Again",
                              "Incorrect Deck Size Input", wx.OK | wx.ICON_ERROR)
                return
            if deck_size <= number_cards:
                wx.MessageBox("Deck size value is smaller than current deck size\nTry reducing the number of cards in "
                              "your current deck", "Incorrect Deck Size Input", wx.OK | wx.ICON_ERROR)
                return
        else:
            number_cards = len(self.deck_3)
            if deck_size > (self.deck_size_counter(self.deck_3_user_library) + number_cards):
                wx.MessageBox("Deck size value is greater than number of available cards\nTry Again",
                              "Incorrect Deck Size Input", wx.OK | wx.ICON_ERROR)
                return
            if deck_size <= number_cards:
                wx.MessageBox("Deck size value is smaller than current deck size\nTry reducing the number of cards in "
                              "your current deck", "Incorrect Deck Size Input", wx.OK | wx.ICON_ERROR)
                return
        while number_cards < deck_size:
            best_card_index = None
            if self.current_deck == 1:
                best_card_index = self.maximise_card(self.deck_1, self.deck_1_user_library, choice)
                if best_card_index == -1:
                    wx.MessageBox(f"Deck size value is greater than number of available cards\nDeck Size: {number_cards}",
                                  "Maximum Deck Size Reached", wx.OK | wx.ICON_INFORMATION)
                    break
                self.deck_1_user_library[best_card_index][3] = self.deck_1_user_library[best_card_index][3] - 1
                name = self.deck_1_user_library[best_card_index][0]
                lvl = self.deck_1_user_library[best_card_index][1]
                fusion = self.deck_1_user_library[best_card_index][2]
                self.deck_1.append([name, lvl, fusion])
            elif self.current_deck == 2:
                best_card_index = self.maximise_card(self.deck_2, self.deck_2_user_library, choice)
                if best_card_index == -1:
                    wx.MessageBox(f"Deck size value is greater than number of available cards\nDeck Size: {number_cards}",
                                  "Maximum Deck Size Reached", wx.OK | wx.ICON_INFORMATION)
                    break
                self.deck_2_user_library[best_card_index][3] = self.deck_2_user_library[best_card_index][3] - 1
                name = self.deck_2_user_library[best_card_index][0]
                lvl = self.deck_2_user_library[best_card_index][1]
                fusion = self.deck_2_user_library[best_card_index][2]
                self.deck_2.append([name, lvl, fusion])
            else:
                best_card_index = self.maximise_card(self.deck_3, self.deck_3_user_library, choice)
                if best_card_index == -1:
                    wx.MessageBox(f"Deck size value is greater than number of available cards\nDeck Size: {number_cards}",
                                  "Maximum Deck Size Reached", wx.OK | wx.ICON_INFORMATION)
                    break
                self.deck_2_user_library[best_card_index][3] = self.deck_3_user_library[best_card_index][3] - 1
                name = self.deck_3_user_library[best_card_index][0]
                lvl = self.deck_3_user_library[best_card_index][1]
                fusion = self.deck_3_user_library[best_card_index][2]
                self.deck_3.append([name, lvl, fusion])
            number_cards += 1

        if self.current_deck == 1:
            self.deck_stat_names_1.clear()
            self.deck_stats_1 = []
            for i in range(0, len(self.deck_1)):
                self.deck_stats_1.append([])
                for j in range(0, len(self.deck_1)):
                    self.deck_stats_1[i].append(0)
            for i in range(0, len(self.deck_1)):
                self.deck_1[i], self.deck_stats_1 = self.determine_statistics(i, self.deck_1, self.deck_stats_1)
                self.deck_stat_names_1.append(self.deck_1[i][0])
            self.refresh_optimize_deck_grids(self.deck_1, self.deck_stat_names_1, self.deck_stats_1)
            self.refresh_add_card_choice(self.deck_1, self.deck_1_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_1)
        elif self.current_deck == 2:
            self.deck_stat_names_2.clear()
            self.deck_stats_2 = []
            for i in range(0, len(self.deck_2)):
                self.deck_stats_2.append([])
                for j in range(0, len(self.deck_2)):
                    self.deck_stats_2[i].append(0)
            for i in range(0, len(self.deck_2)):
                self.deck_2[i], self.deck_stats_2 = self.determine_statistics(i, self.deck_2, self.deck_stats_2)
                self.deck_stat_names_2.append(self.deck_2[i][0])
            self.refresh_optimize_deck_grids(self.deck_2, self.deck_stat_names_2, self.deck_stats_2)
            self.refresh_add_card_choice(self.deck_2, self.deck_2_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_2)
        else:
            self.deck_stat_names_3.clear()
            self.deck_stats_3 = []
            for i in range(0, len(self.deck_2)):
                self.deck_stats_3.append([])
                for j in range(0, len(self.deck_3)):
                    self.deck_stats_3[i].append(0)
            for i in range(0, len(self.deck_3)):
                self.deck_3[i], self.deck_stats_3 = self.determine_statistics(i, self.deck_3, self.deck_stats_3)
                self.deck_stat_names_3.append(self.deck_2[i][0])
            self.refresh_optimize_deck_grids(self.deck_3, self.deck_stat_names_3, self.deck_stats_3)
            self.refresh_add_card_choice(self.deck_3, self.deck_3_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_3)
        return

    def maximise_card(self, deck, deck_library, choice):
        max_score = 0
        max_index = -1
        if len(deck) == 0:
            for i in range(0, len(deck_library)):
                score = 0
                for j in range(0, len(deck_library)):
                    if i == j:
                        if deck_library[i][3] <= 1:
                            continue
                    if deck_library[i][0] in self.all_combo_cards[deck_library[j][0]].combinations:
                        result = self.all_combo_cards[deck_library[j][0]].combinations[deck_library[i][0]]
                        attack = self.all_base_cards[result].attack
                        defense = self.all_base_cards[result].defense
                        rarity = self.all_base_cards[result].rarity
                        attack, defense = self.determine_level_stats(attack, defense, rarity, deck_library[i]
                                                                     , deck_library[j])
                        if choice == 'Attack':
                            score = score + attack
                        elif choice == 'Defense':
                            score = score + defense
                        elif choice == 'Total Stat':
                            score = score + attack + defense
                        else:
                            percentage = float(self.frames[1].custom_percentage.GetValue())/100
                            score = score + (attack*percentage + defense*(1-percentage))
                if score > max_score:
                    max_score = score
                    max_index = i
            return max_index
        else:
            for i in range(0, len(deck_library)):
                if deck_library[i][3] <= 0 or self.name_counter(deck_library[i][0], deck) >= 3:
                    continue
                score = 0
                for j in range(0, len(deck)):
                    if deck_library[i][0] in self.all_combo_cards[deck[j][0]].combinations:
                        result = self.all_combo_cards[deck[j][0]].combinations[deck_library[i][0]]
                        attack = self.all_base_cards[result].attack
                        defense = self.all_base_cards[result].defense
                        rarity = self.all_base_cards[result].rarity
                        attack, defense = self.determine_level_stats(attack, defense, rarity, deck_library[i]
                                                                     , deck[j])
                        if choice == 'Attack':
                            score = score + attack
                        elif choice == 'Defense':
                            score = score + defense
                        elif choice == 'Total Stat':
                            score = score + attack + defense
                        else:
                            percentage = float(self.frames[1].custom_percentage.GetValue())/100
                            score = score + (attack*percentage + defense*(1-percentage))
                if score > max_score:
                    max_score = score
                    max_index = i
            return max_index

    def determine_level_stats(self, attack, defense, result_rarity, combo_1, combo_2):
        avg_lvl = float(combo_1[1] + combo_2[1])/2
        avg_lvl = ceil(avg_lvl)
        if self.all_combo_cards[combo_1[0]].rarity == 5 and self.all_combo_cards[combo_2[0]].rarity == 5:
            if result_rarity == 4:
                attack = attack + 3
                defense = defense + 3
            elif result_rarity == 3:
                attack = attack + 5
                defense = defense + 5
            elif result_rarity == 2:
                attack = attack + 7
                defense = defense + 7
            else:
                attack = attack + 9
                defense = defense + 9
            result_rarity = 4
        elif self.all_combo_cards[combo_1[0]].rarity == 5 or self.all_combo_cards[combo_2[0]].rarity == 5:
            if result_rarity == 3:
                attack = attack + 3
                defense = defense + 3
            elif result_rarity == 2:
                attack = attack + 5
                defense = defense + 5
            elif result_rarity == 1:
                attack = attack + 7
                defense = defense + 7
            result_rarity = 4

        if result_rarity == 4 or result_rarity == 3:
            avg_lvl = avg_lvl + 1

        max_combo_rarity = max(self.all_combo_cards[combo_1[0]].rarity, self.all_combo_cards[combo_2[0]].rarity)
        if max_combo_rarity == 5:
            attack = attack + 4 * (avg_lvl - 1)
            defense = defense + 4 * (avg_lvl - 1)
        elif max_combo_rarity == 3:
            attack = attack + 3 * (avg_lvl - 1)
            defense = defense + 3 * (avg_lvl - 1)
        elif max_combo_rarity == 2:
            attack = attack + 2 * (avg_lvl - 1)
            defense = defense + 2 * (avg_lvl - 1)
        else:
            attack = attack + (avg_lvl - 1)
            defense = defense + (avg_lvl - 1)
        return attack, defense

    def determine_statistics(self, index, deck, deck_statistics):
        avg_atk = 0
        avg_def = 0
        name = deck[index][0]
        for i in range(0, len(deck)):
            if i != index:
                if name in self.all_combo_cards[deck[i][0]].combinations:
                    result = self.all_combo_cards[deck[i][0]].combinations[name]
                    attack = self.all_base_cards[result].attack
                    defense = self.all_base_cards[result].defense
                    rarity = self.all_base_cards[result].rarity
                    attack, defense = self.determine_level_stats(attack, defense, rarity, deck[index], deck[i])
                    deck_statistics[index][i] = attack + defense
                    avg_atk += attack
                    avg_def += defense
        avg_ts = (avg_atk + avg_def)/(max(len(deck) - 1, 1))
        avg_atk = avg_atk/(max(len(deck) - 1, 1))
        avg_def = avg_def/(max(len(deck) - 1, 1))
        return [deck[index][0], deck[index][1], deck[index][2], avg_ts, avg_atk, avg_def], deck_statistics

    def add_card_to_deck(self, event):
        card_add = self.frames[1].add_card_choice.GetStringSelection()
        if card_add == "":
            wx.MessageBox("No more cards can be added to the deck",
                          "Invalid Card", wx.OK | wx.ICON_ERROR)
            return
        pattern = ":L"
        result = re.split(pattern, card_add)
        card_name = result[0]
        pattern_2 = ":F"
        result_2 = re.split(pattern_2, result[1])
        lvl = int(result_2[0])
        fusion = result_2[1]
        if self.current_deck == 1:
            self.deck_1.append([card_name, lvl, fusion])
            for i in range(0, len(self.deck_1_user_library)):
                if card_name == self.deck_1_user_library[i][0] and lvl == self.deck_1_user_library[i][1] and \
                        fusion == self.deck_1_user_library[i][2]:
                    self.deck_1_user_library[i][3] -= 1
                    break
            self.deck_stat_names_1.clear()
            self.deck_stats_1 = []
            for i in range(0, len(self.deck_1)):
                self.deck_stats_1.append([])
                for j in range(0, len(self.deck_1)):
                    self.deck_stats_1[i].append(0)
            for i in range(0, len(self.deck_1)):
                self.deck_1[i], self.deck_stats_1 = self.determine_statistics(i, self.deck_1, self.deck_stats_1)
                self.deck_stat_names_1.append(self.deck_1[i][0])
            self.refresh_optimize_deck_grids(self.deck_1, self.deck_stat_names_1, self.deck_stats_1)
            self.refresh_add_card_choice(self.deck_1, self.deck_1_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_1)
        elif self.current_deck == 2:
            self.deck_2.append([card_name, lvl, fusion])
            for i in range(0, len(self.deck_2_user_library)):
                if card_name == self.deck_2_user_library[i][0] and lvl == self.deck_2_user_library[i][1] and \
                        fusion == self.deck_2_user_library[i][2]:
                    self.deck_2_user_library[i][3] -= 1
                    break
            self.deck_stat_names_2.clear()
            self.deck_stats_2 = []
            for i in range(0, len(self.deck_2)):
                self.deck_stats_2.append([])
                for j in range(0, len(self.deck_2)):
                    self.deck_stats_2[i].append(0)
            for i in range(0, len(self.deck_2)):
                self.deck_2[i], self.deck_stats_2 = self.determine_statistics(i, self.deck_2, self.deck_stats_2)
                self.deck_stat_names_2.append(self.deck_2[i][0])
            self.refresh_optimize_deck_grids(self.deck_2, self.deck_stat_names_2, self.deck_stats_2)
            self.refresh_add_card_choice(self.deck_2, self.deck_2_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_2)
        else:
            self.deck_3.append([card_name, lvl, fusion])
            for i in range(0, len(self.deck_3_user_library)):
                if card_name == self.deck_3_user_library[i][0] and lvl == self.deck_3_user_library[i][1] and \
                        fusion == self.deck_3_user_library[i][2]:
                    self.deck_3_user_library[i][3] -= 1
                    break
            self.deck_stat_names_3.clear()
            self.deck_stats_3 = []
            for i in range(0, len(self.deck_3)):
                self.deck_stats_3.append([])
                for j in range(0, len(self.deck_3)):
                    self.deck_stats_3[i].append(0)
            for i in range(0, len(self.deck_3)):
                self.deck_3[i], self.deck_stats_3 = self.determine_statistics(i, self.deck_3, self.deck_stats_3)
                self.deck_stat_names_3.append(self.deck_3[i][0])
            self.refresh_optimize_deck_grids(self.deck_3, self.deck_stat_names_3, self.deck_stats_3)
            self.refresh_add_card_choice(self.deck_3, self.deck_3_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_3)
        return

    def delete_card_from_deck(self, event):
        delete_card = self.frames[1].delete_card_from_deck_choice.GetStringSelection()
        if delete_card == "":
            wx.MessageBox("No more cards can be deleted from the deck",
                          "Invalid Card", wx.OK | wx.ICON_ERROR)
            return
        result = re.split(":L", delete_card)
        card_name = result[0]
        result_2 = re.split(":F", result[1])
        lvl = int(result_2[0])
        fusion = result_2[1]
        if self.current_deck == 1:
            for i in range(0, len(self.deck_1)):
                if self.deck_1[i][0] == card_name and lvl == self.deck_1[i][1] and fusion == self.deck_1[i][2]:
                    self.deck_1.pop(i)
                    for j in range(0, len(self.deck_1_user_library)):
                        if self.deck_1_user_library[j][0] == card_name and lvl == self.deck_1_user_library[j][1] and \
                                fusion == self.deck_1_user_library[j][2]:
                            self.deck_1_user_library[j][3] += 1
                    break
            self.deck_stat_names_1.clear()
            self.deck_stats_1 = []
            for i in range(0, len(self.deck_1)):
                self.deck_stats_1.append([])
                for j in range(0, len(self.deck_1)):
                    self.deck_stats_1[i].append(0)
            for i in range(0, len(self.deck_1)):
                self.deck_1[i], self.deck_stats_1 = self.determine_statistics(i, self.deck_1, self.deck_stats_1)
                self.deck_stat_names_1.append(self.deck_1[i][0])
            self.refresh_optimize_deck_grids(self.deck_1, self.deck_stat_names_1, self.deck_stats_1)
            self.refresh_delete_card_from_deck_choice(self.deck_1)
            self.refresh_add_card_choice(self.deck_1, self.deck_1_user_library)
        elif self.current_deck == 2:
            for i in range(0, len(self.deck_2)):
                if self.deck_2[i][0] == card_name and lvl == self.deck_2[i][1] and fusion == self.deck_2[i][2]:
                    self.deck_2.pop(i)
                    for j in range(0, len(self.deck_2_user_library)):
                        if self.deck_2_user_library[j][0] == card_name and lvl == self.deck_2_user_library[j][1] and \
                                fusion == self.deck_2_user_library[j][2]:
                            self.deck_2_user_library[j][3] += 1
                    break
            self.deck_stat_names_2.clear()
            self.deck_stats_2 = []
            for i in range(0, len(self.deck_2)):
                self.deck_stats_2.append([])
                for j in range(0, len(self.deck_2)):
                    self.deck_stats_2[i].append(0)
            for i in range(0, len(self.deck_2)):
                self.deck_2[i], self.deck_stats_2 = self.determine_statistics(i, self.deck_2, self.deck_stats_2)
                self.deck_stat_names_2.append(self.deck_2[i][0])
            self.refresh_optimize_deck_grids(self.deck_2, self.deck_stat_names_2, self.deck_stats_2)
            self.refresh_delete_card_from_deck_choice(self.deck_2)
            self.refresh_add_card_choice(self.deck_2, self.deck_2_user_library)
        else:
            for i in range(0, len(self.deck_3)):
                if self.deck_3[i][0] == card_name and lvl == self.deck_3[i][1] and fusion == self.deck_3[i][2]:
                    self.deck_3.pop(i)
                    for j in range(0, len(self.deck_3_user_library)):
                        if self.deck_3_user_library[j][0] == card_name and lvl == self.deck_3_user_library[j][1] and \
                                fusion == self.deck_3_user_library[j][2]:
                            self.deck_3_user_library[j][3] += 1
                    break
            self.deck_stat_names_3.clear()
            self.deck_stats_3 = []
            for i in range(0, len(self.deck_3)):
                self.deck_stats_3.append([])
                for j in range(0, len(self.deck_3)):
                    self.deck_stats_3[i].append(0)
            for i in range(0, len(self.deck_3)):
                self.deck_3[i], self.deck_stats_3 = self.determine_statistics(i, self.deck_3, self.deck_stats_3)
                self.deck_stat_names_3.append(self.deck_3[i][0])
            self.refresh_optimize_deck_grids(self.deck_3, self.deck_stat_names_3, self.deck_stats_3)
            self.refresh_delete_card_from_deck_choice(self.deck_3)
            self.refresh_add_card_choice(self.deck_3, self.deck_3_user_library)

    def clear_deck(self, event):
        if self.current_deck == 1:
            self.deck_1 = []
            self.deck_1_user_library = copy.deepcopy(self.user_library)
            self.deck_stats_1 = []
            self.deck_stat_names_1 = []
            self.refresh_optimize_deck_grids(self.deck_1, self.deck_stat_names_1, self.deck_stats_1)
            self.refresh_add_card_choice(self.deck_1, self.deck_1_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_1)
        elif self.current_deck == 2:
            self.deck_2 = []
            self.deck_2_user_library = copy.deepcopy(self.user_library)
            self.deck_stats_2 = []
            self.deck_stat_names_2 = []
            self.refresh_optimize_deck_grids(self.deck_2, self.deck_stat_names_2, self.deck_stats_2)
            self.refresh_add_card_choice(self.deck_2, self.deck_2_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_2)
        else:
            self.deck_3 = []
            self.deck_3_user_library = copy.deepcopy(self.user_library)
            self.deck_stats_3 = []
            self.deck_stat_names_3 = []
            self.refresh_optimize_deck_grids(self.deck_3, self.deck_stat_names_3, self.deck_stats_3)
            self.refresh_add_card_choice(self.deck_3, self.deck_3_user_library)
            self.refresh_delete_card_from_deck_choice(self.deck_3)

    def save_deck(self, event):
        if self.current_deck == 1:
            save_user_deck(self.deck_1, self.deck_1_user_library, 'deck_1')
        elif self.current_deck == 2:
            save_user_deck(self.deck_2, self.deck_2_user_library, 'deck_2')
        else:
            save_user_deck(self.deck_3, self.deck_3_user_library, 'deck_3')
        wx.MessageBox("Deck Saved", "Save Success", wx.OK | wx.ICON_INFORMATION)

    def add_final_form(self, event):
        attack = self.frames[2].attack_txtctrl.GetValue()
        defense = self.frames[2].defense_txtctrl.GetValue()
        level = self.frames[2].level_choice.GetStringSelection()
        if not level.isnumeric():
            wx.MessageBox("Invalid Level", "Invalid Input", wx.OK | wx.ICON_WARNING)
            return
        level = int(level)
        fusion = self.frames[2].fusion_choice.GetStringSelection()
        ability = self.frames[2].ability_choice.GetStringSelection()
        if fusion == "" or ability == "":
            wx.MessageBox("Invalid fusion or ability inputs", "Invalid Input", wx.OK | wx.ICON_WARNING)
            return
        if (not attack.isnumeric()) or (not defense.isnumeric()):
            wx.MessageBox("Attack or Defense values are not valid", "Invalid Input", wx.OK | wx.ICON_WARNING)
            return
        if level < 5 and fusion == "Yes":
            wx.MessageBox("Card cannot be fused if its level is less than 5", "Invalid Input", wx.OK | wx.ICON_WARNING)
            return
        name = "Final Form: " + attack + ":" + defense + ":" + ability
        if self.current_test_deck == 1:
            self.test_deck_1.append([name, level, fusion])
            self.refresh_test_deck_grids(self.test_deck_1, self.simulation_1)
            self.refresh_remove_final_form(self.test_deck_1)
        elif self.current_test_deck == 2:
            self.test_deck_2.append([name, level, fusion])
            self.refresh_test_deck_grids(self.test_deck_2, self.simulation_2)
            self.refresh_remove_final_form(self.test_deck_2)
        else:
            self.test_deck_3.append([name, level, fusion])
            self.refresh_test_deck_grids(self.test_deck_3, self.simulation_3)
            self.refresh_remove_final_form(self.test_deck_3)

    def remove_final_form(self, event):
        final_form = self.frames[2].remove_final_choice.GetStringSelection()
        if self.current_test_deck == 1:
            for i in range(0, len(self.test_deck_1)):
                if self.test_deck_1[i][0] == final_form:
                    self.test_deck_1.pop(i)
                    break
            self.refresh_test_deck_grids(self.test_deck_1, self.simulation_1)
            self.refresh_remove_final_form(self.test_deck_1)
        elif self.current_test_deck == 2:
            for i in range(0, len(self.test_deck_2)):
                if self.test_deck_2[i][0] == final_form:
                    self.test_deck_2.pop(i)
                    break
            self.refresh_test_deck_grids(self.test_deck_2, self.simulation_2)
            self.refresh_remove_final_form(self.test_deck_2)
        else:
            for i in range(0, len(self.test_deck_3)):
                if self.test_deck_3[i][0] == final_form:
                    self.test_deck_3.pop(i)
                    break
            self.refresh_test_deck_grids(self.test_deck_3, self.simulation_3)
            self.refresh_remove_final_form(self.test_deck_3)

    def simulate_deck(self, event):
        deck = []
        if self.current_test_deck == 1:
            deck = copy.deepcopy(self.test_deck_1)
        elif self.current_test_deck == 2:
            deck = copy.deepcopy(self.test_deck_2)
        else:
            deck = copy.deepcopy(self.test_deck_3)

        mode = self.frames[2].mode_choice.GetStringSelection()
        final_form_preference = self.frames[2].final_preference_choice.GetStringSelection()
        number_simulations = self.frames[2].number_simulations_txtctrl.GetValue()
        if not number_simulations.isnumeric():
            wx.MessageBox("Invalid number of simulations", "Invalid Input", wx.OK | wx.ICON_WARNING)
            return
        number_simulations = int(number_simulations)
        simulation_results = []

        final_form_pattern = "^Final Form:"
        for i in range(0, number_simulations):
            hand = []
            orbs = 0
            health = 30
            index_array = [j for j in range(0, len(deck))]
            turn = 0

            # Initialise hand
            for j in range(0, 5):
                if len(index_array) == 0:
                    break
                random_num = random.randint(0, len(index_array) - 1)
                random_index = index_array[random_num]
                random_card = deck[random_index]
                hand.append(random_card)
                index_array.pop(random_num)

            while len(hand) > 0:
                final_form_check_signal = True
                # Determine the best final form to play
                if orbs >= 2:
                    final_form_score = 0
                    final_form_ability = ""
                    final_form_attack = 0
                    final_form_attack_score = 0
                    final_form_defense = 0
                    final_form_defense_score = 0
                    final_form_index = -1
                    for j in range(0, len(hand)):
                        current_card_name = hand[j][0]
                        ability = ""
                        final_form_card_score = 0
                        if re.search(final_form_pattern, current_card_name) and hand[j][2] == "Yes":
                            ability_array = re.split(":", current_card_name)
                            ability = ability_array[len(ability_array) - 1]
                            attack_array = re.split(" ", ability_array[1])
                            attack = int(attack_array[1])
                            defense = int(ability_array[2])
                            attack_score, defense_score, health_score = update_stats_based_on_ability(attack, defense, ability)
                            if final_form_preference == "Total Stat":
                                if ability == "Pillage" and orbs >= 3:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score
                                elif (ability == "Protection" or ability == "Absorb" or ability == "Curse") and orbs >= 4:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score
                                elif (ability == "Crushing Blow" or ability == "Critical Strike" or ability == "Plunder") \
                                        and orbs >= 5:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score
                                elif ability == "Siphon" or ability == "Pierce" or ability == "Block" or \
                                        ability == "Reflect" or ability == "Weaken":
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score
                            elif final_form_preference == "Attack":
                                if ability == "Pillage" and orbs >= 3:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score
                                elif (ability == "Protection" or ability == "Absorb" or ability == "Curse") and orbs >= 4:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score
                                elif (ability == "Crushing Blow" or ability == "Critical Strike" or ability == "Plunder") \
                                        and orbs >= 5:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score
                                elif ability == "Siphon" or ability == "Pierce" or ability == "Block" or \
                                        ability == "Reflect" or ability == "Weaken":
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score
                            elif final_form_preference == "Defense":
                                if ability == "Pillage" and orbs >= 3:
                                    final_form_check_signal = False
                                    final_form_card_score = defense_score
                                elif (ability == "Protection" or ability == "Absorb" or ability == "Curse") and orbs >= 4:
                                    final_form_check_signal = False
                                    final_form_card_score = defense_score
                                elif (ability == "Crushing Blow" or ability == "Critical Strike" or ability == "Plunder") \
                                        and orbs >= 5:
                                    final_form_check_signal = False
                                    final_form_card_score = defense_score
                                elif ability == "Siphon" or ability == "Pierce" or ability == "Block" or \
                                        ability == "Reflect" or ability == "Weaken":
                                    final_form_check_signal = False
                                    final_form_card_score = defense_score
                            else:
                                if ability == "Absorb" and orbs >= 4:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score + health_score
                                elif ability == "Siphon":
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score + health_score
                                elif ability == "Pillage" and orbs >= 3:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score + health_score
                                elif (ability == "Protection" or ability == "Curse") and orbs >= 4:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score + health_score
                                elif (ability == "Crushing Blow" or ability == "Critical Strike" or ability == "Plunder") \
                                        and orbs >= 5:
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score + health_score
                                elif ability == "Pierce" or ability == "Block" or \
                                        ability == "Reflect" or ability == "Weaken":
                                    final_form_check_signal = False
                                    final_form_card_score = attack_score + defense_score + health_score

                            if final_form_card_score > final_form_score:
                                final_form_score = final_form_card_score
                                final_form_attack_score = attack_score
                                final_form_defense_score = defense_score
                                final_form_attack = attack
                                final_form_defense = defense
                                final_form_ability = ability
                                final_form_index = j
                    if final_form_index != -1:
                        if turn >= len(simulation_results):
                            if final_form_ability == "Pierce" or final_form_ability == "Block" or \
                                    final_form_ability == "Reflect" or final_form_ability == "Siphon" or \
                                    final_form_ability == "Amplify" or final_form_ability == "Weaken":
                                orbs = orbs - 2
                                if final_form_ability == "Siphon":
                                    health = health + int(final_form_attack*1.5)
                                simulation_results.append([
                                    [final_form_attack_score + final_form_defense_score,
                                     final_form_attack_score + final_form_defense_score],
                                    [final_form_attack_score, final_form_attack_score],
                                    [final_form_defense_score, final_form_defense_score],
                                    [orbs, orbs],
                                    [health, health],
                                    [1, 1]
                                ])
                            elif final_form_ability == "Pillage":
                                orbs = orbs - 3
                                simulation_results.append([
                                    [final_form_attack_score + final_form_defense_score,
                                     final_form_attack_score + final_form_defense_score],
                                    [final_form_attack_score, final_form_attack_score],
                                    [final_form_defense_score, final_form_defense_score],
                                    [orbs, orbs],
                                    [health, health],
                                    [1, 1]
                                ])
                            elif final_form_ability == "Protection" or final_form_ability == "Absorb" or \
                                    final_form_ability == "Curse":
                                orbs = orbs - 4
                                if final_form_ability == "Absorb":
                                    health = health + final_form_attack
                                simulation_results.append([
                                    [final_form_attack_score + final_form_defense_score,
                                     final_form_attack_score + final_form_defense_score],
                                    [final_form_attack_score, final_form_attack_score],
                                    [final_form_defense_score, final_form_defense_score],
                                    [orbs, orbs],
                                    [health, health],
                                    [1, 1]
                                ])
                            else:
                                orbs = orbs - 5
                                simulation_results.append([
                                    [final_form_attack_score + final_form_defense_score,
                                     final_form_attack_score + final_form_defense_score],
                                    [final_form_attack_score, final_form_attack_score],
                                    [final_form_defense_score, final_form_defense_score],
                                    [orbs, orbs],
                                    [health, health],
                                    [1, 1]
                                ])
                        else:
                            if final_form_ability == "Pierce" or final_form_ability == "Block" or \
                                    final_form_ability == "Reflect" or final_form_ability == "Siphon" or \
                                    final_form_ability == "Amplify" or final_form_ability == "Weaken":
                                orbs = orbs - 2
                                if final_form_ability == "Siphon":
                                    health = health + int(final_form_attack*1.5)
                                # Total Stat
                                simulation_results[turn][0][0] += final_form_attack_score + final_form_defense_score
                                # Attack
                                simulation_results[turn][1][0] += final_form_attack_score
                                # Defense
                                simulation_results[turn][2][0] += final_form_defense_score
                                # Orbs
                                simulation_results[turn][3][0] += orbs
                                # Health
                                simulation_results[turn][4][0] += health
                                # % No Combo
                                simulation_results[turn][5][0] += 1
                            elif final_form_ability == "Pillage":
                                orbs = orbs - 3
                                # Total Stat
                                simulation_results[turn][0][0] += final_form_attack_score + final_form_defense_score
                                # Attack
                                simulation_results[turn][1][0] += final_form_attack_score
                                # Defense
                                simulation_results[turn][2][0] += final_form_defense_score
                                # Orbs
                                simulation_results[turn][3][0] += orbs
                                # Health
                                simulation_results[turn][4][0] += health
                                # % No Combo
                                simulation_results[turn][5][0] += 1
                            elif final_form_ability == "Protection" or final_form_ability == "Absorb" or \
                                    final_form_ability == "Curse":
                                orbs = orbs - 4
                                if final_form_ability == "Absorb":
                                    health = health + final_form_attack
                                # Total Stat
                                simulation_results[turn][0][0] += final_form_attack_score + final_form_defense_score
                                # Attack
                                simulation_results[turn][1][0] += final_form_attack_score
                                # Defense
                                simulation_results[turn][2][0] += final_form_defense_score
                                # Orbs
                                simulation_results[turn][3][0] += orbs
                                # Health
                                simulation_results[turn][4][0] += health
                                # % No Combo
                                simulation_results[turn][5][0] += 1
                            else:
                                orbs = orbs - 5
                                # Total Stat
                                simulation_results[turn][0][0] += final_form_attack_score + final_form_defense_score
                                # Attack
                                simulation_results[turn][1][0] += final_form_attack_score
                                # Defense
                                simulation_results[turn][2][0] += final_form_defense_score
                                # Orbs
                                simulation_results[turn][3][0] += orbs
                                # Health
                                simulation_results[turn][4][0] += health
                                # % No Combo
                                simulation_results[turn][5][0] += 1
                        # Remove Final Form Card From Hand
                        hand.pop(final_form_index)
                        # Add another card randomly from deck
                        if len(index_array) > 0:
                            random_num = random.randint(0, len(index_array) - 1)
                            random_index = index_array[random_num]
                            random_card = deck[random_index]
                            hand.append(random_card)
                            index_array.pop(random_num)
                        turn = turn + 1
                        continue

                # Determines the best combo to play
                # TS, Attack, Defense
                score = [0, 0, 0]
                # First combo index, Second combo index in hand
                best_card_index = (-1, -1)
                for j in range(0, len(hand)):
                    current_card_name = hand[j][0]
                    if re.search(final_form_pattern, current_card_name):
                        continue
                    for k in range(j + 1, len(hand)):
                        next_card_name = hand[k][0]
                        result_combo_score = 0
                        if re.search(final_form_pattern, next_card_name):
                            continue
                        if current_card_name in self.all_combo_cards[next_card_name].combinations:
                            result_name = self.all_combo_cards[next_card_name].combinations[current_card_name]
                            attack = self.all_base_cards[result_name].attack
                            defense = self.all_base_cards[result_name].defense
                            rarity = self.all_base_cards[result_name].rarity
                            attack, defense = self.determine_level_stats(attack, defense, rarity, hand[j], hand[k])
                            if mode == "Total Stat":
                                result_combo_score = attack + defense
                                if result_combo_score > score[0]:
                                    score[0] = attack + defense
                                    score[1] = attack
                                    score[2] = defense
                                    best_card_index = (j, k)
                            elif mode == "Attack":
                                result_combo_score = attack
                                if result_combo_score > score[1]:
                                    score[0] = attack + defense
                                    score[1] = attack
                                    score[2] = defense
                                    best_card_index = (j, k)
                            else:
                                result_combo_score = defense
                                if result_combo_score > score[2]:
                                    score[0] = attack + defense
                                    score[1] = attack
                                    score[2] = defense
                                    best_card_index = (j, k)
                if best_card_index[0] != -1 or best_card_index[1] != -1:
                    if hand[best_card_index[0]][2] == "Yes" and hand[best_card_index[1]][2] == "Yes":
                        orbs += 3
                        orbs = min(orbs, 5)
                    elif hand[best_card_index[0]][2] == "Yes" or hand[best_card_index[1]][2] == "Yes":
                        orbs += 2
                        orbs = min(orbs, 5)
                    else:
                        orbs += 1
                        orbs = min(orbs, 5)
                    if turn >= len(simulation_results):
                        simulation_results.append([
                            [score[0], score[0]],
                            [score[1], score[1]],
                            [score[2], score[2]],
                            [orbs, orbs],
                            [health, health],
                            [1, 1]
                        ])
                    else:
                        # Total Stat
                        simulation_results[turn][0][0] += score[0]
                        # Attack
                        simulation_results[turn][1][0] += score[1]
                        # Defense
                        simulation_results[turn][2][0] += score[2]
                        # Orbs
                        simulation_results[turn][3][0] += orbs
                        # Health
                        simulation_results[turn][4][0] += health
                        # % No Combo
                        simulation_results[turn][5][0] += 1

                    # Remove Both Combo Cards From Hand
                    hand.pop(best_card_index[1])
                    hand.pop(best_card_index[0])
                    # Add another card randomly from deck
                    for j in range(0, 2):
                        if len(index_array) <= 0:
                            break
                        random_num = random.randint(0, len(index_array) - 1)
                        random_index = index_array[random_num]
                        random_card = deck[random_index]
                        hand.append(random_card)
                        index_array.pop(random_num)
                    turn = turn + 1
                    continue
                else:
                    # Find the best Final Form if no combo has been found
                    if final_form_check_signal:
                        final_form_score = 0
                        final_form_attack = 0
                        final_form_defense = 0
                        final_form_index = -1
                        for j in range(0, len(hand)):
                            current_card_name = hand[j][0]
                            final_form_card_score = 0
                            if re.search(final_form_pattern, current_card_name):
                                ability_array = re.split(":", current_card_name)
                                attack_array = re.split(" ", ability_array[1])
                                attack = int(attack_array[1])
                                defense = int(ability_array[2])
                                if final_form_preference == "Total Stat":
                                    final_form_card_score = attack + defense
                                elif final_form_preference == "Attack" or final_form_preference == "Health":
                                    final_form_card_score = attack
                                elif final_form_preference == "Defense":
                                    final_form_card_score = defense
                                if final_form_card_score > final_form_score:
                                    final_form_score = final_form_card_score
                                    final_form_attack = attack
                                    final_form_defense = defense
                                    final_form_index = j
                        if final_form_index != -1:
                            if turn >= len(simulation_results):
                                simulation_results.append([
                                    [final_form_attack + final_form_defense,
                                     final_form_attack + final_form_defense],
                                    [final_form_attack, final_form_attack],
                                    [final_form_defense, final_form_defense],
                                    [orbs, orbs],
                                    [health, health],
                                    [1, 1]
                                ])
                            else:
                                # Total Stat
                                simulation_results[turn][0][0] += final_form_attack + final_form_defense
                                # Attack
                                simulation_results[turn][1][0] += final_form_attack
                                # Defense
                                simulation_results[turn][2][0] += final_form_defense
                                # Orbs
                                simulation_results[turn][3][0] += orbs
                                # Health
                                simulation_results[turn][4][0] += health
                                # % No Combo
                                simulation_results[turn][5][0] += 1
                            # Remove Final Form Card From Hand
                            hand.pop(final_form_index)
                            # Add another card randomly from deck
                            if len(index_array) > 0:
                                random_num = random.randint(0, len(index_array) - 1)
                                random_index = index_array[random_num]
                                random_card = deck[random_index]
                                hand.append(random_card)
                                index_array.pop(random_num)
                            turn = turn + 1
                            continue
                    # Find Combo Card with the lowest rarity and highest stats
                    lowest_combo_rarity = 6
                    worst_combo_card_index = -1
                    worst_combo_card_attack = 0
                    worst_combo_card_defense = 0
                    for j in range(0, len(hand)):
                        current_card_name = hand[j][0]
                        current_card_rarity = self.all_combo_cards[current_card_name].rarity
                        current_card_attack = self.all_combo_cards[current_card_name].attack
                        current_card_defense = self.all_combo_cards[current_card_name].defense
                        current_card_attack, current_card_defense = determine_stats(current_card_attack,
                                                                                    current_card_defense,
                                                                                    hand[j][1], current_card_rarity)
                        if current_card_rarity < lowest_combo_rarity:
                            lowest_combo_rarity = current_card_rarity
                            worst_combo_card_index = j
                            worst_combo_card_attack = current_card_attack
                            worst_combo_card_defense = current_card_defense
                    orbs = 0
                    if turn >= len(simulation_results):
                        simulation_results.append([
                            [worst_combo_card_attack + worst_combo_card_defense,
                             worst_combo_card_attack + worst_combo_card_defense],
                            [worst_combo_card_attack, worst_combo_card_attack],
                            [worst_combo_card_defense, worst_combo_card_defense],
                            [orbs, orbs],
                            [health, health],
                            [0, 0]
                        ])
                    else:
                        # Total Stat
                        simulation_results[turn][0][0] += worst_combo_card_attack + worst_combo_card_defense
                        # Attack
                        simulation_results[turn][1][0] += worst_combo_card_attack
                        # Defense
                        simulation_results[turn][2][0] += worst_combo_card_defense
                        # Orbs
                        simulation_results[turn][3][0] += orbs
                        # Health
                        simulation_results[turn][4][0] += health
                        # % No Combo
                        simulation_results[turn][5][0] += 0

                    # Remove Final Form Card From Hand
                    hand.pop(worst_combo_card_index)
                    # Add another card randomly from deck
                    if len(index_array) > 0:
                        random_num = random.randint(0, len(index_array) - 1)
                        random_index = index_array[random_num]
                        random_card = deck[random_index]
                        hand.append(random_card)
                        index_array.pop(random_num)
                    turn = turn + 1
        for i in range(0, len(simulation_results)):
            simulation_results[i][0][1] = (simulation_results[i][0][0]) / float(number_simulations)
            simulation_results[i][1][1] = (simulation_results[i][1][0]) / float(number_simulations)
            simulation_results[i][2][1] = (simulation_results[i][2][0]) / float(number_simulations)
            simulation_results[i][3][1] = (simulation_results[i][3][0]) / float(number_simulations)
            simulation_results[i][4][1] = (simulation_results[i][4][0]) / float(number_simulations)
            simulation_results[i][5][1] = ((simulation_results[i][5][0]) / float(number_simulations)) * 100
        if self.current_test_deck == 1:
            self.simulation_1 = simulation_results
            self.refresh_test_deck_grids(self.test_deck_1, self.simulation_1)
        elif self.current_test_deck == 2:
            self.simulation_2 = simulation_results
            self.refresh_test_deck_grids(self.test_deck_2, self.simulation_2)
        else:
            self.simulation_3 = simulation_results
            self.refresh_test_deck_grids(self.test_deck_3, self.simulation_3)

    def set_rows_cols(self, given_frame, given_grid, ColumnNumber, RowNumber):
        given_grid.ClearGrid()
        if given_grid.GetNumberCols() > 0:  # Check if cols exist
            given_grid.DeleteCols(0, given_grid.GetNumberCols())  # Remove existing cols
        given_grid.AppendCols(ColumnNumber)  # Add new cols

        if given_grid.GetNumberRows() > 0:  # Check if rows exist
            given_grid.DeleteRows(0, given_grid.GetNumberRows())  # Remove existing rows
        given_grid.AppendRows(RowNumber)  # Add new rows
        given_grid.ForceRefresh()
        given_frame.Layout()

    def adjust_column_row_sizes(self, given_frame, given_grid, ColumnSize, RowSize, length):
        # Sets the column cell sizes for a given length
        for i in range(length):
            given_grid.SetColSize(i, ColumnSize)

        # Set the row label size (this affects the left-hand labels, not the data cells)
        given_grid.SetRowLabelSize(RowSize)
        given_grid.ForceRefresh()
        given_frame.Layout()

    def refresh_delete_card_choice(self):
        card_names = []
        for i in range(0, len(self.user_library)):
            card_names.append(self.user_library[i][0] + ':L' + str(self.user_library[i][1]) + ':F'
                              + str(self.user_library[i][2]))
        self.delete_card_choice.Set(card_names)

    def refresh_add_card_choice(self, deck, deck_library):
        possible_cards = []
        for i in range(0, len(deck_library)):
            if deck_library[i][3] > 0:
                name = deck_library[i][0]
                count = self.name_counter(name, deck)
                if count < 3:
                    possible_cards.append(name + ':L' + str(deck_library[i][1]) + ':F' + str(deck_library[i][2]))
        self.frames[1].add_card_choice.Set(possible_cards)

    def refresh_delete_card_from_deck_choice(self, deck):
        possible_cards = []
        for i in range(0, len(deck)):
            possible_cards.append(deck[i][0] + ':L' + str(deck[i][1]) + ':F' + str(deck[i][2]))
        self.frames[1].delete_card_from_deck_choice.Set(possible_cards)

    def refresh_remove_final_form(self, deck):
        final_forms = []
        pattern = "^Final Form:"
        for i in range(0, len(deck)):
            if re.search(pattern, deck[i][0]):
                final_forms.append(deck[i][0])
        self.frames[2].remove_final_choice.Set(final_forms)

    def card_names_list(self):
        card_names = list(self.all_combo_card_names)
        card_names = sorted(card_names)
        return card_names

    def name_counter(self, name, deck):
        count = 0
        pattern = ':Onyx$'
        if re.search(pattern, name):
            name = name[0:(len(name)-5)]
        for i in range(0, len(deck)):
            card_name = deck[i][0]
            if re.search(pattern, card_name):
                card_name = card_name[0:(len(card_name) - 5)]
            if name == card_name:
                count = count + 1
        return count

    def deck_size_counter(self, deck_library):
        count = 0
        for i in range(0, len(deck_library)):
            if deck_library[i][3] > 3:
                count = count + 3
            else:
                count = count + deck_library[i][3]
        return count

    def find_attack_and_defense(self, name):
        name = name[12:]
        name = re.split(":", name)
        return int(name[0]), int(name[1]), name[2]

    def OnPaint(self, event, frame):
        filename = "Background2.png"
        # Check if running in a PyInstaller bundle
        if getattr(sys, 'frozen', False):
            # If in a bundle, get the directory where the app is running
            base_path = sys._MEIPASS
        else:
            # If running in a normal Python environment, use the current working directory
            base_path = os.path.dirname(__file__)
        filename = os.path.join(base_path, filename)
        # Handles the drawing of the background image
        dc = wx.PaintDC(frame)
        size = frame.GetSize()

        # Load and resize the image to fit the frame
        image = wx.Image(filename, wx.BITMAP_TYPE_ANY)
        image = image.Scale(size.GetWidth(), size.GetHeight())

        # Draw the resized image on the frame
        bitmap = wx.Bitmap(image)
        dc.DrawBitmap(bitmap, 0, 0, True)

    def OnResize(self, event, frame):
        # Refresh the frame to trigger EVT_PAINT on resize
        frame.Refresh()
        event.Skip()

    def sync_libraries(self):
        if len(self.user_library) == 0:
            self.deck_1, self.deck_1_user_library = [], []
            self.deck_stat_names_1 = []
            self.deck_stats_1 = []

            self.deck_2, self.deck_2_user_library = [], []
            self.deck_stat_names_2 = []
            self.deck_stats_2 = []

            self.deck_3, self.deck_3_user_library = [], []
            self.deck_stat_names_3 = []
            self.deck_stats_3 = []

            self.test_deck_1 = []
            self.simulation_1 = []

            self.test_deck_2 = []
            self.simulation_2 = []

            self.test_deck_3 = []
            self.simulation_3 = []
        else:
            # Check whether all cards within a deck are within user library
            if not self.check_valid_deck(self.deck_1):
                self.deck_1 = []
                self.deck_1_user_library = copy.deepcopy(self.user_library)
                self.deck_stat_names_1 = []
                self.deck_stats_1 = []
                self.test_deck_1 = []
                self.simulation_1 = []
            else:
                self.deck_1_user_library = self.refresh_user_deck_library(self.deck_1)
                self.deck_stat_names_1 = [name[0] for name in self.deck_1]
                self.deck_stats_1 = [[0 for _ in range(len(self.deck_1))] for _ in range(len(self.deck_1))]
                for i in range(0, len(self.deck_1)):
                    self.deck_1[i], self.deck_stats_1 = self.determine_statistics(i, self.deck_1, self.deck_stats_1)
                self.test_deck_1 = copy.deepcopy(self.deck_1)
                self.simulation_1 = []
            if not self.check_valid_deck(self.deck_2):
                self.deck_2 = []
                self.deck_2_user_library = copy.deepcopy(self.user_library)
                self.deck_stat_names_2 = []
                self.deck_stats_2 = []
                self.test_deck_2 = []
                self.simulation_2 = []
            else:
                self.deck_2_user_library = self.refresh_user_deck_library(self.deck_2)
                self.deck_stat_names_2 = [name[0] for name in self.deck_2]
                self.deck_stats_2 = [[0 for _ in range(len(self.deck_2))] for _ in range(len(self.deck_2))]
                for i in range(0, len(self.deck_2)):
                    self.deck_2[i], self.deck_stats_2 = self.determine_statistics(i, self.deck_2, self.deck_stats_2)
                self.test_deck_2 = copy.deepcopy(self.deck_2)
                self.simulation_2 = []
            if not self.check_valid_deck(self.deck_3):
                self.deck_3 = []
                self.deck_3_user_library = copy.deepcopy(self.user_library)
                self.deck_stat_names_3 = []
                self.deck_stats_3 = []
                self.test_deck_3 = []
                self.simulation_3 = []
            else:
                self.deck_3_user_library = self.refresh_user_deck_library(self.deck_3)
                self.deck_stat_names_3 = [name[0] for name in self.deck_3]
                self.deck_stats_3 = [[0 for _ in range(len(self.deck_3))] for _ in range(len(self.deck_3))]
                for i in range(0, len(self.deck_3)):
                    self.deck_3[i], self.deck_stats_3 = self.determine_statistics(i, self.deck_3, self.deck_stats_3)
                self.test_deck_3 = copy.deepcopy(self.deck_3)
                self.simulation_3 = []

    def check_valid_deck(self, deck):
        for i in range(0, len(deck)):
            signal = False
            for j in range(0, len(self.user_library)):
                if deck[i][0] == self.user_library[j][0]:
                    signal = True
                if signal:
                    break
            if not signal:
                return False
        return True

    def refresh_user_deck_library(self, deck):
        user_library = copy.deepcopy(self.user_library)
        for i in range(0, len(deck)):
            for j in range(0, len(user_library)):
                if deck[i][0] == user_library[j][0]:
                    user_library[j][3] = user_library[j][3] - 1
                    break
        return user_library

    def switch_to_deck_1(self, event):
        self.current_deck = 1
        self.frames[1].deck_summary_txt.SetLabel("Deck 1 Summary: ")
        self.frames[1].deck_stats_txt.SetLabel("Deck 1 Statistics:")
        self.refresh_add_card_choice(self.deck_1, self.deck_1_user_library)
        self.refresh_delete_card_from_deck_choice(self.deck_1)
        self.refresh_optimize_deck_grids(self.deck_1, self.deck_stat_names_1, self.deck_stats_1)

    def switch_to_deck_2(self, event):
        self.current_deck = 2
        self.frames[1].deck_summary_txt.SetLabel("Deck 2 Summary: ")
        self.frames[1].deck_stats_txt.SetLabel("Deck 2 Statistics:")
        self.refresh_add_card_choice(self.deck_2, self.deck_2_user_library)
        self.refresh_delete_card_from_deck_choice(self.deck_2)
        self.refresh_optimize_deck_grids(self.deck_2, self.deck_stat_names_2, self.deck_stats_2)

    def switch_to_deck_3(self, event):
        self.current_deck = 3
        self.frames[1].deck_summary_txt.SetLabel("Deck 3 Summary: ")
        self.frames[1].deck_stats_txt.SetLabel("Deck 3 Statistics:")
        self.refresh_add_card_choice(self.deck_3, self.deck_3_user_library)
        self.refresh_delete_card_from_deck_choice(self.deck_3)
        self.refresh_optimize_deck_grids(self.deck_3, self.deck_stat_names_3, self.deck_stats_3)

    def switch_to_test_deck_1(self, event):
        self.current_test_deck = 1
        self.frames[2].deck_txt.SetLabel("Deck 1:")
        self.refresh_test_deck_grids(self.test_deck_1, self.simulation_1)

    def switch_to_test_deck_2(self, event):
        self.current_test_deck = 2
        self.frames[2].deck_txt.SetLabel("Deck 2:")
        self.refresh_test_deck_grids(self.test_deck_2, self.simulation_2)

    def switch_to_test_deck_3(self, event):
        self.current_test_deck = 3
        self.frames[2].deck_txt.SetLabel("Deck 3:")
        self.refresh_test_deck_grids(self.test_deck_3, self.simulation_3)

    def switch_to_deck_frame(self, event):
        for frame in self.frames:
            if frame.IsShown():
                position = frame.GetPosition()
                size = frame.GetSize()
                frame.Hide()
                break
        self.frames[0].SetPosition(position)
        self.frames[0].SetSize(size)
        self.frames[0].Show()

    def switch_to_optimize_deck_frame(self, event):
        for frame in self.frames:
            if frame.IsShown():
                position = frame.GetPosition()
                size = frame.GetSize()
                frame.Hide()
                break
        self.frames[1].SetPosition(position)
        self.frames[1].SetSize(size)
        self.frames[1].Bind(wx.EVT_PAINT, lambda evt: self.OnPaint(evt, self.frames[1]))
        self.frames[1].Show()
        self.currently_optimizing = True
        self.sync_libraries()
        self.refresh_add_card_choice(self.deck_1, self.deck_1_user_library)
        self.refresh_delete_card_from_deck_choice(self.deck_1)
        self.refresh_optimize_deck_grids(self.deck_1, self.deck_stat_names_1, self.deck_stats_1)
        self.frames[1].deck_summary_txt.SetLabel("Deck 1 Summary: ")
        self.frames[1].deck_stats_txt.SetLabel("Deck 1 Statistics:")

    def switch_to_test_deck_frame(self, event):
        for frame in self.frames:
            if frame.IsShown():
                position = frame.GetPosition()
                size = frame.GetSize()
                frame.Hide()
                break
        self.frames[2].SetPosition(position)
        self.frames[2].SetSize(size)
        self.frames[2].Show()
        self.currently_optimizing = False
        self.sync_libraries()
        if self.current_test_deck == 1:
            self.refresh_test_deck_grids(self.test_deck_1, self.simulation_1)
            self.refresh_remove_final_form(self.test_deck_1)
        elif self.current_test_deck == 2:
            self.refresh_test_deck_grids(self.test_deck_2, self.simulation_2)
            self.refresh_remove_final_form(self.test_deck_2)
        else:
            self.refresh_test_deck_grids(self.test_deck_3, self.simulation_3)
            self.refresh_remove_final_form(self.test_deck_3)

    def switch_to_export_csv_frame_deck(self, event):
        self.export_csv_frame.Show()

    def close_export_csv_frame(self, event):
        self.export_csv_frame.Hide()

    def on_close_all_frames(self, event):
        """Close all frames when one is closed."""
        for frame in self.frames:
            frame.Destroy()
        self.export_csv_frame.Destroy()
        event.Skip()

# Don't change the following
if __name__ == "__main__":
    app = wx.App()
    frame = LittleAlchemistAnalyst()
    app.MainLoop()
