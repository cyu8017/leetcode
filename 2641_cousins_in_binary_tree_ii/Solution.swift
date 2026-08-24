// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func replaceValueInTree(_ root: TreeNode?) -> TreeNode? {
        guard let root = root else { return nil }
        root.val = 0
        var q: [TreeNode] = [root]
        while !q.isEmpty {
            let sz = q.count
            var levelSum = 0
            var level: [TreeNode] = []
            for _ in 0..<sz {
                let node = q.removeFirst()
                level.append(node)
                if let l = node.left { levelSum += l.val }
                if let r = node.right { levelSum += r.val }
            }
            for node in level {
                var cousin = levelSum
                if let l = node.left { cousin -= l.val }
                if let r = node.right { cousin -= r.val }
                if let l = node.left {
                    l.val = cousin
                    q.append(l)
                }
                if let r = node.right {
                    r.val = cousin
                    q.append(r)
                }
            }
        }
        return root
    }
}
