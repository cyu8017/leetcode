// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Solution {
    func postorder(_ root: Node?) -> [Int] {
        var result = [Int]()
        func dfs(_ node: Node?) {
            guard let node else { return }
            for child in node.children { dfs(child) }
            result.append(node.val)
        }
        dfs(root)
        return result
    }
}
