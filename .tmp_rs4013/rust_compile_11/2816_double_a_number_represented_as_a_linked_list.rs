struct Solution;
fn main() {}

// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

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
    pub fn double_it(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        fn rev(mut node: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
            let mut prev = None;
            while let Some(mut cur) = node {
                node = cur.next.take();
                cur.next = prev;
                prev = Some(cur);
            }
            prev
        }
        let mut head = rev(head);
        let mut carry = 0;
        {
            let mut cur = &mut head;
            while let Some(node) = cur {
                let val = node.val * 2 + carry;
                node.val = val % 10;
                carry = val / 10;
                cur = &mut node.next;
            }
        }
        if carry > 0 {
            let mut cur = &mut head;
            while let Some(node) = cur {
                if node.next.is_none() {
                    node.next = Some(Box::new(ListNode::new(carry)));
                    break;
                }
                cur = &mut node.next;
            }
        }
        rev(head)
    }
}
