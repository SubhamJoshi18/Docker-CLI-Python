import os
import json
from constant.FilePathConstant import image_pull_json
from constant.FilePathConstant import image_list_json
from constant.FilePathConstant import image_delete_json

def store_deleted_image(data):
    create_if_not_exists_delete(image_delete_json)
    try:
        json_data = get_json_delete_image_data()

        if len(json_data['Deleted_Images']) == 0:
            json_data['Deleted_Images'].append(data)
            save_json_deleted_logs(json_data)
            return True
        elif len(json_data['Deleted_Images']) > 0:
            json_data['Deleted_Images'].append(data)
            save_json_deleted_logs(json_data)
            return True
        else:
            return


    except Exception as e:
        print(f'Error in handling delete images :{e}')



def store_image_list(data):
    create_if_not_exists_image_list(image_list_json)
    image_info = []

    try:

        for payload in data:
            if payload.get('image_Id') and payload.get('image_tags') and payload.get('image_name'):
                image_info.append(payload)

        json_data = get_json_image_data_list()


        if len(image_info) > 0:
            json_data['Images'].extend(image_info)
            save_json_image_logs(json_data)
            print(f'Saved {len(image_info)} Images in Json')
            return True
        else:
            print('No valid image data to store.')

    except Exception as e:
        print(f'Error in storing image list: {e}')




def store_image_pull_logs(payload):
    create_if_not_exists(image_pull_json)
    try:

        json_data = get_json_data()



        if len(json_data['Pull_Images']) == 0:
            json_data['Pull_Images'].append(payload)
            save_json_logs(json_data)
            return True
        elif len(json_data['Pull_Images']) > 0:
            json_data['Pull_Images'].append(payload)
            save_json_logs(json_data)
            return True
        else:
            return
    except Exception as e:
        print(f'Error in storing image in logs : {e}')



def save_json_image_logs(data):
    with open(image_list_json,'w') as file:
        json.dump(data,file,indent=4)
        print('Json Data Saved')
        return



def save_json_logs(data):
    with open(image_pull_json,'w') as file:
        json.dump(data,file,indent=4)
        print('Json Logs Saved')
        return

def save_json_deleted_logs(data):
    with open(image_delete_json,'w') as file:
        json.dump(data,file,indent=4)
        print('Logs Saved Successfully')
        return

def get_json_image_data_list():
    json_data = None
    with open(image_list_json,'r') as json_file:
        json_data = json.load(json_file)

    return json_data


def get_json_delete_image_data():
    json_data = None
    with open(image_delete_json,'r') as json_file:
        json_data = json.load(json_file)
    return json_data

def get_json_data():
    json_data = None
    with open(image_pull_json,'r') as json_file:
        json_data = json.load(json_file)

    return json_data


def create_if_not_exists(file_path):
    json_struct = {"Pull_Images":[]}
    if not os.path.exists(file_path):
        with open(file_path,'w') as file:
            json.dump(json_struct,file,indent=4)
            print('Json File Created')

        return
    print('File already Exists')
    return


def create_if_not_exists_delete(file_path):
    json_struct = {"Deleted_Images":[]}
    if not os.path.exists(file_path):
        with open(file_path,'w') as file:
            json.dump(json_struct,file,indent=4)
            print('Json File Created')
            return

    print('File Already Exists')
    return



def create_if_not_exists_image_list(file_path):
    json_struct = {"Images": []}

    # Check if the file exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump(json_struct, file, indent=4)
            print('Json File Created')
    else:
        print('File Already Exists')