// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

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
    pub fn sort_linked_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut vals = Vec::new();
        let mut cur = head.as_ref();
        while let Some(n) = cur {
            vals.push(n.val);
            cur = n.next.as_ref();
        }
        if vals.is_empty() {
            return None;
        }
        let mut list = vals;
        let mut i = 1;
        while i < list.len() {
            if list[i] < 0 {
                let v = list.remove(i);
                list.insert(0, v);
            } else {
                i += 1;
            }
        }
        let mut out = None;
        for &v in list.iter().rev() {
            out = Some(Box::new(ListNode { val: v, next: out }));
        }
        out
    }
}
