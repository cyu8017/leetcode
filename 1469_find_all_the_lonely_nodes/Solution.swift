// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

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
    func getLonelyNodes(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        func dfs(_ node: TreeNode?) {
            guard let node = node else { return }
            if (node.left == nil) != (node.right == nil) {
                ans.append((node.left ?? node.right)!.val)
            }
            dfs(node.left); dfs(node.right)
        }
        dfs(root)
        return ans
    }
}
