from typing import Union, Type

from marshmallow import Schema, INCLUDE, ValidationError

from core import BadRequestException


def accepts_logic(payload: dict = {}, temp: dict = {}, schema: Schema = None, many=False):
    schema = _get_or_create_schema(schema, many=many)

    try:
        payload['temp'] = temp
        payload = schema.load(payload, unknown=INCLUDE)
        del payload['temp']
    except ValidationError as err:
        raise BadRequestException(message=err.messages)

    return payload


def _get_or_create_schema(
        schema: Union[Schema, Type[Schema]], many: bool = False
) -> Schema:
    if isinstance(schema, Schema):
        return schema
    return schema(many=many)
