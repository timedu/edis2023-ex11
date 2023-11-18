
from argparse import ArgumentParser

todo = {}


def _get_arguments():

    parser = ArgumentParser(
        description='Assignment 11'
    )

    parser.add_argument(
        '-r', '--review', choices=['0', '1', '2'], default='0',
        help='whose code is being run, default: 0 (your code)'
    ) 

    if parser.prog == 'pub.py':
        
        parser.add_argument(
            '-f', '--file_id', choices=['0', '1', '2'], default='0',
            help='which json file is read, default: 0 (films0.son)'
        ) 

    if parser.prog == 'sub.py':

        parser.add_argument(
            '-a', '--app', 
            choices=['last_released_film', 'message_rate', 'top_three_genres'], 
            help='which sub app to run'
        ) 

    return vars(parser.parse_args())


def _get_todo_folder(args):
    
    return 'your_code' if not int(args.get('review')) else f'review_{args["review"]}'     


def set_config():

    args = _get_arguments()

    if args['review'] == '1':
        from todos.review_1 import todo_module
    elif args['review'] == '2':
        from todos.review_2 import todo_module
    else:
        from todos.your_code import todo_module

    message_handler = args.get('app', 'publish_films')

    todo['message_handler'] = getattr(
        todo_module,
        message_handler
    )
    todo['file_id'] = args.get('file_id')

    print('***')
    print('*** todo folder:', _get_todo_folder(args))
    print('*** message handler:', message_handler)
    print('***')
