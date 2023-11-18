
from supp.mq_config \
import connect, disconnect, is_time_to_wait, MQ_TOPIC

from supp.app_config import set_config, todo


if __name__ == '__main__':

    set_config()

    try:

        mq_client = connect()
        mq_client.on_message = todo['message_handler']

        mq_client.subscribe(MQ_TOPIC)
        print('waiting for messages ...')
        
        while True: 
            if not is_time_to_wait(): break

        print(f'no messages within the expected time')            
        disconnect(mq_client)

    except KeyboardInterrupt:

        disconnect(mq_client)
        print()
