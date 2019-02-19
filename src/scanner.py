import nmap                             #importing the python-nmap
nscanner = nmap.PortScanner()           #initiate the nscanner
version=nscanner.nmap_version()         #version on nmap on your system, if u don't have nmap installed on your system you 'll get error
print(version)                          #print the nmap version installed on your system

'''
nscanner.scan('127.0.0.10','1-1024','-sV')          #scan a range of port on a IP
print(nscanner.scaninfo())                          
print(nscanner.csv())
'''


nscanner.scan('185.143.232.21','22-445', '-sV')

#print(nscanner.all_hosts())


print(nscanner.scanstats())
print(nscanner['185.143.232.21'].state())           #checking the host state
print(nscanner['185.143.232.21'].all_protocols())   #checking protocols that active in the mechine
print(nscanner['185.143.232.21']['tcp'].keys())     #checking port state on a specific protocol (give a list of ports)
print(nscanner['185.143.232.21'].has_tcp(80))       #checking a specific port state (true or false)



