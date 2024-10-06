import json
import os
from constant.FilePathConstant import container_json, container_pdf
from extraction.ExtractText import extract_text_from_pdf,text_to_speech
from pdfUtils.ContainerPdf import create_pdf_container_list

def store_containers_json(container_name):
    try:
        create_if_not_exists(container_json)
        valid_len = check_container_length(container_name)

        if not valid_len:
            raise Exception('Container are Empty In Docker Engine')

        data = get_json_data()
        data_container = data['Containers'] or data.get('Containers')
        print(data_container)
        data_container_len = len(data_container) > 0

        if not data_container_len:
            for index , containers in enumerate(container_name):
                data_container.append(containers)

        print(data_container)
        data['Containers'] = data_container
        save_data_to_json(data)
        create_pdf_container_list(container_name)
        print(f'Saved {len(container_name)} to Json')
        text_to_speech(container_name)

        return True
    except Exception as e:
        print(e)
        print(f'Error in storing Container json {e}')




def create_if_not_exists(json_path):
    json_struct = {"Containers":[]}
    if not os.path.exists(json_path):

        with open(json_path, 'w') as json_file:
            json.dump(json_struct,json_file,indent=4)

        print(f'Container JSON File Created')
        return

    print('File is already Created')
    return


def save_data_to_json(json_data):
    print(json_data)

    with open(container_json, 'w') as file:
        json.dump(json_data,file,indent=4)

    return True



def get_json_data():
    json_data = None

    with open(container_json, 'r') as json_content:
        json_data = json.load(json_content)

    return json_data

def check_container_length(containers):
    return len(containers) > 0