from riot_api_wrapper import RiotAPIWrapper

def main():
    api_key = "api-key-here"

    api_wrapper = RiotAPIWrapper(api_key)

    print_account_info(api_wrapper, 'Minsoo', 'NA 1')
    print_account_info(api_wrapper, 'Soju'  , 'KR33')


def print_account_info(api_wrapper, gameName, tagLine):
    response_dict = api_wrapper.api_account_v1(gameName, tagLine)

    print(f'Got the puuid: {response_dict["puuid"]}')
    print(f'Got the user : {response_dict["gameName"]}#{response_dict["tagLine"]}')

if __name__ == '__main__':
    main()
