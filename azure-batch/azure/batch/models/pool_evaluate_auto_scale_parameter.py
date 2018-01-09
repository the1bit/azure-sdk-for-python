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


class PoolEvaluateAutoScaleParameter(Model):
    """Options for evaluating an automatic scaling formula on a pool.

    :param auto_scale_formula: The formula for the desired number of compute
     nodes in the pool. The formula is validated and its results calculated,
     but it is not applied to the pool. To apply the formula to the pool,
     'Enable automatic scaling on a pool'. For more information about
     specifying this formula, see Automatically scale compute nodes in an Azure
     Batch pool
     (https://azure.microsoft.com/en-us/documentation/articles/batch-automatic-scaling).
    :type auto_scale_formula: str
    """

    _validation = {
        'auto_scale_formula': {'required': True},
    }

    _attribute_map = {
        'auto_scale_formula': {'key': 'autoScaleFormula', 'type': 'str'},
    }

    def __init__(self, auto_scale_formula):
        super(PoolEvaluateAutoScaleParameter, self).__init__()
        self.auto_scale_formula = auto_scale_formula
