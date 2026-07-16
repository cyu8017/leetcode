class Solution:
    def getTargetCopy(self, original, cloned, target):
        wanted=target if isinstance(target,int) else target.val
        stack=[(original,cloned)]
        while stack:
            a,b=stack.pop()
            if a.val==wanted:return b.val if isinstance(target,int) else b
            if a.left:stack.append((a.left,b.left))
            if a.right:stack.append((a.right,b.right))
