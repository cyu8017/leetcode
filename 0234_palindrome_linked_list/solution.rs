// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut slow = head.as_ref();
        let mut fast = head.as_ref();
        while fast.is_some() && fast.as_ref().unwrap().next.is_some() {
            slow = slow.unwrap().next.as_ref();
            fast = fast.unwrap().next.as_ref().unwrap().next.as_ref();
        }

        let mut prev = None;
        let mut current = slow.cloned();
        while let Some(mut node) = current {
            let next = node.next.take();
            node.next = prev;
            prev = Some(node);
            current = next;
        }

        let mut left = head.as_ref();
        let mut right = prev.as_ref();
        while let Some(right_node) = right {
            if left.unwrap().val != right_node.val {
                return false;
            }
            left = left.unwrap().next.as_ref();
            right = right_node.next.as_ref();
        }
        true
    }
}
