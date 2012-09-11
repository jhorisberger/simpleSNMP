#!/usr/bin/python


from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp
from pyasn1.codec.ber import encoder, decoder
from pysnmp.proto import api
from time import time


# Protocol version to use
pMod = api.protoModules[api.protoVersion1]
reqPDU =  pMod.GetRequestPDU()


def cbTimerFun(timeNow, startedAt=time()):
    if timeNow - startedAt > 5:
        print ("Request timed out")
    
def cbRecvFun(transportDispatcher, transportDomain, transportAddress,
              wholeMsg, reqPDU=reqPDU):
    while wholeMsg:
        rspMsg, wholeMsg = decoder.decode(wholeMsg, asn1Spec=pMod.Message())
        rspPDU = pMod.apiMessage.getPDU(rspMsg)
        # Match response to request
        if pMod.apiPDU.getRequestID(reqPDU)==pMod.apiPDU.getRequestID(rspPDU):
            # Check for SNMP errors reported
            errorStatus = pMod.apiPDU.getErrorStatus(rspPDU)
            if errorStatus:
                print (errorStatus.prettyPrint())

            else:
                for oid, val in pMod.apiPDU.getVarBinds(rspPDU):
                    global value
                    value = int(val.prettyPrint())
            transportDispatcher.jobFinished(1)
    return wholeMsg




class SNMP:
	
	def request(oid, ip, port=161):
	
		# Build PDU
		pMod.apiPDU.setDefaults(reqPDU)
		pMod.apiPDU.setVarBinds(
			reqPDU, ((oid, pMod.Null()),
					((oid), pMod.Null()))
			)
			
		# Build message
		reqMsg = pMod.Message()
		pMod.apiMessage.setDefaults(reqMsg)
		pMod.apiMessage.setCommunity(reqMsg, 'public')
		pMod.apiMessage.setPDU(reqMsg, reqPDU)
			
		# Send message
		transportDispatcher = AsynsockDispatcher()
		transportDispatcher.registerTransport(
			udp.domainName, udp.UdpSocketTransport().openClientMode()
			)
		transportDispatcher.registerRecvCbFun(cbRecvFun)
		transportDispatcher.registerTimerCbFun(cbTimerFun)
		transportDispatcher.sendMessage(
			encoder.encode(reqMsg), udp.domainName, (ip, port)
			)
		transportDispatcher.jobStarted(1)
		transportDispatcher.runDispatcher()
		transportDispatcher.closeDispatcher()
		
		return value