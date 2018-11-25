class Person:

    def __init__(self, data):
        """
        :param data: dictionary - data about person
        """
        self.data = data

    def get_id(self):
        """
        :return: int - id of the person
        """
        return self.data["id"]

    def count_sustainability_percentage(self, max_values):
        """
        Cannot be more than 1, rounded to 2nd decimal after dot. Return a measurement of environmentally frienliness
        of a person
        :param max_values: collection with three int values - max electricity, max volume of used water, of gas
        :return: double [0..1]
        """
        max_electricity, max_water, max_gas = max_values[0], max_values[1], max_values[2]
        return round((0.4 * self.get_electricity_usage() / max_electricity +
                      0.3 * (self.get_water_usage() / max_water + self.get_gas_usage() / max_gas)), 2)

    def get_electricity_usage(self):
        """
        :return: int - kWHs of electricity
        """
        return self.data["electricity_usage"]

    def get_water_usage(self):
        """
        :return: int - volume of used water in m^3
        """
        return self.data["water_usage"]

    def get_gas_usage(self):
        """
        :return: int - volume of used gas in m^3
        """
        return self.data["gas_usage"]
