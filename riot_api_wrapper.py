import json
import requests


def main():
    # This is my API key
    api_key = "api-key-here"

    # Create RiotAPIWrapper object using api_key
    api_wrapper = RiotAPIWrapper(api_key)

    response_dict = api_wrapper.api_account_v1('Minsoo', 'NA 1')

    print(f'Got the puuid: {response_dict["puuid"]}')
    print(f'For the user : {response_dict["gameName"]}#{response_dict["tagLine"]} ')

    response_dict = api_wrapper.api_account_v1('Soju', 'KR33')

    print(f'Got the puuid: {response_dict["puuid"]}')
    print(f'For the user : {response_dict["gameName"]}#{response_dict["tagLine"]} ')


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
