// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int = 0, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Solution {
    func diameter(_ root: Node?) -> Int {
        var answer = 0
        func depth(_ node: Node) -> Int {
            var longest = 0, second = 0
            for child in node.children {
                let value = depth(child) + 1
                if value > longest {
                    second = longest
                    longest = value
                } else if value > second {
                    second = value
                }
            }
            answer = max(answer, longest + second)
            return longest
        }
        if let root = root { _ = depth(root) }
        return answer
    }
}
