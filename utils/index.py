from constant.DockerConstant import create_container, run_container, pull_image, list_container
from helpers.container import DockerContainer
from helpers.image import DockerImage



docker_container = DockerContainer()
docker_image = DockerImage()


def select_option(choice):
    match choice:
        case 1:
            print("Listing container...")
            result =  docker_container.list_container()
            return result
        case 3:
            print("Listing Images...")
            # Add logic to run a container
            result = docker_image.list_images()
            return result

        case 2:
            print("Pulling image...")
            image_name = str(input('Enter The Image You want to Pull'))
            result = docker_image.pull_image(image_name)
            return result
        case 4:
            print("Listing All Running containers...")
            result = docker_container.list_running_container()
            return result

        case 5:
            print('Running Containers...')
            image_name = str(input('Enter The Image you want to run'))
            command = str(input('Enter the command you want to run'))
            result = docker_container.run_container(image_name,command)
            return result

        case 6:
            print('Deleting Image.....')
            image_name = str(input('Enter The Image You want to Delete: '))
            result = docker_image.delete_image(image_name)
            return result


        case _:  # Wildcard case for any unmatched input
            print("Invalid option selected.")
