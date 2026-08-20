// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

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
    func deepestLeavesSum(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var level = [root], answer = 0
        while !level.isEmpty {
            answer = level.reduce(0) { $0 + $1.val }
            var next: [TreeNode] = []
            for node in level {
                if let l = node.left { next.append(l) }
                if let r = node.right { next.append(r) }
            }
            level = next
        }
        return answer
    }
}
