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


class NetworkInterfaceDnsSettings(Model):
    """DNS settings of a network interface.

    :param dns_servers: List of DNS servers IP addresses. Use
     'AzureProvidedDNS' to switch to azure provided DNS resolution.
     'AzureProvidedDNS' value cannot be combined with other IPs, it must be the
     only value in dnsServers collection.
    :type dns_servers: list[str]
    :param applied_dns_servers: If the VM that uses this NIC is part of an
     Availability Set, then this list will have the union of all DNS servers
     from all NICs that are part of the Availability Set. This property is what
     is configured on each of those VMs.
    :type applied_dns_servers: list[str]
    :param internal_dns_name_label: Relative DNS name for this NIC used for
     internal communications between VMs in the same virtual network.
    :type internal_dns_name_label: str
    :param internal_fqdn: Fully qualified DNS name supporting internal
     communications between VMs in the same virtual network.
    :type internal_fqdn: str
    :param internal_domain_name_suffix: Even if internalDnsNameLabel is not
     specified, a DNS entry is created for the primary NIC of the VM. This DNS
     name can be constructed by concatenating the VM name with the value of
     internalDomainNameSuffix.
    :type internal_domain_name_suffix: str
    """

    _attribute_map = {
        'dns_servers': {'key': 'dnsServers', 'type': '[str]'},
        'applied_dns_servers': {'key': 'appliedDnsServers', 'type': '[str]'},
        'internal_dns_name_label': {'key': 'internalDnsNameLabel', 'type': 'str'},
        'internal_fqdn': {'key': 'internalFqdn', 'type': 'str'},
        'internal_domain_name_suffix': {'key': 'internalDomainNameSuffix', 'type': 'str'},
    }

    def __init__(self, dns_servers=None, applied_dns_servers=None, internal_dns_name_label=None, internal_fqdn=None, internal_domain_name_suffix=None):
        super(NetworkInterfaceDnsSettings, self).__init__()
        self.dns_servers = dns_servers
        self.applied_dns_servers = applied_dns_servers
        self.internal_dns_name_label = internal_dns_name_label
        self.internal_fqdn = internal_fqdn
        self.internal_domain_name_suffix = internal_domain_name_suffix
