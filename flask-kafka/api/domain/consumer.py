from ast import Dict, List

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : consumer.py
Purpose         : -
"""

class Consumer(object):
    group_id: str
    topics: List
    config: Dict

    def __init__(
      self,
      group_id=None,
      topics=None,
      config=None
    ):
      super(Consumer, self).__init__()
      self.group_id = group_id
      self.topics = topics
      self.config = config
