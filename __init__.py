from BaseEfficientFrontier import EfficientFrontier


def TechSector():
    x = EfficientFrontier(("APT.AX", "XRO.AX", "NEA.AX", "EML.AX"),40000)
    x.ImportFromYahooFinance()
    x.MathsMethods()
    return x.Findings()


def BigBanks():
    x = EfficientFrontier(("NAB.AX", "ANZ.AX", "CBA.AX", "WBC.AX", "MQG.AX"),40000)
    x.ImportFromYahooFinance()
    x.MathsMethods()
    return x.Findings()


TechSector = TechSector()
BigBanks = BigBanks()
