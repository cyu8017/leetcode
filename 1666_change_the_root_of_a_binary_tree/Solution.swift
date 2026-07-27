// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

class Node {
    var val: Int
    var left: Node?
    var right: Node?
    var parent: Node?
    init(_ val: Int = 0) {
        self.val = val
    }
}

class Solution {
    func flipBinaryTree(_ root: Node?, _ leaf: Node?) -> Node? {
        var node = leaf
        while node !== root {
            let parent = node!.parent!
            if parent.left === node {
                parent.left = nil
            } else {
                parent.right = nil
            }
            let originalLeft = node!.left
            node!.left = parent
            if originalLeft != nil {
                node!.right = originalLeft
            }
            node = parent
        }
        func fixParent(_ cur: Node?, _ parent: Node?) {
            guard let cur = cur else { return }
            cur.parent = parent
            fixParent(cur.left, cur)
            fixParent(cur.right, cur)
        }
        fixParent(leaf, nil)
        return leaf
    }
}
