// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

class Node {
    var val: Int
    var left: Node?
    var right: Node?
    var random: Node?
    init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
        self.random = nil
    }
}

class Solution {
    private var copies = [ObjectIdentifier: Node]()

    func copyRandomBinaryTree(_ root: Node?) -> Node? {
        guard let root = root else { return nil }
        let id = ObjectIdentifier(root)
        if let c = copies[id] { return c }
        let copy = Node(root.val)
        copies[id] = copy
        copy.left = copyRandomBinaryTree(root.left)
        copy.right = copyRandomBinaryTree(root.right)
        copy.random = copyRandomBinaryTree(root.random)
        return copy
    }
}
