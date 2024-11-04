import sys
import heifer_generator


def list_cows(cows):
    list_of_cows = ''
    for cow in cows:
        cow = cow.get_name()
        list_of_cows += cow + ' '
    return list_of_cows
def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None
if __name__ == '__main__':
    cows = heifer_generator.get_cows()
    if sys.argv[1] == '-l':
        list_of_cows = list_cows(cows)
        print(f"Cows available: {list_of_cows}")
    elif sys.argv[1] == "-n":
        cow = find_cow(sys.argv[2], cows)
        if cow == None:
            print(f"Could not find {sys.argv[2]} cow!")
        else:
            message = ''
            for number, word in enumerate(sys.argv[3:]):
                if number == 0:
                    message += word
                else:
                    message += ' ' + word
            print(message)
            print(cow.get_image())
    else:
        message = ''
        for number, word in enumerate(sys.argv[1:]):
            if number == 0:
                message += word
            else:
                message += ' ' + word
        print(message)
        print(find_cow('heifer', cows).get_image())