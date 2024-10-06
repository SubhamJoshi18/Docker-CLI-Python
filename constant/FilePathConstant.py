import os

current_cwd = os.getcwd()


## container path
container_json =  os.path.join(current_cwd,'jsonLogs','Containers','Container.json')

container_pdf = os.path.join(current_cwd,'pdfs','Container','container.pdf')

container_audio = os.path.join(current_cwd,'audioFile','Container','container.mp3')


##image path


image_pull_json = os.path.join(current_cwd,'jsonLogs','Image','ImagePullLog.json')

image_list_json = os.path.join(current_cwd,'jsonLogs','Image','Image.json')

image_delete_json = os.path.join(current_cwd,'jsonLogs','Image','ImageDelete.json')