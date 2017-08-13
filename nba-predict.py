import requests
import json

def main():
    data = {'name': 'jokic'}
    r = requests.post('https://nba-api.therendersports.com/player/findFromName', json=data)
    r = r.json()
    print(r)

if __name__ == '__main__':
    main()
