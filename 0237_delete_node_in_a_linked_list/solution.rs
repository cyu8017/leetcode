// LeetCode 0237 - Delete Node in a Linked List
// https://leetcode.com/problems/delete-node-in-a-linked-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn delete_node(node: &mut ListNode) {
        let next = node.next.take().unwrap();
        node.val = next.val;
        node.next = next.next;
    }
}
