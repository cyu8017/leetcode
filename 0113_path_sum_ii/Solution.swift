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
    func pathSum(_ root: TreeNode?, _ targetSum: Int) -> [[Int]] {
        var result = [[Int]]()
        func visit(_ node: TreeNode?, _ remaining: Int, _ path: [Int]) {
            guard let node = node else { return }
            let currentPath = path + [node.val]
            if node.left == nil && node.right == nil {
                if node.val == remaining { result.append(currentPath) }
                return
            }
            visit(node.left, remaining - node.val, currentPath)
            visit(node.right, remaining - node.val, currentPath)
        }
        visit(root, targetSum, [])
        return result
    }
}