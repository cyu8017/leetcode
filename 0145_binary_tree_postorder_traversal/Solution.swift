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
    func postorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()

        func traverse(_ node: TreeNode?) {
            guard let node else { return }
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)
        }

        traverse(root)
        return result
    }
}