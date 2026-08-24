// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Solution {
    func preorder(_ root: Node?) -> [Int] {
        var result = [Int]()
        func dfs(_ node: Node?) {
            guard let node else { return }
            result.append(node.val)
            for child in node.children { dfs(child) }
        }
        dfs(root)
        return result
    }
}
