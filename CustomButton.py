import wx
import wx.lib.newevent

# Create a custom event for the button click
ParallelogramButtonEvent, EVT_PARALLELOGRAM_BUTTON = wx.lib.newevent.NewCommandEvent()

class ParallelogramButton(wx.Panel):
    def __init__(self, parent, label="", id=wx.ID_ANY, size=(200, 70), skew=30):
        super().__init__(parent, id, size=size)

        self.label = label
        self.skew = skew  # Skew defines the horizontal offset to create the parallelogram shape

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)

        # Bind paint and mouse events
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnHover)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)

        # State variables for hover effect
        self.is_hovered = False

    def OnPaint(self, event):
        width, height = self.GetSize()
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        # Set colors based on hover state
        fill_color = wx.Colour(100, 149, 237) if self.is_hovered else wx.Colour(72, 61, 139)
        gc.SetBrush(wx.Brush(fill_color))
        gc.SetPen(wx.Pen(wx.Colour(0, 0, 0), 2))  # Black border

        # Define the points for a parallelogram
        path = gc.CreatePath()
        path.MoveToPoint(self.skew, 0)  # Top-left (skew offset)
        path.AddLineToPoint(width, 0)  # Top-right
        path.AddLineToPoint(width - self.skew, height)  # Bottom-right (skew offset)
        path.AddLineToPoint(0, height)  # Bottom-left
        path.CloseSubpath()

        gc.DrawPath(path)

        # Draw the label in the center
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        gc.SetFont(font, wx.Colour(255, 255, 255))
        tw, th = gc.GetTextExtent(self.label)
        gc.DrawText(self.label, (width - tw) / 2, (height - th) / 2)

    def OnClick(self, event):
        # Fire a custom button event
        evt = ParallelogramButtonEvent(self.GetId())
        wx.PostEvent(self.GetParent(), evt)

    def OnHover(self, event):
        self.is_hovered = True
        self.Refresh()

    def OnLeave(self, event):
        self.is_hovered = False
        self.Refresh()