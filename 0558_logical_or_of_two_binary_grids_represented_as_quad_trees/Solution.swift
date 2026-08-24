// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

class Node {
    var val: Bool
    var isLeaf: Bool
    var topLeft: Node?
    var topRight: Node?
    var bottomLeft: Node?
    var bottomRight: Node?

    init(_ val: Bool, _ isLeaf: Bool) {
        self.val = val
        self.isLeaf = isLeaf
    }

    init(_ val: Bool, _ isLeaf: Bool, _ topLeft: Node?, _ topRight: Node?, _ bottomLeft: Node?, _ bottomRight: Node?) {
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    }
}

class Solution {
    func intersect(_ quadTree1: Node?, _ quadTree2: Node?) -> Node? {
        guard let q1 = quadTree1, let q2 = quadTree2 else { return quadTree1 ?? quadTree2 }
        if q1.isLeaf { return q1.val ? q1 : q2 }
        if q2.isLeaf { return q2.val ? q2 : q1 }
        let topLeft = intersect(q1.topLeft, q2.topLeft)
        let topRight = intersect(q1.topRight, q2.topRight)
        let bottomLeft = intersect(q1.bottomLeft, q2.bottomLeft)
        let bottomRight = intersect(q1.bottomRight, q2.bottomRight)
        if let tl = topLeft, let tr = topRight, let bl = bottomLeft, let br = bottomRight,
           tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf,
           tl.val == tr.val, tr.val == bl.val, bl.val == br.val {
            return Node(tl.val, true)
        }
        return Node(false, false, topLeft, topRight, bottomLeft, bottomRight)
    }
}
