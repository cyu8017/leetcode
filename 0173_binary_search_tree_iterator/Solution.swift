// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

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

class BSTIterator {
    private var stack = [TreeNode]()

    init(_ root: TreeNode?) {
        pushLeft(root)
    }

    func next() -> Int {
        let node = stack.removeLast()
        pushLeft(node.right)
        return node.val
    }

    func hasNext() -> Bool {
        !stack.isEmpty
    }

    private func pushLeft(_ node: TreeNode?) {
        var current = node
        while let currentNode = current {
            stack.append(currentNode)
            current = currentNode.left
        }
    }
}