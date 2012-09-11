simpleSNMP Examples
================

**Note:** For these examples to work, you have to adress a device that is SNMP compadible  
  


 
Description 
------------

### demo.py

Reads a value forom a given OID and IP and returns the value   

Example to read the OID 1.3.6.1.2.1.2.2.1.10.2 (downstream packets) from the IP 10.0.0.1 (my local router)
`sudo python3 demo.py 10.0.0.1`  

**Note:** you can change the oid in the demo.py on line 9


