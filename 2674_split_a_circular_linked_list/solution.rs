// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

impl Solution {
    pub fn split_circular_linked_list(
        list: Option<Box<ListNode>>,
    ) -> Vec<Option<Box<ListNode>>> {
        let mut vals = Vec::new();
        let mut cur = list;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = node.next;
        }
        if vals.is_empty() {
            return vec![None, None];
        }
        let mid = (vals.len() + 1) / 2;
        fn build(slice: &[i32]) -> Option<Box<ListNode>> {
            let mut head = None;
            for &v in slice.iter().rev() {
                head = Some(Box::new(ListNode { val: v, next: head }));
            }
            head
        }
        vec![build(&vals[..mid]), build(&vals[mid..])]
    }
}
