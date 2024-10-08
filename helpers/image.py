from abc import ABC,abstractmethod
from exceptions.index import DockerImageException
from config.dockerConfig import docker_client
from docker.errors import ImageNotFound
from docker.errors import APIError
from exceptions.index import DockerException
from docker.errors import DockerException
from datetime import datetime
from jsonUtils.Image.ImageJson import store_image_pull_logs
from jsonUtils.Image.ImageJson import store_image_list
from jsonUtils.Image.ImageJson import store_deleted_image
from extraction.ExtractText import translate


class DockerImageAbs(ABC):


    @abstractmethod
    def pull_image(self,image_name):
        pass

    @abstractmethod
    def list_images(self):
        pass

    @abstractmethod
    def delete_image(self,image_name):
        pass



class DockerImage(DockerImageAbs,ABC):


  def pull_image(self, image_name):
    images = []
    try:

        all_images = docker_client.images.list(all=True)

        for image in all_images:
            if image:
                images.append(image)

        print(f'Total {len(images)} are there in your docker engine')


        image_name = image_name.strip()


        check_images = docker_client.images.get(image_name)

        if not check_images:
            raise ImageNotFound('Image Does not Exists')


        print('Pulling Image')

        image = docker_client.images.pull(image_name)

        current_datetime = datetime.now()

        payload_logs = {
            "image_Tags":image.tags,
            "image_pull_at" : current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        }

        store_image_pull_logs(payload_logs)

        print(f'Successfully pulled image : {image.tags}')

    except ImageNotFound:
        print(f"Image '{image_name}' not found. Attempting to pull it...")
        try:
            docker_client.images.pull(image_name)
            print(f"Successfully pulled image: {image_name}")
        except APIError as e:
            print(f"Error pulling image: {e}")
    except DockerException as e:
        print(f"Error interacting with Docker: {e}")
    except Exception as e:
        print(f'An unexpected error occurred: {e}')





  def list_images(self):
     images_list = []

     try:
         all_images = docker_client.images.list(all=True)
         for index , image in enumerate(all_images):
             custom_payload = {
                 "image_Id" : image.id,
                 "image_tags":image.tags,
                 "image_name":image.labels
             }

             images_list.append(custom_payload)
         print('Image Fetches from Docker Engine') if len(images_list) > 0 else print('Images are Empty in your Docker Engine')
         store_image_list(images_list)
         image_statement = f'There are {len(images_list)}  Images in your Docker Engine'
         translate(image_statement)
         return images_list

     except DockerException as e:
         print(f'Error listing Images : {e}')

     except Exception as e:
         print(f'An Error Occur : {e}')




  def delete_image(self,image_name):
      try:

          image = image_name.strip()

          get_image = docker_client.images.get(image)

          if not get_image:
              raise ImageNotFound('Image Does Not Exists')

          print(f'Deleting {get_image.id} with {get_image.tags}')

          current_date = datetime.now()


          payload = {
              "image_name":image_name,
              "image_id":get_image.id,
              "deleted_at": current_date.strftime("%Y-%m-%d %H:%M:%S")
          }
          store_deleted_image(payload)
          get_image.remove(force=True)

          print(f'{get_image.id} Has Been Deleted or Removed')

          return True
      except ImageNotFound as e:
          print(f'{e}')

      except DockerException as e:
          print(f'Docker Encountered an error {e}')

      except Exception as e:
          print(f'An Error Occur : {e}')
