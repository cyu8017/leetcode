// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn merge_nodes(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = ListNode { val: 0, next: None };
        let mut tail = &mut dummy;
        let mut sum = 0;
        let mut p = head.and_then(|h| h.next);
        while let Some(node) = p {
            if node.val == 0 {
                tail.next = Some(Box::new(ListNode { val: sum, next: None }));
                tail = tail.next.as_mut().unwrap();
                sum = 0;
            } else {
                sum += node.val;
            }
            p = node.next;
        }
        dummy.next
    }
}
