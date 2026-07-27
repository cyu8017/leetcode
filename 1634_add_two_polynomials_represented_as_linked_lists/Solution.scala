// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

class PolyNode(_coefficient: Int = 0, _power: Int = 0, _next: PolyNode = null) {
  var coefficient: Int = _coefficient
  var power: Int = _power
  var next: PolyNode = _next
}

object Solution {
  def addPoly(poly1: PolyNode, poly2: PolyNode): PolyNode = {
    var p1 = poly1
    var p2 = poly2
    val dummy = new PolyNode()
    var cur = dummy
    while (p1 != null || p2 != null) {
      var c = 0
      var p = 0
      if (p2 == null || (p1 != null && p1.power > p2.power)) {
        c = p1.coefficient; p = p1.power; p1 = p1.next
      } else if (p1 == null || p2.power > p1.power) {
        c = p2.coefficient; p = p2.power; p2 = p2.next
      } else {
        c = p1.coefficient + p2.coefficient; p = p1.power
        p1 = p1.next; p2 = p2.next
      }
      if (c != 0) {
        cur.next = new PolyNode(c, p)
        cur = cur.next
      }
    }
    dummy.next
  }
}
