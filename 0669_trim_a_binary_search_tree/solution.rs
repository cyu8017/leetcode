// LeetCode 0669 - Trim a Binary Search Tree
// https://leetcode.com/problems/trim-a-binary-search-tree/

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
    pub fn trim_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
        low: i32,
        high: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let root = root?;
        let val = root.borrow().val;
        if val < low {
            return Self::trim_bst(root.borrow().right.clone(), low, high);
        }
        if val > high {
            return Self::trim_bst(root.borrow().left.clone(), low, high);
        }
        {
            let mut node = root.borrow_mut();
            node.left = Self::trim_bst(node.left.clone(), low, high);
            node.right = Self::trim_bst(node.right.clone(), low, high);
        }
        Some(root)
    }
}
