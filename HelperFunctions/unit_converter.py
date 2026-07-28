#WIP

class UnitConverter:



    # Unit conversions

    # Mass
    LB_TO_KG = 0.45359237

    # Pressure
    MMHG_TO_KPA = 0.133322387415

    # Length
    FT_TO_M = 0.3048

    # Energy
    KCAL_TO_KJ = 4.184

    # Tempurature
    # SEE FUNCTION

    # ----- Mass -----
    @staticmethod
    def lb_to_kg(pounds: float) -> float:
        return pounds * UnitConverter.LB_TO_KG

    @staticmethod
    def kg_to_lb(kilograms: float) -> float:
        return kilograms / UnitConverter.LB_TO_KG

    # ----- Pressure -----
    @staticmethod
    def mmhg_to_kpa(mmhg: float) -> float:
        return mmhg * UnitConverter.MMHG_TO_KPA

    @staticmethod
    def kpa_to_mmhg(kpa: float) -> float:
        return kpa / UnitConverter.MMHG_TO_KPA

    # ----- Length -----
    @staticmethod
    def ft_to_m(ft: float) -> float:
        return ft * UnitConverter.FT_TO_M

    @staticmethod
    def m_to_ft(m: float) -> float:
        return m / UnitConverter.FT_TO_M

    # ----- Energy -----
    @staticmethod
    def kcal_to_kj(kcal: float) -> float:
        return kcal * UnitConverter.KCAL_TO_KJ

    @staticmethod
    def kj_to_kcal(kj: float) -> float:
        return kj / UnitConverter.KCAL_TO_KJ


    # ----- Tempurature -----
    @staticmethod
    def f_to_c(f: float) -> float:
        return (f - 32) * (5/9)

    @staticmethod
    def c_to_f(c: float) -> float:
        return (c * (9/5)) + 32