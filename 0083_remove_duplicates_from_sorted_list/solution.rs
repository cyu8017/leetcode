// LeetCode 0083 - Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn delete_duplicates(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut current = head.as_mut();

        while let Some(node) = current {
            while node.next.as_ref().map_or(false, |n| n.val == node.val) {
                node.next = node.next.as_mut().unwrap().next.take();
            }
            current = node.next.as_mut();
        }

        head
    }
}
