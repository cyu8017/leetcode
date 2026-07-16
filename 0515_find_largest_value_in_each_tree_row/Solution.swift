// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution {
    func largestValues(_ root: TreeNode?) -> [Int] {
        guard let root = root else {
            return []
        }

        var result = [Int]()
        var queue = [root]

        while !queue.isEmpty {
            var levelMax = Int.min
            let levelSize = queue.count
            for _ in 0..<levelSize {
                let node = queue.removeFirst()
                levelMax = max(levelMax, node.val)
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
            result.append(levelMax)
        }

        return result
    }
}

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
