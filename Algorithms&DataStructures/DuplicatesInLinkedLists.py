class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
	while currentNode != None:
		nextNew = currentNode.next
		while nextNew != None and nextNew.value == currentNode.value:
			nextNew = nextNew.next
			
		currentNode.next = nextNew
		currentNode = nextNew
	return linkedList
			