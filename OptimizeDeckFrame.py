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
## Class OptimizeDeckFrame
###########################################################################

class OptimizeDeckFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Little Alchemist Analyst"), pos = wx.DefaultPosition, size = wx.Size( 800,700 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2.SetMinSize( wx.Size( -1,50 ) )

        bSizer2.Add( ( 300, 0), 0, wx.EXPAND, 5 )

        self.card_library_button = wx.Button( self, wx.ID_ANY, _(u"Card Library"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.card_library_button, 0, wx.ALL, 5 )

        self.optimized_deck_button = wx.Button( self, wx.ID_ANY, _(u"Optimize Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.optimized_deck_button, 0, wx.ALL, 5 )

        self.test_deck_button = wx.Button( self, wx.ID_ANY, _(u"Test Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.test_deck_button, 0, wx.ALL, 5 )


        bSizer16.Add( bSizer2, 0, wx.EXPAND, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer18.Add( ( 400, 0), 0, wx.EXPAND, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"Optimize Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetFont( wx.Font( 19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer18.Add( self.m_staticText10, 0, wx.ALL, 5 )


        bSizer16.Add( bSizer18, 0, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer13.SetMinSize( wx.Size( -1,150 ) )

        bSizer13.Add( ( 310, 0), 0, wx.EXPAND, 5 )

        self.deck_1_button = wx.Button( self, wx.ID_ANY, _(u"Deck 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.deck_1_button, 0, wx.ALL, 5 )

        self.deck_2_button = wx.Button( self, wx.ID_ANY, _(u"Deck 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.deck_2_button, 0, wx.ALL, 5 )

        self.deck_3_button = wx.Button( self, wx.ID_ANY, _(u"Deck 3"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.deck_3_button, 0, wx.ALL, 5 )


        bSizer16.Add( bSizer13, 0, wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Mode:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer14.Add( self.m_staticText11, 0, wx.ALL, 5 )

        mode_choiceChoices = []
        self.mode_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mode_choiceChoices, 0 )
        self.mode_choice.SetSelection( 0 )
        bSizer14.Add( self.mode_choice, 0, wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, _(u"Custom (%):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        bSizer14.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.custom_percentage = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.custom_percentage.SetMinSize( wx.Size( 50,-1 ) )

        bSizer14.Add( self.custom_percentage, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, _(u"Deck Size:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        bSizer14.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.deck_size = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer14.Add( self.deck_size, 0, wx.ALL, 5 )

        self.optimize_deck_button = wx.Button( self, wx.ID_ANY, _(u"Optimize"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.optimize_deck_button, 0, wx.ALL, 5 )


        bSizer16.Add( bSizer14, 0, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, _(u"Add Card:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer15.Add( self.m_staticText13, 0, wx.ALL, 5 )

        add_card_choiceChoices = []
        self.add_card_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, add_card_choiceChoices, 0 )
        self.add_card_choice.SetSelection( 0 )
        self.add_card_choice.SetMinSize( wx.Size( 175,-1 ) )

        bSizer15.Add( self.add_card_choice, 0, wx.ALL, 5 )

        self.add_card_to_deck_button = wx.Button( self, wx.ID_ANY, _(u"Add Card"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.add_card_to_deck_button, 0, wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, _(u"Delete Card:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        bSizer15.Add( self.m_staticText14, 0, wx.ALL, 5 )

        delete_card_from_deck_choiceChoices = []
        self.delete_card_from_deck_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, delete_card_from_deck_choiceChoices, 0 )
        self.delete_card_from_deck_choice.SetSelection( 0 )
        self.delete_card_from_deck_choice.SetMinSize( wx.Size( 175,-1 ) )

        bSizer15.Add( self.delete_card_from_deck_choice, 0, wx.ALL, 5 )

        self.delete_card_from_deck_button = wx.Button( self, wx.ID_ANY, _(u"Delete Card"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.delete_card_from_deck_button, 0, wx.ALL, 5 )


        bSizer16.Add( bSizer15, 0, wx.EXPAND, 5 )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.deck_summary_txt = wx.StaticText( self, wx.ID_ANY, _(u"Deck Summary:"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.deck_summary_txt.Wrap( -1 )

        bSizer17.Add( self.deck_summary_txt, 0, wx.ALL, 5 )

        self.clear_deck_button = wx.Button( self, wx.ID_ANY, _(u"Clear Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.clear_deck_button, 0, wx.ALL, 5 )


        bSizer17.Add( ( 130, 0), 0, wx.EXPAND, 5 )

        self.deck_stats_txt = wx.StaticText( self, wx.ID_ANY, _(u"Deck Statistics:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.deck_stats_txt.Wrap( -1 )

        bSizer17.Add( self.deck_stats_txt, 0, wx.ALL, 5 )


        bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.save_deck_button = wx.Button( self, wx.ID_ANY, _(u"Save Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.save_deck_button, 0, wx.ALL, 5 )

        self.export_decks_button = wx.Button( self, wx.ID_ANY, _(u"Export to CSV"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.export_decks_button, 0, wx.ALL, 5 )


        bSizer21.Add( bSizer17, 0, wx.EXPAND, 5 )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        self.deck_summary_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 320,350 ), 0 )

        # Grid
        self.deck_summary_grid.CreateGrid( 35, 5 )
        self.deck_summary_grid.EnableEditing( True )
        self.deck_summary_grid.EnableGridLines( True )
        self.deck_summary_grid.EnableDragGridSize( False )
        self.deck_summary_grid.SetMargins( 0, 0 )

        # Columns
        self.deck_summary_grid.EnableDragColMove( False )
        self.deck_summary_grid.EnableDragColSize( True )
        self.deck_summary_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.deck_summary_grid.EnableDragRowSize( True )
        self.deck_summary_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.deck_summary_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer22.Add( self.deck_summary_grid, 0, wx.ALL, 5 )

        self.deck_statistics_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,350 ), 0 )

        # Grid
        self.deck_statistics_grid.CreateGrid( 35, 35 )
        self.deck_statistics_grid.EnableEditing( True )
        self.deck_statistics_grid.EnableGridLines( True )
        self.deck_statistics_grid.EnableDragGridSize( False )
        self.deck_statistics_grid.SetMargins( 0, 0 )

        # Columns
        self.deck_statistics_grid.EnableDragColMove( False )
        self.deck_statistics_grid.EnableDragColSize( True )
        self.deck_statistics_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.deck_statistics_grid.EnableDragRowSize( True )
        self.deck_statistics_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.deck_statistics_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer22.Add( self.deck_statistics_grid, 0, wx.ALL, 5 )


        bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


        bSizer19.Add( bSizer21, 1, wx.EXPAND, 5 )


        bSizer16.Add( bSizer19, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer16 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.optimize_deck_button.Bind( wx.EVT_BUTTON, self.optimize_deck )
        self.delete_card_from_deck_button.Bind( wx.EVT_BUTTON, self.delete_card_from_deck )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def optimize_deck( self, event ):
        event.Skip()

    def delete_card_from_deck( self, event ):
        event.Skip()


