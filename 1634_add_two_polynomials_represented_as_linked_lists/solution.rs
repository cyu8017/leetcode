// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct PolyNode {
    pub coefficient: i32,
    pub power: i32,
    pub next: Option<Box<PolyNode>>,
}

impl PolyNode {
    #[inline]
    pub fn new(coefficient: i32, power: i32) -> Self {
        PolyNode { coefficient, power, next: None }
    }
}

impl Solution {
    pub fn add_poly(
        mut poly1: Option<Box<PolyNode>>,
        mut poly2: Option<Box<PolyNode>>,
    ) -> Option<Box<PolyNode>> {
        let mut dummy = Box::new(PolyNode::new(0, 0));
        let mut cur = &mut dummy;
        while poly1.is_some() || poly2.is_some() {
            let (c, p) = match (poly1.as_ref(), poly2.as_ref()) {
                (Some(a), Some(b)) if a.power == b.power => {
                    let c = a.coefficient + b.coefficient;
                    let p = a.power;
                    poly1 = poly1.unwrap().next;
                    poly2 = poly2.unwrap().next;
                    (c, p)
                }
                (Some(a), Some(b)) if a.power > b.power => {
                    let c = a.coefficient;
                    let p = a.power;
                    poly1 = poly1.unwrap().next;
                    (c, p)
                }
                (Some(a), None) => {
                    let c = a.coefficient;
                    let p = a.power;
                    poly1 = poly1.unwrap().next;
                    (c, p)
                }
                (_, Some(b)) => {
                    let c = b.coefficient;
                    let p = b.power;
                    poly2 = poly2.unwrap().next;
                    (c, p)
                }
                _ => break,
            };
            if c != 0 {
                cur.next = Some(Box::new(PolyNode::new(c, p)));
                cur = cur.next.as_mut().unwrap();
            }
        }
        dummy.next
    }
}
