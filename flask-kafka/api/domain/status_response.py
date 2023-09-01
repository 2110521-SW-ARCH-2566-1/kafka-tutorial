"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : status_response.py
Purpose         : -
"""


class StatusResponse(object):
  code: str
  desc: str

  def __init__(self, code, desc):
    self.code = code
    self.desc = desc