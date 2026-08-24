// LeetCode 0814 - Binary Tree Pruning
// https://leetcode.com/problems/binary-tree-pruning/

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
    pub fn prune_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let node = root?;
        {
            let mut n = node.borrow_mut();
            n.left = Self::prune_tree(n.left.take());
            n.right = Self::prune_tree(n.right.take());
            if n.val == 0 && n.left.is_none() && n.right.is_none() {
                return None;
            }
        }
        Some(node)
    }
}
