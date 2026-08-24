struct Solution;
// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

use std::collections::HashSet;

#[derive(PartialEq, Eq, Clone, Debug)]
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
    pub fn modified_list(nums: Vec<i32>, mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let s: HashSet<i32> = nums.into_iter().collect();
        let mut dummy = ListNode { val: 0, next: None };
        let mut tail = &mut dummy;
        while let Some(mut node) = head {
            head = node.next.take();
            if !s.contains(&node.val) {
                tail.next = Some(node);
                tail = tail.next.as_mut().unwrap();
            }
        }
        dummy.next
    }
}

fn main() {}
