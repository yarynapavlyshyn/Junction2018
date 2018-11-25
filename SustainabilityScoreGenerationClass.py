from PersonClass import Person
import requests


class SustainabilityScoreGeneration:

    def __init__(self, _link):
        """
        Create txt file where score of every person is computed.
        :param _link: str - txt file with data
        """
        r = requests.get(_link)
        self.data = r.json()
        self.size = len(self.data)
        self.sorted = False
        self.modified = False

    def get_average_score(self):
        """
        Calculate score - percentage of sustainability of a person life
        :return: decimal - from 1 to 0
        """

        return round(sum(p.count_sustainability_percentage for p in [Person(person_info) for person_info in self.data])
                     / self.size, 2)

    def count_max_usage_values(self):
        max_electricity = 0
        max_water = 0
        max_gas = 0
        for person in self.data:
            if person["electricity_usage"] > max_electricity:
                max_electricity = person["electricity_usage"]
            if person["water_usage"] > max_water:
                max_water = person["water_usage"]
            if person["gas_usage"] > max_gas:
                max_gas = person["gas_usage"]
        return max_electricity, max_water, max_gas

    def modify_data_by_adding_scores(self):
        """
        :return: the same json file expanded by adding score value
        """
        self.modified = True
        for p in self.data:
            p["score"] = Person(p).count_sustainability_percentage(self.count_max_usage_values())

    def sort_by_scores(self):
        """
        Sort only if the data was modified
        """
        if not self.modified: self.modify_data_by_adding_scores()
        self.data = sorted(self.data, key=lambda k: k["score"], reverse=True)
        self.sorted = True

    def pick_the_winner(self):
        """
        :return: None or all the data of the person who's score is the highest
        """
        if not self.data: return
        if not self.sorted: self.sort_by_scores()
        return self.data[0]

    def __str__(self):
        """
        String representation
        :return: all the data about persons line by line
        """
        result = ""
        for p in self.data:
            result += p + "\n"
        return result

link = "http://10.100.39.132:8000/data"
s = SustainabilityScoreGeneration(link)
s.sort_by_scores()
print(s)