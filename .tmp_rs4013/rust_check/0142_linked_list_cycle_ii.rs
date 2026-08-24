struct Solution;
// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn detect_cycle(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut slow = head.as_deref();
        let mut fast = head.as_deref();
        let mut met = false;
        while let Some(fast_node) = fast {
            let Some(next_fast) = fast_node.next.as_deref() else {
                break;
            };
            slow = slow.and_then(|node| node.next.as_deref());
            fast = next_fast.next.as_deref();
            if let (Some(s), Some(f)) = (slow, fast) {
                if std::ptr::eq(s, f) {
                    met = true;
                    break;
                }
            }
        }
        if !met {
            return None;
        }
        let mut p1 = head.as_deref();
        let mut p2 = slow;
        while let (Some(a), Some(b)) = (p1, p2) {
            if std::ptr::eq(a, b) {
                return Some(Box::new(ListNode { val: a.val, next: None }));
            }
            p1 = a.next.as_deref();
            p2 = b.next.as_deref();
        }
        None
    }
}

fn main() {}
