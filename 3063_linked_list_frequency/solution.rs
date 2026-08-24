// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

use std::collections::HashMap;


#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn frequencies_of_elements(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut cnt = HashMap::new();
        while let Some(node) = head {
            *cnt.entry(node.val).or_insert(0) += 1;
            head = node.next;
        }
        let mut dummy = ListNode { val: 0, next: None };
        for &val in cnt.values() {
            dummy.next = Some(Box::new(ListNode {
                val,
                next: dummy.next.take(),
            }));
        }
        dummy.next
    }
}
