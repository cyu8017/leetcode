// LeetCode 0206 - Reverse Linked List
#[derive(PartialEq, Eq)]
pub struct ListNode { pub val: i32, pub next: Option<Box<ListNode>> }
impl Solution { pub fn reverse_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> { let mut previous = None; while let Some(mut node) = head { head = node.next.take(); node.next = previous; previous = Some(node); } previous } }
