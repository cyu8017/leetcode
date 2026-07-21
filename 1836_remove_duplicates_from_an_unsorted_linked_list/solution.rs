// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

use std::collections::HashMap;

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn delete_duplicates_unsorted(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut counts = HashMap::new();
        let mut node = head.as_ref();
        while let Some(curr) = node {
            *counts.entry(curr.val).or_insert(0) += 1;
            node = curr.next.as_ref();
        }

        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut current = &mut dummy;
        while let Some(mut node) = current.next.take() {
            if counts.get(&node.val).copied().unwrap_or(0) > 1 {
                current.next = node.next.take();
            } else {
                current.next = Some(node);
                current = current.next.as_mut().unwrap();
            }
        }
        dummy.next
    }
}
