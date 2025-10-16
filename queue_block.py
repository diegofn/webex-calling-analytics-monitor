import wxcadm
import queue

# Define the list of "blocked" numbers
blocked_callers = ['+181815551234',
                   '+17655559876']
# Set up the connection to Webex, making sure to include get_xsi=True
access_token = "ODI0ZDI1ZjItMjg1My00ZGU4LTg4YTgtYjJlYWNlYmJkYTYwMWI0NDcwNTYtOWI3_P0A1_b65d66a2-cba5-4212-88ab-bdc03b1d93aa"
webex = wxcadm.Webex(access_token)
webex.org.get_xsi_endpoints()

# Start the connection to XSI Events, open a channel and subscribe to the Call Center Queue event package
events = wxcadm.XSIEvents(webex.org)
events_queue = queue.Queue()
channel = events.open_channel(events_queue)
channel.subscribe("Call Center Agent")

# Start a loop to watch incoming messages
while True:
    message = events_queue.get()
    print (message['xsi:Event']['xsi:eventData']['@xsi1:type'])
    event_type = message['xsi:Event']['xsi:eventData']['@xsi1:type']
    call_queue_id = message['xsi:Event']['xsi:targetId']
    if event_type == "xsi:ACDCallAddedEvent":
        caller_number = message['xsi:Event']['xsi:eventData']['xsi:queueEntry']['xsi:remoteParty']['xsi:address']
        call_id = message['xsi:Event']['xsi:eventData']['xsi:queueEntry']['xsi:callId']
        # The address comes in the Events as a tel: URI so let's clean it up to get jus the number
        caller_number = caller_number.split(":")[-1]
        if caller_number in blocked_callers:
            # This is a blocked user. In our example, we block them by transferring them to an unused extension
            xsi = wxcadm.XSICallQueue(call_queue_id, org=webex.org)
            call = xsi.attach_call(call_id)
            call.transfer("8889")



# message
#{'xsi:Event': {'@xmlns:xsi': 'http://schema.broadsoft.com/xsi', '@xmlns:xsi1': 'http://www.w3.org/2001/XMLSchema-instance', '@xsi1:type': 'xsi:SubscriptionEvent', 'xsi:eventID': '0793e813-814f-4e25-9893-0b12d5c038b8', 'xsi:sequenceNumber': '11', 'xsi:userId': 'ce408669-9ce6-4714-be2d-58e662a79741', 'xsi:externalApplicationId': 'd2ab1443-bc8d-40c3-8e8d-655b0ba7d409', 'xsi:subscriptionId': '962c3aa9-f1cf-449b-97d0-c7436d036959', 'xsi:channelId': '6e62216c-c152-4c0b-857a-8287470cdf59', 'xsi:targetId': 'f9iiqqdffz@98303641.us10.bcld.webex.com', 'xsi:eventData': {...}}}

# message['xsi:Event']
#{'@xmlns:xsi': 'http://schema.broadsoft.com/xsi', '@xmlns:xsi1': 'http://www.w3.org/2001/XMLSchema-instance', '@xsi1:type': 'xsi:SubscriptionEvent', 'xsi:eventID': '0793e813-814f-4e25-9893-0b12d5c038b8', 'xsi:sequenceNumber': '11', 'xsi:userId': 'ce408669-9ce6-4714-be2d-58e662a79741', 'xsi:externalApplicationId': 'd2ab1443-bc8d-40c3-8e8d-655b0ba7d409', 'xsi:subscriptionId': '962c3aa9-f1cf-449b-97d0-c7436d036959', 'xsi:channelId': '6e62216c-c152-4c0b-857a-8287470cdf59', 'xsi:targetId': 'f9iiqqdffz@98303641.us10.bcld.webex.com', 'xsi:eventData': {'@xsi1:type': 'xsi:AgentStateEvent', 'xsi:agentStateInfo': {...}}}

# message['xsi:Event']['xsi:eventData']
#{'@xsi1:type': 'xsi:AgentStateEvent', 'xsi:agentStateInfo': {'xsi:state': 'Wrap-Up', 'xsi:stateTimestamp': {...}, 'xsi:wrapUpCallId': 'callhalf-11296441472:0', 'xsi:signInTimestamp': '0', 'xsi:totalAvailableTime': '14793620', 'xsi:averageWrapUpTime': {...}, 'xsi:wrapUpCallCenterUserId': 'wek6m548be@98303641.us10.bcld.webex.com'}}

#message['xsi:Event']['xsi:eventData']['xsi:agentStateInfo']
#{'xsi:state': 'Wrap-Up', 'xsi:stateTimestamp': {'xsi:value': '1760133147023'}, 'xsi:wrapUpCallId': 'callhalf-11296441472:0', 'xsi:signInTimestamp': '0', 'xsi:totalAvailableTime': '14793620', 'xsi:averageWrapUpTime': {'xsi:value': '19545'}, 'xsi:wrapUpCallCenterUserId': 'wek6m548be@98303641.us10.bcld.webex.com'}
