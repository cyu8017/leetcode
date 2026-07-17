// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn swap_nodes(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut vals = Vec::new();
        let mut node = head.as_deref();
        while let Some(current) = node {
            vals.push(current.val);
            node = current.next.as_deref();
        }
        let i = k as usize - 1;
        let j = vals.len() - k as usize;
        vals.swap(i, j);
        let mut idx = 0;
        let mut node = head.as_deref_mut();
        while let Some(current) = node {
            if idx == i || idx == j {
                current.val = vals[idx];
            }
            idx += 1;
            node = current.next.as_deref_mut();
        }
        head
    }
}
