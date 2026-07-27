// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

class Node {
    var val: String
    var left: Node?
    var right: Node?

    init(_ val: String, _ left: Node? = nil, _ right: Node? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }

    func evaluate() -> Int {
        if !"+-*/".contains(val) { return Int(val)! }
        let a = left!.evaluate()
        let b = right!.evaluate()
        switch val {
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        default: return a / b
        }
    }
}

class TreeBuilder {
    func expTree(_ postfix: [String]) -> Node? {
        var stack = [Node]()
        for token in postfix {
            let node = Node(token)
            if "+-*/".contains(token) {
                node.right = stack.removeLast()
                node.left = stack.removeLast()
            }
            stack.append(node)
        }
        return stack.last
    }
}
