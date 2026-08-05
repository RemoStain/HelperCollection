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
        """
        Convert pounds to kilograms.

        Args:
            pounds (float): The weight in pounds.

        Returns:
            float: The weight in kilograms.
        """
        return pounds * UnitConverter.LB_TO_KG

    @staticmethod
    def kg_to_lb(kilograms: float) -> float:
        """
        Convert kilograms to pounds.

        Args:
            kilograms (float): The weight in kilograms.

        Returns:
            float: The weight in pounds.
        """
        return kilograms / UnitConverter.LB_TO_KG


    # ----- Pressure -----
    @staticmethod
    def mmhg_to_kpa(mmhg: float) -> float:
        """
        Convert millimeters of mercury (mmHg) to kilopascals (kPa).

        Args:
            mmhg (float): The pressure in millimeters of mercury.

        Returns:
            float: The pressure in kilopascals.
        """
        return mmhg * UnitConverter.MMHG_TO_KPA

    @staticmethod
    def kpa_to_mmhg(kpa: float) -> float:
        """
        Convert kilopascals (kPa) to millimeters of mercury (mmHg).

        Args:
            kpa (float): The pressure in kilopascals.

        Returns:
            float: The pressure in millimeters of mercury.
        """
        return kpa / UnitConverter.MMHG_TO_KPA


    # ----- Length -----
    @staticmethod
    def ft_to_m(ft: float) -> float:
        """
        Convert feet to meters.

        Args:
            ft (float): The length in feet.

        Returns:
            float: The length in meters.
        """
        return ft * UnitConverter.FT_TO_M

    @staticmethod
    def m_to_ft(m: float) -> float:
        """
        Convert meters to feet.

        Args:
            m (float): The length in meters.

        Returns:
            float: The length in feet.
        """
        return m / UnitConverter.FT_TO_M


    # ----- Energy -----
    @staticmethod
    def kcal_to_kj(kcal: float) -> float:
        """
        Convert kilocalories (kcal) to kilojoules (kJ).
        
        Args:
            kcal (float): The energy in kilocalories.

        Returns:
            float: The energy in kilojoules.
        """
        return kcal * UnitConverter.KCAL_TO_KJ

    @staticmethod
    def kj_to_kcal(kj: float) -> float:
        """
        Convert kilojoules (kJ) to kilocalories (kcal/Cal).

        Args:
            kj (float): The energy in kilojoules.

        Returns:
            float: The energy in kilocalories.
        """
        return kj / UnitConverter.KCAL_TO_KJ


    # ----- Tempurature -----
    @staticmethod
    def f_to_c(f: float) -> float:
        """
        Convert Fahrenheit to Celsius.

        Args:
            f (float): The temperature in Fahrenheit.

        Returns:
            float: The temperature in Celsius.
        """
        return (f - 32) * (5/9)

    @staticmethod
    def c_to_f(c: float) -> float:
        """
        Convert Celsius to Fahrenheit.

        Args:
            c (float): The temperature in Celsius.

        Returns:
            float: The temperature in Fahrenheit.
        """
        return (c * (9/5)) + 32
