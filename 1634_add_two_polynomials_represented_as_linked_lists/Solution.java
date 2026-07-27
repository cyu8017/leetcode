// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

import java.util.*;

class PolyNode {
    int coefficient;
    int power;
    PolyNode next;
    PolyNode() {}
    PolyNode(int x, int y) { coefficient = x; power = y; }
    PolyNode(int x, int y, PolyNode next) { coefficient = x; power = y; this.next = next; }
}

class Solution {
    public PolyNode addPoly(PolyNode poly1, PolyNode poly2) {
        PolyNode dummy = new PolyNode();
        PolyNode cur = dummy;
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
            if (c != 0) {
                cur.next = new PolyNode(c, p);
                cur = cur.next;
            }
        }
        return dummy.next;
    }

    public int[][] addPoly(int[][] poly1, int[][] poly2) {
        PolyNode head = addPoly(build(poly1), build(poly2));
        List<int[]> out = new ArrayList<>();
        for (PolyNode cur = head; cur != null; cur = cur.next) {
            out.add(new int[] {cur.coefficient, cur.power});
        }
        return out.toArray(new int[0][]);
    }

    private PolyNode build(int[][] items) {
        PolyNode dummy = new PolyNode();
        PolyNode cur = dummy;
        for (int[] item : items) {
            cur.next = new PolyNode(item[0], item[1]);
            cur = cur.next;
        }
        return dummy.next;
    }
}
