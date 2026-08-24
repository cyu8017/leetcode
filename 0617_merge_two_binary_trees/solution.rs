// LeetCode 0617 - Merge Two Binary Trees
// https://leetcode.com/problems/merge-two-binary-trees/

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
    pub fn merge_trees(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        match (root1, root2) {
            (None, r) | (r, None) => r,
            (Some(a), Some(b)) => {
                let mut a_ref = a.borrow_mut();
                let b_ref = b.borrow();
                a_ref.val += b_ref.val;
                let left = Self::merge_trees(a_ref.left.clone(), b_ref.left.clone());
                let right = Self::merge_trees(a_ref.right.clone(), b_ref.right.clone());
                a_ref.left = left;
                a_ref.right = right;
                drop(a_ref);
                Some(a)
            }
        }
    }
}
