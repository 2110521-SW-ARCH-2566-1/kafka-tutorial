from typing import Dict, List

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : consumer.py
Purpose         : -
"""

class Consumer(object):
    group_id: str
    topic: str
    config: Dict

    def __init__(
      self,
      group_id=None,
      topic=None,
      config=None
    ):
      super(Consumer, self).__init__()
      self.group_id = group_id
      self.topic = topic
      self.config = config
