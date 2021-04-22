# Basic class in Python
# NXPython/shapes/Block.py (shapes folder in the same place as hello.py file)
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


class Block:

    #    length = 0         # class variable shared by all instances
    #	width = ...

    def getVolume(self):
        return self.length * self.width * self.height

    def __init__(self, x, y, z, length, width, height, color, material):
        self.length = length    # instance variable unique to each instance
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.material = material

    def initForNX(self, x, y, z, length, width, height, color, material):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The block
        blockfeaturebuilder1 = workPart.Features.CreateBlockFeatureBuilder(
            NXOpen.Features.Block.Null)
        blockfeaturebuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths

        origBlock = NXOpen.Point3d(float(x), float(y), float(z))
        blockfeaturebuilder1.SetOriginAndLengths(
            origBlock, str(length), str(width), str(height))
        blockfeaturebuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

        self.body = blockfeaturebuilder1.Commit().GetBodies()[0]
        origBlock.SetName("The Block")
        blockfeaturebuilder1.Destroy()

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The block
        blockfeaturebuilder1 = workPart.Features.CreateBlockFeatureBuilder(
            NXOpen.Features.Block.Null)
        blockfeaturebuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths

        origBlock = NXOpen.Point3d(float(self.x), float(self.y), float(self.z))
        blockfeaturebuilder1.SetOriginAndLengths(origBlock, str(
            self.length), str(self.width), str(self.height))
        blockfeaturebuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

        self.body = blockfeaturebuilder1.Commit().GetBodies()[0]
        blockfeaturebuilder1.Destroy()

    def subtract(self, tool):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        subtractfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(
            NXOpen.Features.BooleanFeature.Null)

        # bodyTarget_.GetBodies()[0] # From where to subtract
        subtractfeaturebuilder1.Target = self.body
        subtractfeaturebuilder1.Tool = tool  # What to subtract
        subtractfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Subtract

        subtractfeaturebuilder1.Commit()
        subtractfeaturebuilder1.Destroy()

    def intersect(self, tool):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        intersectfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(
            NXOpen.Features.BooleanFeature.Null)

        # bodyTarget_.GetBodies()[0] # From where to intersect
        intersectfeaturebuilder1.Target = self.body
        intersectfeaturebuilder1.Tool = tool  # What to intersect

        intersectfeaturebuilder1.RetainTool = True

        intersectfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Intersect

        returnObj = intersectfeaturebuilder1.Commit()
        print("BigAssDagga")
        returnObj.Print()
        intersectfeaturebuilder1.Destroy()

    def blend(self, x1, y1, z1, x2, y2, z2):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(
            NXOpen.Features.Feature.Null)
        scCollector1 = workPart.ScCollectors.CreateCollector()
        edges = [NXOpen.Edge.Null] * 1
        for edge in self.body.GetEdges():
            vertex, vertex2 = edge.GetVertices()
            tmp = (vertex.X, vertex.Y, vertex.Z)
            tmp2 = (vertex2.X, vertex2.Y, vertex2.Z)
            if (x1, y1, z1) == tmp:
                if (x2, y2, z2) == tmp2:
                    edges[0] = edge
            elif (x1, y1, z1) == tmp2:
                if (x2, y2, z2) == tmp:
                    edges[0] = edge

        ruleEdgeDumb1 = workPart.ScRuleFactory.CreateRuleEdgeDumb(edges)
        rules2 = [None] * 1
        rules2[0] = ruleEdgeDumb1
        scCollector1.ReplaceRules(rules2, True)
        edgeBlendBuilder1.AddChainset(scCollector1, "8")
        edgeBlendBuilder1.CommitFeature()
        edgeBlendBuilder1.Destroy()
