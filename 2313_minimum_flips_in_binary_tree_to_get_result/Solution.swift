// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

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
    func minimumFlips(_ root: TreeNode?, _ result: Bool) -> Int {
        func dfs(_ node: TreeNode?) -> (Int, Int) {
            guard let node = node else { return (0, 0) }
            if node.left == nil && node.right == nil {
                return node.val == 0 ? (0, 1) : (1, 0)
            }
            if node.val == 5 {
                let x = dfs(node.left)
                return (x.1, x.0)
            }
            let L = dfs(node.left)
            let R = dfs(node.right)
            let lf = L.0, lt = L.1, rf = R.0, rt = R.1
            if node.val == 2 {
                return (lf + rf, min(lt + rt, min(lt + rf, lf + rt)))
            }
            if node.val == 3 {
                return (min(lf + rf, min(lf + rt, lt + rf)), lt + rt)
            }
            if node.val == 4 {
                return (min(lf + rf, lt + rt), min(lf + rt, lt + rf))
            }
            return (0, 0)
        }
        let res = dfs(root)
        return result ? res.1 : res.0
    }
}
