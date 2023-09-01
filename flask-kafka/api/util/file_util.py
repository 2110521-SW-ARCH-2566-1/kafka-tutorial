import yaml

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : file_util.py
Purpose         : -
"""


def read_yaml_file(path):
  with open(path, "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    return cfg
