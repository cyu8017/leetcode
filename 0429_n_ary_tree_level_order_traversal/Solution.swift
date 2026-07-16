// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Solution {
    func levelOrder(_ root: Node?) -> [[Int]] {
        guard let root else {
            return []
        }

        var result: [[Int]] = []
        var queue: [Node] = [root]

        while !queue.isEmpty {
            var level: [Int] = []
            let size = queue.count
            for _ in 0..<size {
                let node = queue.removeFirst()
                level.append(node.val)
                queue.append(contentsOf: node.children)
            }
            result.append(level)
        }

        return result
    }
}
