import requests
import sys

def main():
    url = "http://stats.nba.com/stats/playerdashptshotlog?"\
    "DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0" \
    "&Outcome=&Period=0&PlayerID=202322&Season=2014-15&SeasonSegment"\
    "=&SeasonType=Playoffs&TeamID=0&VsConference=&VsDivision="

    response = requests.get(url)
    response.raise_for_status()
    shots = response.json()['resultSets'][0]['rowSet']

    print shots[0]

if __name__ == "__main__":
    sys.exit(main())
