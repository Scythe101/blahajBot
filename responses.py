import random


def randomblahaj():
    rnd = random.randint(0, 19)
    image = 'images/blahaj' + str(rnd) + '.jpg'
    return image
    # return


def get_response(message: str):
    p_message = message.lower()
    if p_message == '/blahaj':
        
        return randomblahaj()
    if p_message == '/blåhaj':
        return randomblahaj()
