// LeetCode 0203 - Remove Linked List Elements
#[derive(PartialEq, Eq)]
pub struct ListNode { pub val: i32, pub next: Option<Box<ListNode>> }
impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: head }); let mut current = &mut dummy;
        while let Some(mut node) = current.next.take() {
            if node.val == val {
                current.next = node.next.take();
            } else {
                current.next = Some(node);
                current = current.next.as_mut().unwrap();
            }
        }
        dummy.next
    }
}
