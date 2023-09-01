from marshmallow import Schema, fields

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : producer_schema.py
Purpose         : -
"""


class ProducerSchema(Schema):
  topic = fields.Str(required=True)
  message = fields.Str(required=True)
  config = fields.Dict()
