"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : header.py
Purpose         : -
"""


class Header(object):
  request_id: str
  transaction_date: str

  def __init__(
    self,
    request_id=None,
    transaction_date=None
  ):
    super(Header, self).__init__()
    self.request_id = request_id
    self.transaction_date = transaction_date