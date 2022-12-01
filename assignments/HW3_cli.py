""" CLI program to for HW3 homework """
# Shreya Karmakar
import argparse

if __name__ == "__main__":
    # Set up argparse parser and arguments here
    parser = argparse.ArgumentParser(
        epilog='Does print, combine, then len. '
               'If no flags given, does nothing.'
    )
    # Add the arguments here
    parser.add_argument('texts',
                        help='Input strings to operate on',
                        nargs='+')
    parser.add_argument('-p',
                        '--print',
                        help='Just print the input strings',
                        action='store_true')
    parser.add_argument('-c',
                        '--combine',
                        help='Print input strings combined in a continuous'
                        'string',
                        action='store_true')
    parser.add_argument('-l',
                        '--len',
                        help='Print each string with its index and length',
                        action='store_true')

    args = parser.parse_args()
    # execute whatever the flags say to do here in the correct order.
    if args.print:
        print(' '.join(args.texts))
    if args.combine:
        print(''.join(args.texts))
    if args.len:
        for i, word in enumerate(args.texts, 1):
            print(f'Word  # {i} is "{word}" and has {len(word)} letter(s)')
    # If you prefer to call a single main() function written above the
    # if __name__ == "__main__":
    # statement, that is OK with me.
    # The important thing is to make it work correctly. ;-)
    # But don't overthink things.
