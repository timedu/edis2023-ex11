
import json
from sys import stdout
from time import sleep, time

from supp.mq_config import  \
    reset_time_to_wait,     \
    MQ_TOPIC,               \
    MQ_PUBLISH_DELAY



# --
# Publish films
#

def publish_films(mq_client, films):

    # replace with actual code
    # --
    mq_client.publish(MQ_TOPIC, json.dumps({
        "name": "Le Havre",
        "genre": "Drama",
        "directed_by": "Aki Kaurismaki",
        "initial_release_date": "2011"
    }, indent=2))
    stdout.write('.')
    stdout.flush()
    # --

    

# --
# Last released films
#

_last_released_film_so_far = None

def last_released_film(_unused1, _unused2, msg):

    global _last_released_film_so_far

    try:
        
        # replace with actual code
        # --
        print('---\nthe latest film so far:', flush=True)
        print(json.dumps({
            "name": "Le Havre",
            "genre": "Drama",
            "directed_by": "Aki Kaurismaki",
            "initial_release_date": "2011"
        }, indent=2), flush=True)
        # --


        # uncomment this
        # reset_time_to_wait()

    except json.JSONDecodeError:
        pass

    except KeyError:
        pass



# --
# Top three genres
#

_genres_map = {}
_last_printed_genres_json = None

def top_three_genres(_unused1, _unused2, msg):

    global _genres_map, _last_printed_genres_json

    try:

        # replace with actual code
        # --
        print('---\nthe latest film so far:', flush=True)
        print(json.dumps([
            ["Documentary film", 57],
            ["Action Film", 53],
            ["Comedy", 40]
        ], indent=2), flush=True)
        # --


        # uncomment this
        # reset_time_to_wait()

    except json.JSONDecodeError:
        pass

    except KeyError:
        pass



# --
# Message rate
#

_message_counter = 0
_start_time = time()

def message_rate(_unused1, _unused2, msg):
    
    global _message_counter, _start_time
    
    try:

        # replace with actual code
        # --
        print(f'{3.14159265359:.2f} messages per second')
        # --


        # uncomment this
        # reset_time_to_wait()

    except json.JSONDecodeError:
        pass

    except KeyError:
        pass

    pass

