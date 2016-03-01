# -*- coding: utf8 -*-fr

"""
ItopapiSubnet is a abstraction of Subnet representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiSubnet(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Subnet',
        # Define which fields to save when creating or updating from the python API
        'save': ['ip', 'ip_mask', 'subnet_name', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
        ],
        'list_types': {'vlans_list': 'VLAN'},
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiSubnet, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiSubnet, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiSubnet)

    """
    ItopapiPhysicalInterface is an object that represents a PhysicalInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiSubnet, self).__init__(data)
        # base IP address for the subnet
        self.ip = None
        # IP mask for the subnet
        self.ip_mask = None
        # Subnet name
        self.subnet_name = None
        # Subnet's organization id. Call find_organization to get the full information or just use
        # org_id_friendlyname and organization_name
        self.org_id = None
        # Subnet's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Subnet's organization name
        self.org_name = None
        # Subnet's description
        self.description = None
        # VLANs associated with this Subnet
        self.vlans_list = None


    def find_organization(self):
        """
        Retrieve the ItopapiOrganization related to this instance
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None