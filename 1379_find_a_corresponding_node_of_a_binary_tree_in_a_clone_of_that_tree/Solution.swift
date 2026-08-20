// LeetCode 1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}

class Solution {
    func getTargetCopy(_ original: TreeNode?, _ cloned: TreeNode?, _ target: TreeNode?) -> TreeNode? {
        guard let target = target else { return nil }
        var stack = [(original, cloned)]
        while !stack.isEmpty {
            let (a, b) = stack.removeLast()
            guard let a = a, let b = b else { continue }
            if a === target { return b }
            if a.left != nil { stack.append((a.left, b.left)) }
            if a.right != nil { stack.append((a.right, b.right)) }
        }
        return nil
    }
}
