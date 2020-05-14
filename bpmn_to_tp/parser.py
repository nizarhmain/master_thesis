import xml.etree.ElementTree as ET


# 1 get all participants
# 2 get all messages


tree = ET.parse('bike_rental.bpmn')
root = tree.getroot()

# clean the output from {http://www.omg.org/spec/BPMN/20100524/MODEL}message
# trim it all the way until the second '}'


def trimb(string):
    trimmed = string[string.find('}'):]
    # print(trimmed[1:])
    elem = trimmed[1:]

    return elem


messages = []
participants = []
messageFlows = []

for child in root:
    # print(child.tag)

    # clean the output from {http://www.omg.org/spec/BPMN/20100524/MODEL}message
    # trim it all the way until the second '}'

    # print(trimmed[1:])

    elem = trimb(child.tag)

    if elem == 'message':
        # print(child.attrib)
        messages.append(child.attrib)
        # print(messages)

    if elem == 'choreography':

        for subchild in child:
            # print(subchild.attrib)

            subchild_type = trimb(subchild.tag)

            if subchild_type == 'participant':
                participants.append(subchild.attrib)

            if subchild_type == 'messageFlow':
                messageFlows.append(subchild.attrib)


# print(participants)
# print(messages)

# print(messageFlows)


def findParticipant(arr, id):
    for x in arr:
        if x["id"] == id:
            return x


def findMsgRef(arr, id):
    for x in arr:
        if x["id"] == id:
            return x


for msgflow in messageFlows:

    sourceguy = findParticipant(participants, msgflow['sourceRef'])
    # could ofc be optimized but its not an issue right now
    targetguy = findParticipant(participants, msgflow['targetRef'])

    message = findMsgRef(messages, msgflow['messageRef'])

    print('%s ----> %s ----> %s.'%(sourceguy['name'],message['name'], targetguy['name']))


# messages.append(child.attrib)

