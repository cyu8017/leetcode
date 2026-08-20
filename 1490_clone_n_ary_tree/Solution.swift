// LeetCode 1490 - Clone N-ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int) {
        self.val = val
        self.children = []
    }
}

class Solution {
    func cloneTree(_ root: Node?) -> Node? {
        guard let root = root else { return nil }
        let copy = Node(root.val)
        copy.children = root.children.compactMap { cloneTree($0) }
        return copy
    }
}
