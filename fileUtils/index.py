import os
from constant.FilePathConstant import container_pdf,container_json,image_delete_json,image_pull_json,image_list_json

def clear_environment():

    files_to_delete = [
        container_json,
        image_delete_json,
        image_pull_json,
        image_list_json,
    ]


    files_deleted = False


    for file in files_to_delete:
        if os.path.exists(file):
            os.unlink(file)
            files_deleted = True

    if files_deleted:
        print('Cleaned Environment Created')
    else:
        print('No need To Clean')