// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

type PolyNode struct {
	Coefficient int
	Power       int
	Next        *PolyNode
}

func addPoly(poly1 *PolyNode, poly2 *PolyNode) *PolyNode {
	dummy := &PolyNode{}
	cur := dummy
	for poly1 != nil || poly2 != nil {
		var c, p int
		if poly2 == nil || (poly1 != nil && poly1.Power > poly2.Power) {
			c, p = poly1.Coefficient, poly1.Power
			poly1 = poly1.Next
		} else if poly1 == nil || poly2.Power > poly1.Power {
			c, p = poly2.Coefficient, poly2.Power
			poly2 = poly2.Next
		} else {
			c, p = poly1.Coefficient+poly2.Coefficient, poly1.Power
			poly1 = poly1.Next
			poly2 = poly2.Next
		}
		if c != 0 {
			cur.Next = &PolyNode{Coefficient: c, Power: p}
			cur = cur.Next
		}
	}
	return dummy.Next
}
