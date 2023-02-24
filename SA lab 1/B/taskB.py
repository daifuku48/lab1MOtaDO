# класс партії, доступне ім'я, інформація, та кількість голосів, об'явлені геттери та сеттери
# для інкапсуляції
class Party:

    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.votes = 0

    def __str__(self):
        return f"{self.name} {self.info} {self.votes}"

    def get_votes(self):
        return self.votes

    def get_info(self):
        return self.info

    def get_name(self):
        return self.name

    def add_votes(self, votes):
        if not isinstance(votes, int):
            raise TypeError("Votes must be an integer.")
        self.votes += votes

    def set_votes(self, votes):
        if not isinstance(votes, int):
            raise TypeError("Votes must be an integer.")
        self.votes = votes

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self.name = name

    def set_info(self, info):
        if not isinstance(info, str):
            raise TypeError("Info must be a string.")
        self.info = info

    def get_percentage(self, total_votes):
        return self.votes / total_votes


# дільниця
class District:

    def __init__(self, id_, address, head, members):
        self.id = id_
        self.address = address
        self.head = head
        self.members = members
        self.results = {}

    def set_id(self, id_):
        if not isinstance(id_, str):
            raise TypeError("id must be a string.")
        self.id = id_

    def set_address(self, address):
        if not isinstance(address, str):
            raise TypeError("Address must be a string.")
        self.address = address

    def set_head(self, head):
        if not isinstance(head, str):
            raise TypeError("Head must be a string.")
        self.head = head

    def set_members(self, members):
        if not isinstance(members, list):
            raise TypeError("Members must be a list.")
        self.members = members

    def set_results(self, results):
        if not isinstance(results, dict):
            raise TypeError("Results must be a dictionary.")
        self.results = results

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def get_head(self):
        return self.head

    def get_members(self):
        return self.members

    def get_results(self):
        return self.results

    def add_results(self, party, votes):
        if not isinstance(party, Party):
            raise TypeError("Party must be an instance of the Party class.")
        if not isinstance(votes, int):
            raise TypeError("Votes must be an integer.")
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
                    flag = 0
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
                    district.set_results(party_votes_data_dict)
                    self.districts.append(district)
        except FileNotFoundError:
            print("File not found. Please check if the file name and path are correct.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

    def calculate_results(self):
        try:
            for district in self.districts:
                for party, votes in district.results.items():
                    self.total_votes += int(votes)
                    for item_party in self.parties:
                        if item_party.get_name() == party:
                            item_party.add_votes(int(votes))
            else:
                for party in self.parties:
                    percentage = party.get_percentage(self.total_votes)
                    if percentage >= 0.05:
                        print(f'{party.name}: {percentage:.2%}')

        except Exception as e:
            print(f"An error occurred while calculating the results: {str(e)}")

    def set_district_address(self, district_number, new_address):
        try:
            for district in self.districts:
                if district.id == district_number:
                    district.set_address(new_address)
                    break
            else:
                print(f"District {district_number} not found.")
        except Exception as e:
            print(f"An error occurred while setting the district address: {str(e)}")

    def set_district_head(self, district_number, new_head):
        try:
            for district in self.districts:
                if district.number == district_number:
                    district.set_head(new_head)
                    break
            else:
                print(f"District {district_number} not found.")
        except Exception as e:
            print(f"An error occurred while setting the district head: {str(e)}")

    def set_district_members(self, district_number, new_members):
        try:
            for district in self.districts:
                if district.number == district_number:
                    district.set_members(new_members)
                    break
            else:
                print(f"District {district_number} not found.")
        except Exception as e:
            print(f"An error occurred while setting the district members: {str(e)}")

    def set_district_votes_for_party(self, district_number, party_name, new_votes):
        try:
            for district in self.districts:
                if district.number == district_number:
                    district.set_votes_for_party(party_name, new_votes)
                    break
            else:
                print(f"District {district_number} not found.")
        except Exception as e:
            print(f"An error occurred while setting the district votes for party: {str(e)}")

    def set_party_name(self, party_name, new_name):
        try:
            for party in self.parties:
                if party.name == party_name:
                    party.set_name(new_name)
                    break
            else:
                print(f"Party {party_name} not found.")
        except Exception as e:
            print(f"An error occurred while setting the party name: {str(e)}")


def main():
    elections = ElectionParty()
    elections.read_file("election_party.txt", "election_districts.txt")
    elections.calculate_results()


if __name__ == "__main__":
    main()
