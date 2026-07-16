// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

struct HeapNode {
    val: i32,
    node: ListNode,
}

impl PartialEq for HeapNode {
    fn eq(&self, other: &Self) -> bool {
        self.val == other.val
    }
}

impl Eq for HeapNode {}

impl PartialOrd for HeapNode {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(other.val.cmp(&self.val))
    }
}

impl Ord for HeapNode {
    fn cmp(&self, other: &Self) -> Ordering {
        other.val.cmp(&self.val)
    }
}

impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        let mut heap = BinaryHeap::new();
        for node in lists.into_iter().flatten() {
            heap.push(HeapNode {
                val: node.val,
                node: *node,
            });
        }

        let mut dummy = ListNode { val: 0, next: None };
        let mut current = &mut dummy;

        while let Some(item) = heap.pop() {
            let mut node = item.node;
            if let Some(next) = node.next.take() {
                heap.push(HeapNode {
                    val: next.val,
                    node: *next,
                });
            }
            current.next = Some(Box::new(node));
            current = current.next.as_mut().unwrap();
        }

        dummy.next
    }
}
