from stravalib.client import Client
import pandas as pd
from stravalib import unithelper
from math import floor
import argparse

def main(access_token):
  client = Client(access_token=access_token)

  activities = client.get_activities(limit=1000)

  results = list(activities)

  # activity = client.get_activity(results[0].id)

  # print(activity.splits_metric)

  for result in results:
      activity = client.get_activity(result.id)

      # best_efforts = activity.best_efforts

      # for be in best_efforts:
      #   print be.elapsed_time

      splits = activity.splits_metric
      
      if len(splits) > 5:
        time = 0.0
        distance = 0.0
        for split in splits[:5]:
          time += split.moving_time.days * 1440.0 + split.moving_time.seconds / 60.0
          distance += float(split.distance)

        minutes = floor(time)
        seconds = (time - minutes) * 60.0
        print("Distance: "+str(distance)+" Time: "+str(minutes)+":"+str(seconds)+" Calories: "+str(activity.calories))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run data gathering on user.")

    parser.add_argument('--access-token', help='Strava API Client Secret',
                        action='store', required=True)
    args = parser.parse_args()

main(access_token=args.access_token)