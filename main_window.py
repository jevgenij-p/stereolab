""" A module for main window UI layout """

import wx
import cv2


class MainWindow(wx.Frame):
    """ Main window UI layout """

    def __init__(self, title):

        wx.Frame.__init__(self, None, title=title,
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        self.create_layout()
        self.create_menu()
        self.Show(True)

    def create_layout(self):
        """ Create UI layout elements """

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizerAndFit(sizer)

    def create_icon_panel(self):
        """ Create an icon panel layout """

        sizer = wx.BoxSizer(wx.VERTICAL)

    def create_menu(self):
        """ Create main menu """
        menu_file = wx.Menu()
        menu_exit = menu_file.Append(wx.ID_EXIT, "E&xit")

        menu_bar = wx.MenuBar()
        menu_bar.Append(menu_file, "&File")
        self.SetMenuBar(menu_bar)
