// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init(_ val: Int = 0, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func encodeNaryTree(_ root: Node?) -> TreeNode? {
        guard let root else {
            return nil
        }

        let binary = TreeNode(root.val)
        if root.children.isEmpty {
            return binary
        }

        binary.left = encodeNaryTree(root.children[0])
        var sibling = binary.left
        for index in 1..<root.children.count {
            sibling?.right = encodeNaryTree(root.children[index])
            sibling = sibling?.right
        }
        return binary
    }

    func decodeBinaryTree(_ root: TreeNode?) -> Node? {
        guard let root else {
            return nil
        }

        let node = Node(root.val, [])
        var current = root.left
        while let currentNode = current {
            node.children.append(decodeBinaryTree(currentNode)!)
            current = currentNode.right
        }
        return node
    }
}
