# -*- coding: utf8 -*-fr

"""
Import all class needed
"""

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>']

from itopapi.model.prototype import ItopapiPrototype, ItopapiUnimplementedMethod
from itopapi.model.rack import ItopapiRack
from itopapi.model.server import ItopapiServer
from itopapi.model.osFamily import ItopapiOSFamily
from itopapi.model.osVersion import ItopapiOSVersion
from itopapi.model.osLicence import ItopapiOSLicence
from itopapi.model.vlan import ItopapiVLAN
from itopapi.model.subnet import ItopapiSubnet
from itopapi.model.physicalInterface import ItopapiPhysicalInterface
from itopapi.model.virtualMachine import ItopapiVirtualMachine
from itopapi.model.webServer import ItopapiWebServer
from itopapi.model.webApplication import ItopapiWebApplication
from itopapi.model.service import ItopapiService
from itopapi.model.organization import ItopapiOrganization
from itopapi.model.location import ItopapiLocation
from itopapi.model.enclosure import ItopapiEnclosure
from itopapi.model.brand import ItopapiBrand
from itopapi.model.model import ItopapiModel
from itopapi.model.applicationSolution import ItopapiApplicationSolution

# TODO partial list of missing classes, with no particular order: Peripheral, MobilePhone, Printer, PC, Phone, IPPhone,
# Tablet, TapeLibrary, SANSwitchNAS, PDU, PowerSource, DatabaseSchema, OtherSoftware
