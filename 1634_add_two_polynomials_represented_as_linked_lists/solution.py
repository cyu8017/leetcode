class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient, self.power, self.next = x, y, next
class Solution:
    def addPoly(self, poly1, poly2):
        list_mode = isinstance(poly1, list) or isinstance(poly2, list)
        def build(items):
            dummy=cur=PolyNode()
            for c,p in items: cur.next=PolyNode(c,p); cur=cur.next
            return dummy.next
        if isinstance(poly1,list): poly1=build(poly1)
        if isinstance(poly2,list): poly2=build(poly2)
        dummy=cur=PolyNode()
        while poly1 or poly2:
            if not poly2 or poly1 and poly1.power>poly2.power: c,p=poly1.coefficient,poly1.power; poly1=poly1.next
            elif not poly1 or poly2.power>poly1.power: c,p=poly2.coefficient,poly2.power; poly2=poly2.next
            else: c,p=poly1.coefficient+poly2.coefficient,poly1.power; poly1=poly1.next; poly2=poly2.next
            if c: cur.next=PolyNode(c,p); cur=cur.next
        if not list_mode: return dummy.next
        out=[]; cur=dummy.next
        while cur: out.append([cur.coefficient,cur.power]); cur=cur.next
        return out
