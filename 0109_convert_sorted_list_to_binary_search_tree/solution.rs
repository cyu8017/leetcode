// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

impl Solution {
    pub fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut values = Vec::new();
        let mut current = head;
        while let Some(node) = current {
            values.push(node.val);
            current = node.next;
        }
        Self::build(&values, 0, values.len() as i32 - 1)
    }

    fn build(values: &[i32], left: i32, right: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if left > right {
            return None;
        }
        let mid = (left + right + 1) / 2;
        let mut root = TreeNode::new(values[mid as usize]);
        root.left = Self::build(values, left, mid - 1);
        root.right = Self::build(values, mid + 1, right);
        Some(Rc::new(RefCell::new(root)))
    }
}
