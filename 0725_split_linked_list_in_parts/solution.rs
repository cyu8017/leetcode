// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

#[derive(Debug, PartialEq, Eq)]
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
    pub fn split_list_to_parts(
        head: Option<Box<ListNode>>,
        k: i32,
    ) -> Vec<Option<Box<ListNode>>> {
        let mut values = Vec::new();
        let mut current = head;
        while let Some(node) = current {
            values.push(node.val);
            current = node.next;
        }
        let k = k as usize;
        let length = values.len();
        let part_size = length / k;
        let extra = length % k;
        let mut result = Vec::with_capacity(k);
        let mut idx = 0;
        for i in 0..k {
            let size = part_size + if i < extra { 1 } else { 0 };
            let mut dummy = ListNode::new(0);
            let mut tail = &mut dummy;
            for _ in 0..size {
                tail.next = Some(Box::new(ListNode::new(values[idx])));
                tail = tail.next.as_mut().unwrap();
                idx += 1;
            }
            result.push(dummy.next);
        }
        result
    }
}
