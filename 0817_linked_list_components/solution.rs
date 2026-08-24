// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

use std::collections::HashSet;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn num_components(head: Option<Box<ListNode>>, nums: Vec<i32>) -> i32 {
        let present: HashSet<i32> = nums.into_iter().collect();
        let mut count = 0;
        let mut connected = false;
        let mut cur = head;
        while let Some(node) = cur {
            if present.contains(&node.val) {
                if !connected {
                    count += 1;
                    connected = true;
                }
            } else {
                connected = false;
            }
            cur = node.next;
        }
        count
    }
}
