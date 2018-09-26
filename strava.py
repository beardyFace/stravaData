from stravalib.client import Client
import pandas as pd
from stravalib import unithelper
from math import floor
import argparse

def main(access_token):
  client = Client(access_token=access_token)

  activities = client.get_activities(limit=1000)

  results = list(activities)

  best_times = []
  for result in results:
      activity = client.get_activity(result.id)

      best_efforts = activity.best_efforts

      for be in best_efforts:
        if float(be.distance) > 4900 and float(be.distance) < 5100:
          best_times.append(be.elapsed_time)
    
  best_times.sort()
  for time in best_times:
    print time

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run data gathering on user.")

    parser.add_argument('--access-token', help='Strava API Client Secret',
                        action='store', required=True)
    args = parser.parse_args()

main(access_token=args.access_token)