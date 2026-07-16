class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?

    init(_ val: Int, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()

        func traverse(_ node: TreeNode?) {
            guard let node else { return }
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        }

        traverse(root)
        return result
    }
}