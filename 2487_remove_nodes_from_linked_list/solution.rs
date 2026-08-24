// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn remove_nodes(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        fn rev(mut node: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
            let mut prev = None;
            while let Some(mut cur) = node {
                node = cur.next.take();
                cur.next = prev;
                prev = Some(cur);
            }
            prev
        }
        let mut mx = 0;
        let mut dummy = Box::new(ListNode { val: 0, next: rev(head) });
        {
            let mut prev = dummy.as_mut();
            while prev.next.is_some() {
                if prev.next.as_ref().unwrap().val >= mx {
                    mx = prev.next.as_ref().unwrap().val;
                    prev = prev.next.as_mut().unwrap();
                } else {
                    let nxt = prev.next.as_mut().unwrap().next.take();
                    prev.next = nxt;
                }
            }
        }
        rev(dummy.next)
    }
}
