# -*- coding:utf-8 -*-
import os
import glob

current_path = os.path.dirname(os.path.realpath(__file__))


def storage_path(file_path=""):
    return os.path.join(base_path("storage"), file_path)


def base_path(file_path=""):
    return os.path.join(current_path, file_path)


def get_faces():
    return glob.glob(storage_path("images\\faces\\*.jpg"))


def get_dlib_model(model_file_name):
    return os.path.join(storage_path("model"), model_file_name)


if __name__ == '__main__':
    print(base_path("asd"))
    print(storage_path("asd"))
