// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

class Node {
    var val: String
    var left: Node?
    var right: Node?
    init(_ val: String = "", _ left: Node? = nil, _ right: Node? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func checkEquivalence(_ root1: Node?, _ root2: Node?) -> Bool {
        var a = [Character: Int]()
        var b = [Character: Int]()
        count(root1, &a)
        count(root2, &b)
        return a == b
    }

    private func count(_ node: Node?, _ out: inout [Character: Int]) {
        guard let node = node else { return }
        if node.val == "+" {
            count(node.left, &out)
            count(node.right, &out)
        } else if let ch = node.val.first {
            out[ch, default: 0] += 1
        }
    }
}
