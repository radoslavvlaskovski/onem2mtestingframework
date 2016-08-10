"""

Module that create a list of all OneM2M Resource types
and their attributes
 
"""

from Mappings import Resource as r

csebase_attributes = ["acpi", "poa", "nl", "cst", "csi", "srt", "ncp"]
CSEBase = r.Resource(csebase_attributes, "m2m:cb")

ae_attributes = ['aa','at','et','api','aei','apn','poa','or','nl','csz']
AE = r.Resource(ae_attributes,"m2m:ae")

acp_attributes = ['aa','at','et','pv','pvs']
AccessControlPolicy = r.Resource(acp_attributes,"m2m:acp")

['','','','','']

container_attributes = ['acpi','aa','at','et','or','cr','mni','mbs','mia','cni','cbs','li','st']
Container = r.Resource(container_attributes,"m2m:cnt")

contentInstance_attributes = ['cnf','cs','aa','at','cr','or',"con"]
ContentInstance = r.Resource(contentInstance_attributes,"m2m:cin")

delivery_attributes = ['acpi','et','st','sr','tg','ls','dmd','arq','eca']
Delivery = r.Resource(delivery_attributes,"m2m:dlv")

execInstance_attributes = ['exs','exr','exd','ext','exm','exf','exy','exn','exra','acpi','et']
ExecInstance = r.Resource(execInstance_attributes,"m2m:exin")

eventConfig_attributes = ['evi','evt','evs','eve','opt','ds','acpi','et']
EventConfig = r.Resource(eventConfig_attributes,"m2m:evcg")

group_attributes = ['mt','cnm','mnm','mid','macp','mtv','csy','gn','acpi','aa','at','cr']
Group = r.Resource(group_attributes,"m2m:grp")

locationPolicy_attributes = ['los','lou','lot','lor','loi','lon','lost','acpi','aa','at','et']
LocationPolicy = r.Resource(locationPolicy_attributes,"m2m:lcp")

node_attributes = ['ni','hcl','acpi','aa','at']
Node = r.Resource(node_attributes,"m2m:nod")

remoteCSE_attributes = ['cb','mei','tri','rr','cst','csi','acpi','aa','at','et','poa','nl']
RemoteCSE = r.Resource(remoteCSE_attributes,"m2m:csr")

request_attributes = ['og','mi','rs','ol','op','rid','et','acpi']
Request = r.Resource(request_attributes,"m2m:req")

schedule_attributes = ['se','et','at','aa','acpi']
Schedule = r.Resource(schedule_attributes,"m2m:sch")

serviceSubscribedNode_attributes = ['di','rlk','et','acpi']
serviceSubscribedNode = r.Resource(serviceSubscribedNode_attributes,"m2m:svsn")

statsCollect_attributes = ['sci','cei','cdi','srs','sm','cp','et','acpi']
statsCollect = r.Resource(statsCollect_attributes,"m2m:stcl")

subscription_attributes = ['enc','exc','nu','gpi','nfu','bn','rl','psn','pn','nsp','ln','nct','nec','su','et','acpi']
subscription = r.Resource(subscription_attributes,"m2m:sub")

firmware_attributes = ['vr','url','ud','uds','fwnnam','et','acpi']
firmware = r.Resource(firmware_attributes,"m2m:fwr")

software_attributes = ['vr','url','in','un','ins','act','dea','acts','swn','et','acpi']
software = r.Resource(software_attributes,"m2m:swr")

memory_attributes = ['mma','mmt','et','acpi']
memory = r.Resource(memory_attributes,"m2m:mem")

areaNwkInfo_attributes = ['acts','ant','ldv','et','acpi']
areaNwkInfo = r.Resource(areaNwkInfo_attributes,"m2m:ani")

areaNwkDeviceInfo_attributes = ['ss','dvd','dvt','awi','sli','sld','lnh','et','acpi']
areaNwkDeviceInfo = r.Resource(areaNwkDeviceInfo_attributes,"m2m:andi")

battery_attributes = ['btl','bts','et','acpi']
battery = r.Resource(battery_attributes,"m2m:")

deviceInfo_attributes = ['dlb','man','mod','dty','fwv','swv','hwv','et','acpi']
deviceInfo = r.Resource(deviceInfo_attributes,"m2m:bat")

deviceCapability_attributes = ['can','att','cas','ena','dis','cus','et','acpi']
deviceCapability = r.Resource(deviceCapability_attributes,"m2m:dvc")

reboot_attributes = ['rbo','far','et','acpi']
reboot = r.Resource(reboot_attributes,"m2m:rbo")

eventLog_attributes = ['lgt','lgd','lgst','lga','lgo','et','acpi']
eventLog = r.Resource(eventLog_attributes,"m2m:evl")

cmdhPolicy_attributes = ['cpn','cmlk','et','acpi']
cmdhPolicy = r.Resource(cmdhPolicy_attributes,"m2m:cmp")

activeCmdhPolicy_attributes = ['acmlk','cmlk','et','acpi']
activeCmdhPolicy = r.Resource(activeCmdhPolicy_attributes,"m2m:acmp")

cmdhDefEcValue_attributes = ['od','ror','rct','rctn','rch','dev','et','acpi']
cmdhDefaults = r.Resource(cmdhDefEcValue_attributes,"m2m:acmp")

cmdhEcDefParamValues_attributes = ['aec','dget','dset','doet','drp','dda','et','acpi']
cmdhDefEcValue = r.Resource(cmdhEcDefParamValues_attributes,"m2m:cmdv")

cmdhLimits_attributes = ['od','ror','rct','rctn','rch','et','acpi']
cmdhLimits = r.Resource(cmdhLimits_attributes,"m2m:cml")

cmdhNwAccessRule_attributes = ['mrv','bop','ohc','et','acpi']
cmdhNetworkAccessRules = r.Resource(cmdhNwAccessRule_attributes,"m2m:cmwr")

cmdhBuffer_attributes = ['mbfs','sgp','et','acpi']
cmdhBuffer = r.Resource(cmdhBuffer_attributes,"m2m:cmbf")

serviceSubscribedAppRule_attributes = ['aae','aai','apci','et','acpi']
serviceSubscribedAppRule = r.Resource(serviceSubscribedAppRule_attributes,"m2m:asar")


resources_list = list()

resources_list.append(CSEBase)
resources_list.append(AE)
resources_list.append(ContentInstance)
resources_list.append(Delivery)
resources_list.append(ExecInstance)
resources_list.append(EventConfig)
resources_list.append(Group)
resources_list.append(LocationPolicy)
resources_list.append(Node)
resources_list.append(RemoteCSE)
resources_list.append(Request)
resources_list.append(Schedule)
resources_list.append(serviceSubscribedNode)
resources_list.append(statsCollect)
resources_list.append(subscription)
resources_list.append(firmware)
resources_list.append(software)
resources_list.append(memory)
resources_list.append(areaNwkInfo)
resources_list.append(areaNwkDeviceInfo)
resources_list.append(battery)
resources_list.append(deviceInfo)
resources_list.append(deviceCapability)
resources_list.append(reboot)
resources_list.append(eventLog)
resources_list.append(cmdhPolicy)
resources_list.append(activeCmdhPolicy)
resources_list.append(cmdhDefEcValue)
resources_list.append(cmdhDefaults)
resources_list.append(cmdhLimits)
resources_list.append(cmdhNetworkAccessRules)
resources_list.append(cmdhBuffer)
resources_list.append(serviceSubscribedAppRule)


def find_resource(resource_type):
    for resource in resources_list:
        if resource_type == resource.get_short_name():
            return resource
