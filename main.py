""" An application for stereo image analysis with OpenCV """

import wx
from main_window import MainWindow


def main():
    """ Create main window """
    app = wx.App(False)
    frame = MainWindow("StereoLab")
    app.SetTopWindow(frame)
    app.MainLoop()

if __name__ == '__main__':
    main()
