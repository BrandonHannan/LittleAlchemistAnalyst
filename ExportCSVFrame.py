# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class ExportCSVFrame
###########################################################################

class ExportCSVFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Export Deck"), pos = wx.DefaultPosition, size = wx.Size( 500,175 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer29 = wx.BoxSizer( wx.VERTICAL )


        bSizer29.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, _(u"Export Deck Statistics"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        self.m_staticText20.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer29.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer29.Add( ( 0, 25), 0, wx.EXPAND, 5 )

        bSizer30 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, _(u"Filename: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer30.Add( self.m_staticText22, 0, wx.ALL, 5 )

        self.csv_filename_txtctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer30.Add( self.csv_filename_txtctrl, 0, wx.ALL, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, _(u"Directory: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer30.Add( self.m_staticText21, 0, wx.ALL, 5 )

        self.directory_picker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.Size( 200,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer30.Add( self.directory_picker, 0, wx.ALL, 5 )


        bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer29.Add( bSizer30, 0, wx.EXPAND, 5 )


        bSizer29.Add( ( 0, 20), 0, wx.EXPAND, 5 )

        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.cancel_button = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer31.Add( self.cancel_button, 0, wx.ALL, 5 )

        self.save_button = wx.Button( self, wx.ID_ANY, _(u"Save CSV"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer31.Add( self.save_button, 0, wx.ALL, 5 )


        bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer29.Add( bSizer31, 0, wx.EXPAND, 5 )


        bSizer29.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer29 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


