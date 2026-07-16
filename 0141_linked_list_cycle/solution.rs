// LeetCode 0141 - Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
pub fn has_cycle(head: Option<Box<ListNode>>) -> bool {
    let mut slow = head.as_deref();
    let mut fast = head.as_deref();

    while let Some(fast_node) = fast {
        let Some(next_fast) = fast_node.next.as_deref() else {
            return false;
        };

        slow = slow.and_then(|node| node.next.as_deref());
        fast = next_fast.next.as_deref();

        if let (Some(slow_node), Some(fast_node)) = (slow, fast) {
            if std::ptr::eq(slow_node, fast_node) {
                return true;
            }
        }
    }
    false
}
}
// LeetCode 0141 - Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

impl Solution {
    pub fn solve() {
    }
}