
import json
from os.path import dirname, join

from supp.mq_config import connect, disconnect
from supp.app_config import set_config, todo


def get_films(file_id):

    films_path = join(
        dirname(__file__), 
        'data',
        f'films{file_id}.json'
    )
    with open(films_path) as films_file:
        films = json.load(films_file)["films"]
    return films


if __name__ == '__main__':

    set_config()

    try:

        films = get_films(todo['file_id'])  
        mq_client = connect()

        print(f"starting to publish films ({todo['file_id']})")
        todo['message_handler'](mq_client, films)
        print(f"\nno more films to publish ({todo['file_id']})")

        disconnect(mq_client)

    except KeyboardInterrupt:

        disconnect(mq_client)
        print()
