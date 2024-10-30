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
## Class DeckFrame
###########################################################################

class DeckFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Little Alchemist Analyst"), pos = wx.DefaultPosition, size = wx.Size( 800,700 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2.SetMinSize( wx.Size( -1,250 ) )

        bSizer2.Add( ( 300, 0), 0, wx.EXPAND, 5 )

        self.card_library_button = wx.Button( self, wx.ID_ANY, _(u"Card Library"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.card_library_button, 0, wx.ALL, 5 )

        self.optimized_deck_button = wx.Button( self, wx.ID_ANY, _(u"Optimize Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.optimized_deck_button, 0, wx.ALL, 5 )

        self.test_deck_button = wx.Button( self, wx.ID_ANY, _(u"Test Deck"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.test_deck_button, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer2, 0, wx.EXPAND, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Current Library"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.card_library_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.card_library_grid.CreateGrid( 5, 3 )
        self.card_library_grid.EnableEditing( True )
        self.card_library_grid.EnableGridLines( True )
        self.card_library_grid.EnableDragGridSize( False )
        self.card_library_grid.SetMargins( 0, 0 )

        # Columns
        self.card_library_grid.EnableDragColMove( False )
        self.card_library_grid.EnableDragColSize( True )
        self.card_library_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.card_library_grid.EnableDragRowSize( True )
        self.card_library_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.card_library_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer11.Add( self.card_library_grid, 0, wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Load Card Library from Andersam Optimizer:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer12.Add( self.m_staticText8, 0, wx.ALL, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.file_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select Andersam Optimizer Excel file"), _(u"CSV files (*.csv)|*.csv|Excel files (*.xls;*.xlsx)|*.xls;*.xlsx"), wx.DefaultPosition, wx.Size( 200,-1 ), wx.FLP_DEFAULT_STYLE )
        bSizer14.Add( self.file_picker, 0, wx.ALL, 5 )


        bSizer14.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.load_andersam_optimizer_button = wx.Button( self, wx.ID_ANY, _(u"Load Cards"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.load_andersam_optimizer_button, 0, wx.ALL, 5 )


        bSizer12.Add( bSizer14, 0, wx.EXPAND, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Add Card:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer12.Add( self.m_staticText9, 0, wx.ALL, 5 )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        card_name_choiceChoices = []
        self.card_name_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), card_name_choiceChoices, 0 )
        self.card_name_choice.SetSelection( 0 )
        gbSizer1.Add( self.card_name_choice, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        card_level_choiceChoices = []
        self.card_level_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 75,-1 ), card_level_choiceChoices, 0 )
        self.card_level_choice.SetSelection( 0 )
        gbSizer1.Add( self.card_level_choice, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        fusion_choiceChoices = []
        self.fusion_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 75,-1 ), fusion_choiceChoices, 0 )
        self.fusion_choice.SetSelection( 0 )
        gbSizer1.Add( self.fusion_choice, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.card_amount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        gbSizer1.Add( self.card_amount, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.add_card_button = wx.Button( self, wx.ID_ANY, _(u"Add Card"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.add_card_button, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        delete_card_choiceChoices = []
        self.delete_card_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), delete_card_choiceChoices, 0 )
        self.delete_card_choice.SetSelection( 0 )
        gbSizer1.Add( self.delete_card_choice, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.delete_card_button = wx.Button( self, wx.ID_ANY, _(u"Delete Card"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.delete_card_button, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"Save Current Card Library:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        gbSizer1.Add( self.m_staticText10, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.save_card_library_button = wx.Button( self, wx.ID_ANY, _(u"Save Card LIbrary"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.save_card_library_button, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        bSizer41 = wx.BoxSizer( wx.VERTICAL )


        bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Combo Card:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer41.Add( self.m_staticText2, 0, wx.ALL, 5 )


        gbSizer1.Add( bSizer41, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )


        bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Level:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )


        gbSizer1.Add( bSizer5, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Fusion:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )


        gbSizer1.Add( bSizer6, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer61 = wx.BoxSizer( wx.VERTICAL )


        bSizer61.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, _(u"Amount:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )

        bSizer61.Add( self.m_staticText41, 0, wx.ALL, 5 )


        gbSizer1.Add( bSizer61, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )


        bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"Delete Card:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer10.Add( self.m_staticText7, 0, wx.ALL, 5 )


        gbSizer1.Add( bSizer10, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


        bSizer12.Add( gbSizer1, 1, wx.EXPAND, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer11, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.load_andersam_optimizer_button.Bind( wx.EVT_BUTTON, self.load_andersam_optimizer )
        self.add_card_button.Bind( wx.EVT_BUTTON, self.add_card_to_library )
        self.delete_card_button.Bind( wx.EVT_BUTTON, self.delete_card_from_library )
        self.save_card_library_button.Bind( wx.EVT_BUTTON, self.save_user_card_library )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def load_andersam_optimizer( self, event ):
        event.Skip()

    def add_card_to_library( self, event ):
        event.Skip()

    def delete_card_from_library( self, event ):
        event.Skip()

    def save_user_card_library( self, event ):
        event.Skip()


