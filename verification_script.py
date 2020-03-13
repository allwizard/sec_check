import os, time

#Set environment variables
OSSEC_PATH = ['/var/ossec/bin/ossec-execd','/var/ossec/bin/ossec-agentd','/var/ossec/bin/ossec-syscheckd','/var/ossec/bin/ossec-logcollector','/var/ossec/bin/wazuh-modulesd']
TANIUM_PATH = '/opt/Tanium/TaniumClient'
AGENT_PATH = ['C:/Users/g803249/Documents/sec_agent/working/sec_agent.txt','C:/Users/g803249/Documents/sec_agent/working/sec_agent2.txt']
RESULT = 'C:/Users/g803249/Documents/sec_agent/working/sec_agent_install_verification.txt'
METRICS_LOGS = ['C:/Users/g803249/Documents/sec_agent/working/']

#Installation Check Function
def install_check(path):
    if os.path.isfile(path):
        install_status = path + ' Exists in host'
        f = open(RESULT, 'w')
        f.write("1")
        f.close()
        modTimesinceEpoc = os.path.getmtime(path)
        modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
    
        print(install_status)
        print("Last Modified Time : ", modificationTime )

    else:    
        install_status = path + ' Does NOT exist in host'
        f = open(RESULT, 'w')
        f.write("0")
        f.close()
    
        print(install_status)


#OSSEC Check
for path in AGENT_PATH:
    install_check(path)

#Tanium Check








