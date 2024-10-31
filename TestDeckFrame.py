# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class TestDeckFrame
###########################################################################

class TestDeckFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Little Alchemist Analyst"), pos = wx.DefaultPosition, size = wx.Size( 875,700 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 191, 113, 223 ) )

        bSizer32 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2.SetMinSize( wx.Size( -1,50 ) )

        bSizer2.Add( ( 350, 0), 0, wx.EXPAND, 5 )

        self.card_library_button = wx.Button( self, wx.ID_ANY, _(u"Card Library"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.card_library_button, 0, wx.ALL, 5 )

        self.optimized_deck_button = wx.Button( self, wx.ID_ANY, _(u"Optimize Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.optimized_deck_button, 0, wx.ALL, 5 )

        self.test_deck_button = wx.Button( self, wx.ID_ANY, _(u"Test Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.test_deck_button, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer2, 0, wx.EXPAND, 5 )

        bSizer47 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer47.Add( ( 450, 0), 0, wx.EXPAND, 5 )

        self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, _(u"Test Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText43.Wrap( -1 )

        self.m_staticText43.SetFont( wx.Font( 19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.m_staticText43.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer47.Add( self.m_staticText43, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer47, 0, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer13.SetMinSize( wx.Size( -1,85 ) )

        bSizer13.Add( ( 360, 0), 0, wx.EXPAND, 5 )

        self.deck_1_button = wx.Button( self, wx.ID_ANY, _(u"Deck 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.deck_1_button, 0, wx.ALL, 5 )

        self.deck_2_button = wx.Button( self, wx.ID_ANY, _(u"Deck 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.deck_2_button, 0, wx.ALL, 5 )

        self.deck_3_button = wx.Button( self, wx.ID_ANY, _(u"Deck 3"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.deck_3_button, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer13, 0, wx.EXPAND, 5 )

        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer46.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, _(u"Add Final Form:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        self.m_staticText23.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.m_staticText23.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer46.Add( self.m_staticText23, 0, wx.ALL, 5 )

        self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, _(u"Level:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText33.Wrap( -1 )

        self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer46.Add( self.m_staticText33, 0, wx.ALL, 5 )

        level_choiceChoices = []
        self.level_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), level_choiceChoices, 0 )
        self.level_choice.SetSelection( 0 )
        bSizer46.Add( self.level_choice, 0, wx.ALL, 5 )

        self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, _(u"Fusion:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )

        self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer46.Add( self.m_staticText34, 0, wx.ALL, 5 )

        fusion_choiceChoices = []
        self.fusion_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), fusion_choiceChoices, 0 )
        self.fusion_choice.SetSelection( 0 )
        bSizer46.Add( self.fusion_choice, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer46, 0, wx.EXPAND, 5 )

        bSizer39 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer39.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, _(u"Atk:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        self.m_staticText24.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer39.Add( self.m_staticText24, 0, wx.ALL, 5 )

        self.attack_txtctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer39.Add( self.attack_txtctrl, 0, wx.ALL, 5 )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, _(u"Def:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        self.m_staticText25.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer39.Add( self.m_staticText25, 0, wx.ALL, 5 )

        self.defense_txtctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer39.Add( self.defense_txtctrl, 0, wx.ALL, 5 )

        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, _(u"Ability:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        self.m_staticText26.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer39.Add( self.m_staticText26, 0, wx.ALL, 5 )

        ability_choiceChoices = []
        self.ability_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), ability_choiceChoices, 0 )
        self.ability_choice.SetSelection( 0 )
        bSizer39.Add( self.ability_choice, 0, wx.ALL, 5 )

        self.add_final_button = wx.Button( self, wx.ID_ANY, _(u"Add"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer39.Add( self.add_final_button, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer39, 0, wx.EXPAND, 5 )

        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, _(u"Remove Final Form:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        self.m_staticText27.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer41.Add( self.m_staticText27, 0, wx.ALL, 5 )

        remove_final_choiceChoices = []
        self.remove_final_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, remove_final_choiceChoices, 0 )
        self.remove_final_choice.SetSelection( 0 )
        bSizer41.Add( self.remove_final_choice, 0, wx.ALL, 5 )

        self.remove_final_button = wx.Button( self, wx.ID_ANY, _(u"Remove"), wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer41.Add( self.remove_final_button, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer41, 0, wx.EXPAND, 5 )

        bSizer42 = wx.BoxSizer( wx.VERTICAL )

        bSizer42.SetMinSize( wx.Size( -1,75 ) )
        self.deck_txt = wx.StaticText( self, wx.ID_ANY, _(u"Deck 1:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.deck_txt.Wrap( -1 )

        self.deck_txt.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.deck_txt.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer42.Add( self.deck_txt, 0, wx.ALL, 5 )

        self.deck_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,110 ), 0 )

        # Grid
        self.deck_grid.CreateGrid( 3, 10 )
        self.deck_grid.EnableEditing( True )
        self.deck_grid.EnableGridLines( True )
        self.deck_grid.EnableDragGridSize( False )
        self.deck_grid.SetMargins( 0, 0 )

        # Columns
        self.deck_grid.EnableDragColMove( False )
        self.deck_grid.EnableDragColSize( True )
        self.deck_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.deck_grid.EnableDragRowSize( True )
        self.deck_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.deck_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer42.Add( self.deck_grid, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer42, 0, wx.EXPAND, 5 )

        bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, _(u"Mode:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        self.m_staticText29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer43.Add( self.m_staticText29, 0, wx.ALL, 5 )

        mode_choiceChoices = []
        self.mode_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mode_choiceChoices, 0 )
        self.mode_choice.SetSelection( 0 )
        bSizer43.Add( self.mode_choice, 0, wx.ALL, 5 )

        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, _(u"Number of Simulations:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )

        self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer43.Add( self.m_staticText30, 0, wx.ALL, 5 )

        self.number_simulations_txtctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer43.Add( self.number_simulations_txtctrl, 0, wx.ALL, 5 )

        self.settings_button = wx.Button( self, wx.ID_ANY, _(u"Settings"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer43.Add( self.settings_button, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer43, 0, wx.EXPAND, 5 )

        bSizer44 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, _(u"Final Form Preference:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer44.Add( self.m_staticText31, 0, wx.ALL, 5 )

        final_preference_choiceChoices = []
        self.final_preference_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, final_preference_choiceChoices, 0 )
        self.final_preference_choice.SetSelection( 0 )
        bSizer44.Add( self.final_preference_choice, 0, wx.ALL, 5 )

        self.simulation_button = wx.Button( self, wx.ID_ANY, _(u"Run Simulation"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer44.Add( self.simulation_button, 0, wx.ALL, 5 )


        bSizer44.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.export_csv_button = wx.Button( self, wx.ID_ANY, _(u"Export to CSV"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer44.Add( self.export_csv_button, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer44, 0, wx.EXPAND, 5 )

        bSizer45 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, _(u"Simulation Results:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )

        self.m_staticText32.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer45.Add( self.m_staticText32, 0, wx.ALL, 5 )

        self.simulation_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.simulation_grid.CreateGrid( 6, 30 )
        self.simulation_grid.EnableEditing( True )
        self.simulation_grid.EnableGridLines( True )
        self.simulation_grid.EnableDragGridSize( False )
        self.simulation_grid.SetMargins( 0, 0 )

        # Columns
        self.simulation_grid.EnableDragColMove( False )
        self.simulation_grid.EnableDragColSize( True )
        self.simulation_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.simulation_grid.EnableDragRowSize( True )
        self.simulation_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.simulation_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.simulation_grid.SetMinSize( wx.Size( -1,168 ) )

        bSizer45.Add( self.simulation_grid, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer45, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer32 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


