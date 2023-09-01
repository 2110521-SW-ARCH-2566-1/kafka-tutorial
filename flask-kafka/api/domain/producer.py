from ast import Dict

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : producer.py
Purpose         : -
"""


class Producer(object):
    topic: str
    message: str
    config: Dict

    def __init__(
      self,
      topic=None,
      message=None,
      config=None
    ):
      super(Producer, self).__init__()
      self.topic = topic
      self.message = message
      self.config = config