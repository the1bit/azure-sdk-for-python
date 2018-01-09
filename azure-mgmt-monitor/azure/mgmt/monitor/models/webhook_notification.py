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


class WebhookNotification(Model):
    """Webhook notification of an autoscale event.

    :param service_uri: the service address to receive the notification.
    :type service_uri: str
    :param properties: a property bag of settings. This value can be empty.
    :type properties: dict[str, str]
    """

    _attribute_map = {
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, service_uri=None, properties=None):
        super(WebhookNotification, self).__init__()
        self.service_uri = service_uri
        self.properties = properties
