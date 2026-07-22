// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

using System.Collections.Generic;

public class PolyNode {
    public int coefficient;
    public int power;
    public PolyNode next;
    public PolyNode(int x = 0, int y = 0, PolyNode next = null) {
        coefficient = x;
        power = y;
        this.next = next;
    }
}

public class Solution {
    public PolyNode AddPoly(PolyNode poly1, PolyNode poly2) {
        var dummy = new PolyNode();
        var cur = dummy;
        while (poly1 != null || poly2 != null) {
            int c, p;
            if (poly2 == null || (poly1 != null && poly1.power > poly2.power)) {
                c = poly1.coefficient; p = poly1.power; poly1 = poly1.next;
            } else if (poly1 == null || poly2.power > poly1.power) {
                c = poly2.coefficient; p = poly2.power; poly2 = poly2.next;
            } else {
                c = poly1.coefficient + poly2.coefficient; p = poly1.power;
                poly1 = poly1.next; poly2 = poly2.next;
            }
            if (c != 0) { cur.next = new PolyNode(c, p); cur = cur.next; }
        }
        return dummy.next;
    }

    // Harness may pass list form; keep overload for compile/demo.
    public int[][] AddPoly(int[][] poly1, int[][] poly2) {
        PolyNode Build(int[][] items) {
            var dummy = new PolyNode();
            var cur = dummy;
            foreach (var item in items) { cur.next = new PolyNode(item[0], item[1]); cur = cur.next; }
            return dummy.next;
        }
        var head = AddPoly(Build(poly1), Build(poly2));
        var outList = new List<int[]>();
        for (var cur = head; cur != null; cur = cur.next) outList.Add(new[] { cur.coefficient, cur.power });
        return outList.ToArray();
    }
}
