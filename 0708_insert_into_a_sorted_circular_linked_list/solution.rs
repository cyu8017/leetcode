// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

#[derive(Debug, PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn insert(head: Option<Box<ListNode>>, insert_val: i32) -> Option<Box<ListNode>> {
        let mut values = Vec::new();
        let mut current = head;
        while let Some(node) = current {
            values.push(node.val);
            current = node.next;
        }
        if values.is_empty() {
            return Some(Box::new(ListNode::new(insert_val)));
        }

        let n = values.len();
        let mut insert_after = n - 1;
        for i in 0..n {
            let prev = values[i];
            let curr = values[(i + 1) % n];
            if (prev <= insert_val && insert_val <= curr)
                || (prev > curr && (insert_val >= prev || insert_val <= curr))
            {
                insert_after = i;
                break;
            }
        }
        values.insert(insert_after + 1, insert_val);

        let mut dummy = ListNode::new(0);
        let mut tail = &mut dummy;
        for val in values {
            tail.next = Some(Box::new(ListNode::new(val)));
            tail = tail.next.as_mut().unwrap();
        }
        dummy.next
    }
}
