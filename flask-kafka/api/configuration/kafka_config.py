"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : kafka_config.py
Purpose         : This Python file is used to contain the necessary parameters for connecting to Kafka.
"""


class KafkaConfig:
    bootstrap_servers: str
    auto_offset_reset: str

    def __init__(self, bootstrap_servers, auto_offset_reset):
      self.bootstrap_servers = bootstrap_servers
      self.auto_offset_reset = auto_offset_reset

    def __repr__(self):
      return "<KafkaConfig(name={self.name!r})>".format(self=self)