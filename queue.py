# codeing = UTF-8
class Queue():
    def __init__(qu, size):
        qu.queue = [];
        qu.size = size;
        qu.head = -1;
        qu.tail = -1;

    def Empty(qu):
        if qu.head == qu.tail:
            return True
        else:
            return False

    def Full(qu):
        if qu.tail - qu.head + 1 == qu.size:
            return True
        else:
            return False

    def enQueue(qu, content):
        if qu.Full():
            print "Queue is Full!"
        else:
            qu.queue.append(content)
            qu.tail = qu.tail + 1

    def outQueue(qu):
        if qu.Empty():
            print "Queue is Empty!"
        else:
            qu.head = qu.head + 1

