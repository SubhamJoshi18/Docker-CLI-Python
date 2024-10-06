from exceptions.index import DockerException
from libs.option import ask_question
from utils.index import select_option
from fileUtils.index import clear_environment

def start_docker():

    try:
        clear_environment()
        print('Starting Docker Python')
        ask_question()
        choices = int(input('Enter Your Options'))
        select_option(choices)

    except DockerException as e:
        print(f'{e}')


start_docker()