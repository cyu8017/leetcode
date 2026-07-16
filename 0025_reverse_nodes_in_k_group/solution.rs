// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let k = k as usize;
        let mut values = Vec::new();
        let mut current = head.as_ref();
        while let Some(node) = current {
            values.push(node.val);
            current = node.next.as_ref();
        }

        let mut index = 0;
        while index + k <= values.len() {
            values[index..index + k].reverse();
            index += k;
        }

        let mut dummy = ListNode { val: 0, next: None };
        let mut tail = &mut dummy;
        for value in values {
            tail.next = Some(Box::new(ListNode { val: value, next: None }));
            tail = tail.next.as_mut().unwrap();
        }
        dummy.next
    }
}
