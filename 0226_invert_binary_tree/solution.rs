// LeetCode 0226 - Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

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
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = &root {
            let mut node_ref = node.borrow_mut();
            let left = node_ref.left.take();
            let right = node_ref.right.take();
            node_ref.left = Self::invert_tree(right);
            node_ref.right = Self::invert_tree(left);
        }
        root
    }
}
