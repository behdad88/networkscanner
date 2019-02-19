import nmap
testscanner = nmap.PortScanner()
name=testscanner.nmap_version()
print(name)