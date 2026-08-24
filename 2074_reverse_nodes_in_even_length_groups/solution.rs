// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

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
    pub fn reverse_even_length_groups(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut vals = Vec::new();
        let mut cur = head.as_ref();
        while let Some(n) = cur {
            vals.push(n.val);
            cur = n.next.as_ref();
        }
        let mut i = 0;
        let mut group = 1;
        while i < vals.len() {
            let cnt = group.min(vals.len() - i);
            if cnt % 2 == 0 {
                vals[i..i + cnt].reverse();
            }
            i += cnt;
            group += 1;
        }
        let mut out = None;
        for &v in vals.iter().rev() {
            out = Some(Box::new(ListNode { val: v, next: out }));
        }
        out
    }
}
