from exceptions.index import DockerException
from libs.option import ask_question
from utils.index import select_option

def start_docker():

    try:

        print('Starting Docker Python')
        ask_question()
        choices = int(input('Enter Your Options'))
        select_option(choices)





    except DockerException as e:
        print(f'{e}')


start_docker()