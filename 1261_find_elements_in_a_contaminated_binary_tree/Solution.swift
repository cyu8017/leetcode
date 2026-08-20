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

// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class FindElements {
    private var values = Set<Int>()

    init(_ root: TreeNode?) {
        recover(root, 0)
    }

    private func recover(_ node: TreeNode?, _ value: Int) {
        guard let node = node else { return }
        node.val = value
        values.insert(value)
        recover(node.left, 2 * value + 1)
        recover(node.right, 2 * value + 2)
    }

    func find(_ target: Int) -> Bool {
        values.contains(target)
    }
}
