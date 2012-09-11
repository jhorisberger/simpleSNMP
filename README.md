simpleSNMP
==========

A  simple Wrapper for the pysnmp Library

##Intro
The pysnmp-library is in my opinion one of the better librarys because it is pure python implemented. 
What realy bugs me though is that it is verry big to use in your code. The demo for a simple get request
is 89 lines of code, which I think is to much to have in my code. So I wrote a simple wrapper that converts
a SNMP-Get request into a one-liner. At the moment all other commands are not suported but this may change 
in the future.

##Description
### SNMP.request(OID, IP)
Returns a sting containing the data from the reqested OID and IP. The request is made using SNMP v1 and the user 'public'  
Example:  
`SNMP.request((1,3,6,1,2,1,2,2,1,16,2), '10.0.0.1')`