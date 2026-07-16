// LeetCode 0236 - Lowest Common Ancestor of a Binary Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

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
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if Self::ptr_eq(&root, &p) || Self::ptr_eq(&root, &q) {
            return root;
        }
        let root = root?;
        let left = Self::lowest_common_ancestor(root.borrow().left.clone(), p, q);
        let right = Self::lowest_common_ancestor(root.borrow().right.clone(), p, q);
        if left.is_some() && right.is_some() {
            Some(root)
        } else {
            left.or(right)
        }
    }

    fn ptr_eq(
        a: &Option<Rc<RefCell<TreeNode>>>,
        b: &Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (a, b) {
            (Some(x), Some(y)) => Rc::ptr_eq(x, y),
            (None, None) => true,
            _ => false,
        }
    }
}
