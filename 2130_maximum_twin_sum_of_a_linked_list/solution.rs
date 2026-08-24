// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let mut vals = Vec::new();
        let mut cur = head.as_ref();
        while let Some(node) = cur {
            vals.push(node.val);
            cur = node.next.as_ref();
        }
        let n = vals.len();
        (0..n / 2).map(|i| vals[i] + vals[n - 1 - i]).max().unwrap_or(0)
    }
}
