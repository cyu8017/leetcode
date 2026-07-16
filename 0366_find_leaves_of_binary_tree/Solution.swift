// LeetCode 0366 - Find Leaves of Binary Tree
// https://leetcode.com/problems/find-leaves-of-binary-tree/

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
    func findLeaves(_ root: TreeNode?) -> [[Int]] {
        var layers: [[Int]] = []

        func dfs(_ node: TreeNode?) -> Int {
            guard let node = node else {
                return -1
            }

            let height = max(dfs(node.left), dfs(node.right)) + 1
            while layers.count <= height {
                layers.append([])
            }
            layers[height].append(node.val)
            return height
        }

        dfs(root)
        return layers
    }
}
