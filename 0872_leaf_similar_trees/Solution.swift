// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

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
    func leafSimilar(_ root1: TreeNode?, _ root2: TreeNode?) -> Bool {
        return leaves(root1) == leaves(root2)
    }

    private func leaves(_ node: TreeNode?) -> [Int] {
        var result = [Int]()
        func dfs(_ cur: TreeNode?) {
            guard let cur = cur else { return }
            if cur.left == nil && cur.right == nil {
                result.append(cur.val)
                return
            }
            dfs(cur.left)
            dfs(cur.right)
        }
        dfs(node)
        return result
    }
}
