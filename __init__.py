from BaseEfficientFrontier import EfficientFrontier


def TechSector():
    x = EfficientFrontier(("APT.AX", "XRO.AX", "NEA.AX", "EML.AX"))
    x.ImportFromYahooFinance()
    x.MathsMethods()
    return x.Findings()


def BigBanks():
    x = EfficientFrontier(("NAB.AX", "ANZ.AX", "CBA.AX", "WBC.AX", "MQG.AX"))
    x.ImportFromYahooFinance()
    x.MathsMethods()
    return x.Findings()




# TechSector = TechSector()

BigBanks = BigBanks()
