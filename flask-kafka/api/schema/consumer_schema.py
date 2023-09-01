from marshmallow import Schema, fields

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : consumer_schema.py
Purpose         : -
"""


class ConsumerSchema(Schema):
  group_id = fields.Str(required=True)
  topics = fields.List(
    fields.Str(),
    required=True
  )
  config = fields.Dict()
