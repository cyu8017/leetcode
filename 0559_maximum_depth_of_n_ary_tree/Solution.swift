// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Solution {
    func maxDepth(_ root: Node?) -> Int {
        guard let root else { return 0 }
        if root.children.isEmpty { return 1 }
        var best = 0
        for child in root.children {
            best = max(best, maxDepth(child))
        }
        return best + 1
    }
}
