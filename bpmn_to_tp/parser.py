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

# trim until lower dash is found


def triml(string):
    trimmed = string[:string.find('_')]
    # print(trimmed[1:])
    elem = trimmed[0:]
    return elem


messages = []
participants = []
messageFlows = []
choreographyTasks = []
sequenceFlows = []
exclusiveGateways = []
parallelGateways = []
eventBasedGateways = []

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

            if subchild_type == 'choreographyTask':
                choreographyTasks.append(subchild)

            if subchild_type == 'sequenceFlow':
                # print(subchild.attrib)
                sequenceFlows.append(subchild)

            if subchild_type == 'exclusiveGateway':
                # print(subchild.attrib)
                exclusiveGateways.append(subchild)

            if subchild_type == 'parallelGateway':
                print(subchild.attrib)
                parallelGateways.append(subchild)

            if subchild_type == 'eventBasedGateway':
                print(subchild.attrib)
                eventBasedGateways.append(subchild)



def findOutgoings(id):
    # figure out the type

    elementType = triml(id)
    print(elementType)

    if elementType == 'SequenceFlow':
        for seq in sequenceFlows:
            if seq.attrib['id'] == id:
                print(seq.attrib)
                findOutgoings(seq.attrib['sourceRef'])
    
    if elementType == 'ExclusiveGateway':
        for x in exclusiveGateways:
            if x.attrib['id'] == id:
                for y in x:
                    if trimb(y.tag) == 'incoming':
                        print(y.text)
                        findOutgoings(y.text)

    if elementType == 'ChoreographyTask':
        for x in choreographyTasks:
            if x.attrib['id'] == id:
                print(x.attrib['name'])

    
    if elementType == 'EventBasedGateway':
        for x in eventBasedGateways:
            if x.attrib['id'] == id:
                for y in x:
                    if trimb(y.tag) == 'incoming':
                        print(y.text)
                        findOutgoings(y.text)

    if elementType == 'ParallelGateway':
        for x in parallelGateways:
            if x.attrib['id'] == id:
                for y in x:
                    if trimb(y.tag) == 'incoming':
                        print(y.text)
                        findOutgoings(y.text)




def preconditions_choreotask(id):

    for task in choreographyTasks:
        if task.attrib['id'] == id:
            for child in task:

                if trimb(child.tag) == 'incoming':
                    print(child.text)
                    # this is the id of the sequence flow
                    findOutgoings(child.text)
                    # find all the outgoing ones that are equal to this one

                if trimb(child.tag) == 'outgoing':
                    print('nevermind this')

            # figure out the incoming and the outcoming of these task
            # since this can only come from one way


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

    print('%s ----> %s ----> %s.' %
          (sourceguy['name'], message['name'], targetguy['name']))


# messages.append(child.attrib)


# preconditions_choreotask('ChoreographyTask_1ivug1p')

# preconditions_choreotask('ChoreographyTask_137ic1s')

# preconditions_choreotask('ChoreographyTask_1j5c18h')

# damage refund
# preconditions_choreotask('ChoreographyTask_00tsj0o')

# give feedback
# preconditions_choreotask('ChoreographyTask_1buzavy')

# give credits
# preconditions_choreotask('ChoreographyTask_0tydxhk')

# initial requ
# preconditions_choreotask('ChoreographyTask_1tcylad')


# pay bike
preconditions_choreotask('ChoreographyTask_0j5nws5')