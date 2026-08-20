// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

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
    func delNodes(_ root: TreeNode?, _ to_delete: [Int]) -> [TreeNode?] {
        let delete = Set(to_delete)
        var forest: [TreeNode?] = []
        func dfs(_ node: TreeNode?, _ isRoot: Bool) -> TreeNode? {
            guard let node = node else { return nil }
            let removed = delete.contains(node.val)
            if isRoot && !removed { forest.append(node) }
            node.left = dfs(node.left, removed)
            node.right = dfs(node.right, removed)
            return removed ? nil : node
        }
        dfs(root, true)
        return forest
    }
}
