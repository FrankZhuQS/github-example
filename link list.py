
class node(object):
    # 链表的节点
    def __init__(self, data, p=None):
        self.data = data
        self.next = p
    # 重写打印
    def __repr__(self):
        return str(self.data)


class linklist(object):
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head == None

    def length(self):
        temp = self.head
        counter = 0
        while temp != None:
            counter += 1
            temp = temp.next
        return counter

    def clear(self):
        self.head = None

    def travel(self):
        temp = self.head
        if self.isempty():
            print("is empty")
        else:
            while temp != None:
                print(temp)
                temp = temp.next

    def append(self, data):
        n = node(data)
        if self.isempty():
            self.head = n
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n

    def add(self, data):
        n = node(data)
        n.next = self.head
        self.head = n

    def insert(self, num, data):
        # 下表 == num
        l = self.length()
        if num <= 0:
            self.add(data)
        elif num >= l:
            self.append(data)
        else:
            temp = node(data)
            counter = 0
            pre = self.head
            while counter < num - 1:
                counter += 1
                pre = pre.next
            temp.next = pre.next
            pre.next = temp

    def search(self, data):
        temp = self.head
        result = False
        while temp.next != None:
            if temp.data == data:
                result = True
                break
            temp = temp.next
        return result

    def remove(self, data):
        # 删除一个
        temp = self.head
        pre = None
        while temp != None:
            if temp.data == data:
                if not pre:
                    self.head = temp.next
                    break
                else:
                    pre.next = temp.next
                    break
            else:
                pre = temp
                temp = temp.next





'''
a = linklist()
a.append(15)
a.append(16)
a.add(14)
a.insert(-1, 13)
a.insert(15,17)
a.insert(1,13.5)
a.travel()
a.remove(16)
a.travel()
print(a.length())
print(a.search(15))
print(a.search(20))
'''
