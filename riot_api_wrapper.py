import json
import requests


# Riot API Wrapper class (Object Oriented Programming)
class RiotAPIWrapper:
    def __init__(self, api_key):
        # This class is going to hold onto a member variable
        # called api_key. The member variable is denoted by "self"
        self.api_key = api_key


    # This is a member function. A function that is part of the class.
    def api_account_v1(self, gameName, tagLine):
        new_tagLine = self._check_tagLine(tagLine)

        get_request_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{new_tagLine}?api_key={self.api_key}"

        # Make API call
        response = requests.get(get_request_url)

        response_dict = json.loads(response.content)

        return response_dict

    def api_match_history_v5(self, gameName, tagLine):
        # blah

        return blah

    def _check_tagLine(self, tagLine):
        if ' ' in tagLine:
            return tagLine.replace(' ', '%20')
        return tagLine


if __name__ == '__main__':
    main()
