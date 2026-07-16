// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

// Rust's ownership-safe `Box<ListNode>` representation cannot contain a cycle.
// Consequently, no cycle entry can exist in this signature.
impl Solution {
pub fn detect_cycle(_head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    None
}
}
// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

impl Solution {
    pub fn solve() {
    }
}