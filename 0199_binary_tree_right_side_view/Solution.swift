// LeetCode 0199 - Binary Tree Right Side View
class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?

    init(_ val: Int = 0, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func rightSideView(_ root: TreeNode?) -> [Int] {
        guard let root = root else { return [] }
        var result: [Int] = []
        var queue = [root]

        while !queue.isEmpty {
            let levelSize = queue.count
            for index in 0..<levelSize {
                let node = queue.removeFirst()
                if index == levelSize - 1 {
                    result.append(node.val)
                }
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
        }
        return result
    }
}