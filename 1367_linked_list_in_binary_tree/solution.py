class Solution:
    def isSubPath(self, head, root):
        def match(a,b):
            return not a or bool(b and a.val==b.val and (match(a.next,b.left) or match(a.next,b.right)))
        return bool(root and (match(head,root) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)))
