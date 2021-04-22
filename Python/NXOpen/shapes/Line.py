import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


class Line:

    def __init__(self, StartPoint, EndPoint, weldable):
        self.startPoint = StartPoint
        self.endPoint = EndPoint
        self.weldable = weldable

    # instance variable unique to each instance
    def initForNX(self):
        self.__createLine()

    def __createLine(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        self.line = workPart.Curves.CreateLine(self.startPoint, self.endPoint)

        if (self.weldable):
            self.line.Color = 36
        else:
            self.line.Color = 186
        self.line.LineWidth = NXOpen.DisplayableObject.ObjectWidth.Thick
        self.line.RedisplayObject()
        self.line.SetVisibility(NXOpen.SmartObjectVisibilityOption.Visible)
