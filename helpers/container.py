from config.dockerConfig import docker_client
from exceptions.index import DockerContainerException
from abc import ABC,abstractmethod
from docker.errors import ImageNotFound
from datetime import datetime
from helpers.image import DockerImage
from jsonUtils.Container.ContainerJson import store_containers_json


docker_image = DockerImage()


class DockerContainerAbs(ABC):



    @abstractmethod
    def list_running_container(self):
        pass

    @abstractmethod
    def list_container(self):
        pass


    @abstractmethod
    def run_container(self,image_name,command=None):
        pass




class DockerContainer(DockerContainerAbs, ABC):

    def list_running_container(self):
        running_container_name  = []
        try:

            running_container = docker_client.containers.list()


            print(running_container)
            return running_container

        except DockerContainerException as e:
            print(f'Error in Docker Container : {e}')

        except Exception as e:
            print(f'An Error Occur : {e}')


    def list_container(self):
        container_name = []
        try:

            containers = docker_client.containers.list(all=True)

            for index , container in enumerate(containers):
                container_name.append(container.name)


            if len(container_name)  == 0 or not container_name:
                raise DockerContainerException('There is no container on your Docker Engine')

            store_containers_json(container_name)

            return container_name

        except DockerContainerException as e:
            print(f'Docker Container Captured An Error : {e}')

        except Exception as e:
            print(f'An Error Occur {e}')


    def run_container(self,image_name,command=None):

        try:
            all_images = docker_image.list_images()



            image = image_name.strip()

            exists_image = docker_client.images.get(image)

            if not exists_image or image_name not in all_images:
                raise ImageNotFound('Image does not found')



            if command:
                print('Running Docker Container')

                container = docker_client.containers.run(image_name,command.split(' '),detach=True)

                print(f'{container.id} is running  {datetime.now()}')



            container = docker_client.containers.run(image_name,detach=True)

            print(f'{container.id} is running on {datetime.now()}')


        except ImageNotFound as e:

            print(f'Image Does not Exists , Pulling Image',)
            docker_client.images.pull(image_name)
            print('Image Pulled SuccessFully')


        except DockerContainerException as e:
            print(f'Error in Docker Container : {e}')

        except Exception as e:
            print(f'An Error Occur : {e}')
