struct Solution;
fn main() {}

// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn insert_greatest_common_divisors(
        mut head: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut cur = head.as_mut();
        while let Some(node) = cur {
            if node.next.is_none() {
                break;
            }
            let next = node.next.take();
            let g = gcd(node.val, next.as_ref().unwrap().val);
            node.next = Some(Box::new(ListNode {
                val: g,
                next,
            }));
            cur = node.next.as_mut().unwrap().next.as_mut();
        }
        head
    }
}
