// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func recoverFromPreorder(_ traversal: String) -> TreeNode? {
        let chars = Array(traversal)
        var stack = [TreeNode]()
        var i = 0
        let n = chars.count
        while i < n {
            var depth = 0
            while i < n && chars[i] == "-" {
                depth += 1
                i += 1
            }
            var val = 0
            while i < n && chars[i].isNumber {
                val = val * 10 + chars[i].wholeNumberValue!
                i += 1
            }
            let node = TreeNode(val)
            while stack.count > depth { stack.removeLast() }
            if let parent = stack.last {
                if parent.left == nil { parent.left = node }
                else { parent.right = node }
            }
            stack.append(node)
        }
        return stack.first
    }
}
