// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int = 0, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Solution {
    func findRoot(_ tree: [Node]) -> Node? {
        var value = 0
        var nodes = [Int: Node]()
        for node in tree {
            nodes[node.val] = node
            value ^= node.val
            for child in node.children {
                value ^= child.val
            }
        }
        return nodes[value]
    }
}
