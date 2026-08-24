// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

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
    func findDuplicateSubtrees(_ root: TreeNode?) -> [TreeNode?] {
        var counts = [String: Int]()
        var result = [TreeNode?]()
        func serialize(_ node: TreeNode?) -> String {
            guard let node else { return "#" }
            let key = "\(node.val),\(serialize(node.left)),\(serialize(node.right))"
            counts[key, default: 0] += 1
            if counts[key] == 2 { result.append(node) }
            return key
        }
        _ = serialize(root)
        return result
    }
}
