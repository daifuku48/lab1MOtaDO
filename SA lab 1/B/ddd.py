
#клас партії, містить назву, інформацію та кількість голосів, які спочатку дорівнюють нулю
class Party:
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.votes = 0

    def add_votes(self, votes):
        self.votes += votes


class PollingStation:
    def __init__(self, number, address, head, members):
        self.number = number
        self.address = address
        self.head = head
        self.members = members
        self.results = {}

    def add_result(self, party, votes):
        self.results[party] = votes


class ElectionResults:
    def __init__(self, polling_stations):
        self.polling_stations = polling_stations
        self.party_results = {}

    def calculate_results(self):
        total_votes = 0
        for station in self.polling_stations:
            for party, votes in station.results.items():
                if party not in self.party_results:
                    self.party_results[party] = 0
                self.party_results[party] += votes
                total_votes += votes

        qualified_parties = {}
        for party, votes in self.party_results.items():
            if votes / total_votes >= 0.05:
                qualified_parties[party] = votes / total_votes * 100

        return qualified_parties


def main():
    # Створення дільниць та партій
    station1 = PollingStation(1, "вул. Пушкіна, 12", "Іванова Іванна", ["Петров Петро", "Сидорова Олена"])
    station2 = PollingStation(2, "вул. Леніна, 7", "Петров Петро", ["Іванов Іван", "Коваленко Марія"])
    party1 = PoliticalParty("Партія 1", "Інформація про Партію 1")
    party2 = PoliticalParty("Партія 2", "Інформація про Партію 2")
    party3 = PoliticalParty("Партія 3", "Інформація про Партію 3")
    party4 = PoliticalParty("Партія 4", "Інформація про Партію 4")
    party5 = PoliticalParty("Партія 5", "Інформація про Партію 5")

    # Додавання результатів виборів на кожну дільницю
    station1.add_result(party1, 120)
    station1.add_result(party2, 80)
    station1.add_result(party3, 50)
    station1.add_result(party4, 30)
    station2.add_result(party1, 70)
    station2.add_result(party2, 100)
    station2.add_result(party3, 90)
    station2.add_result(party4, 40)
    station2.add_result(party5, 3)

    # Створення результатів виборів та підведення підсумків
    results = ElectionResults([station1, station2])
    qualified_parties = results.calculate_results()

    # Виведення підсумків
    print("Партії, які набрали більше 5% голосів:")
    for party, percent in qualified_parties.items():
        print(party.name, ": ", round(percent, 2), "%")


if __name__ == '__main__': main()