import os
import json
import numpy as np

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, mode = "r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    else:
        return data[field]


def linear_search(sequential_data, number):
    search_res = {"positions": [], "count": 0}

    for i, value in enumerate(sequential_data):
        if value == number:
            search_res["positions"].append(i)
            search_res["count"] += 1

    return search_res


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")

    search_res = linear_search(sequential_data, number=0)

    print(search_res)




if __name__ == '__main__':
    main()