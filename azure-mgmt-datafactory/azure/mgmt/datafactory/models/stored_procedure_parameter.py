# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StoredProcedureParameter(Model):
    """SQL stored procedure parameter.

    :param value: Stored procedure parameter value. Type: string (or
     Expression with resultType string).
    :type value: object
    :param type: Stored procedure parameter type. Possible values include:
     'String', 'Int', 'Decimal', 'Guid', 'Boolean', 'Date'
    :type type: str or
     ~azure.mgmt.datafactory.models.StoredProcedureParameterType
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, value, type=None):
        self.value = value
        self.type = type
