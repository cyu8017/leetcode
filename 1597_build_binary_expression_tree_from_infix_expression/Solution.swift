// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

class Node {
    var val: String
    var left: Node?
    var right: Node?
    init(_ val: String = " ", _ left: Node? = nil, _ right: Node? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func expTree(_ s: String) -> Node? {
        var nodes = [Node]()
        var ops = [Character]()
        let priority: [Character: Int] = ["+": 1, "-": 1, "*": 2, "/": 2]
        func apply() {
            let op = ops.removeLast()
            let right = nodes.removeLast()
            let left = nodes.removeLast()
            nodes.append(Node(String(op), left, right))
        }
        for ch in s {
            if ch.isNumber {
                nodes.append(Node(String(ch)))
            } else if ch == "(" {
                ops.append(ch)
            } else if ch == ")" {
                while ops.last != "(" { apply() }
                ops.removeLast()
            } else {
                while let last = ops.last, last != "(", priority[last]! >= priority[ch]! {
                    apply()
                }
                ops.append(ch)
            }
        }
        while !ops.isEmpty { apply() }
        return nodes[0]
    }
}
