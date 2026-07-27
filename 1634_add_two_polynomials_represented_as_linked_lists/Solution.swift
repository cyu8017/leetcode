// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

public class PolyNode {
    public var coefficient: Int
    public var power: Int
    public var next: PolyNode?
    public init() { self.coefficient = 0; self.power = 0; self.next = nil; }
    public init(_ x: Int, _ y: Int) { self.coefficient = x; self.power = y; self.next = nil; }
    public init(_ x: Int, _ y: Int, _ next: PolyNode?) {
        self.coefficient = x
        self.power = y
        self.next = next
    }
}

class Solution {
    func addPoly(_ poly1: PolyNode?, _ poly2: PolyNode?) -> PolyNode? {
        let dummy = PolyNode()
        var cur = dummy
        var p1 = poly1, p2 = poly2
        while p1 != nil || p2 != nil {
            let c: Int
            let p: Int
            if p2 == nil || (p1 != nil && p1!.power > p2!.power) {
                c = p1!.coefficient
                p = p1!.power
                p1 = p1!.next
            } else if p1 == nil || p2!.power > p1!.power {
                c = p2!.coefficient
                p = p2!.power
                p2 = p2!.next
            } else {
                c = p1!.coefficient + p2!.coefficient
                p = p1!.power
                p1 = p1!.next
                p2 = p2!.next
            }
            if c != 0 {
                cur.next = PolyNode(c, p)
                cur = cur.next!
            }
        }
        return dummy.next
    }
}
