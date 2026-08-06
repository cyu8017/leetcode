// LeetCode 1325 - Delete Leaves With a Given Value
// https://leetcode.com/problems/delete-leaves-with-a-given-value/

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
        TreeNode { val, left: None, right: None }
    }
}

impl Solution {
    pub fn remove_leaf_nodes(
        root: Option<Rc<RefCell<TreeNode>>>,
        target: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let root = root?;
        {
            let mut n = root.borrow_mut();
            n.left = Self::remove_leaf_nodes(n.left.take(), target);
            n.right = Self::remove_leaf_nodes(n.right.take(), target);
            if n.left.is_none() && n.right.is_none() && n.val == target {
                return None;
            }
        }
        Some(root)
    }
}
