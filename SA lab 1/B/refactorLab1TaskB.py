class Party:

    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.votes = 0

    def __str__(self):
        return f"{self.name} {self.info} {self.votes}"

    def add_votes(self, votes):
        self.votes += votes

    def get_percentage(self, total_votes):
        return self.votes / total_votes


class District:

    def __init__(self, id_, address, head, members):
        self.id = id_
        self.address = address
        self.head = head
        self.members = members
        self.results = {}

    def add_votes(self, party, votes):
        self.results.setdefault(party, 0)
        self.results[party] += votes

    def __str__(self):
        return f"{self.id} {self.results} {self.head} {self.members} {self.address}"


class ElectionParty:

    def __init__(self):
        self.parties = []
        self.districts = []
        self.total_votes = 0

    def read_file(self, file_parties, file_districts):
        try:
            with open(file_parties, "r") as file:
                while True:
                    line_party = file.readline()
                    if not line_party:
                        break
                    line_party = line_party.strip().split(",")
                    party = Party(line_party[0], line_party[1])
                    self.parties.append(party)
            with open(file_districts, "r") as file:
                while True:
                    lines_head_members = file.readline()
                    if not lines_head_members:
                        break
                    district_data = lines_head_members.strip().split(',')
                    lines_party_votes = file.readline()
                    if not lines_party_votes:
                        break
                    party_votes_data = lines_party_votes.strip().split(',')
                    party_votes_data_dict = {}
                    for party in party_votes_data:
                        key, value = party.split(':')
                        party_votes_data_dict[key] = int(value)
                    district = District(district_data[0], district_data[1], district_data[2],
                                        district_data[3:len(district_data)])
                    district.results = party_votes_data_dict
                    self.districts.append(district)
        except FileNotFoundError:
            print("File not found. Please check if the file name and path are correct.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

    def calculate_results(self):
        for district in self.districts:
            for party, votes in district.results.items():
                self.total_votes += int(votes)
                for item_party in self.parties:
                    if item_party.name == party:
                        item_party.add_votes(int(votes))
        else:
            for party in self.parties:
                percentage = party.get_percentage(self.total_votes)
                if percentage >= 0.05:
                    print(f'{party.name}: {percentage:.2%}')


def main():
    elections = ElectionParty()
    elections.read_file("election_party.txt", "election_districts.txt")
    elections.calculate_results()


if __name__ == "__main__":
    main()
