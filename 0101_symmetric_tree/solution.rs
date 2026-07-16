// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match root {
            None => true,
            Some(node) => {
                let node = node.borrow();
                Self::mirrors(node.left.clone(), node.right.clone())
            }
        }
    }

    fn mirrors(
        left: Option<Rc<RefCell<TreeNode>>>,
        right: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (left, right) {
            (None, None) => true,
            (Some(left), Some(right)) => {
                let left = left.borrow();
                let right = right.borrow();
                left.val == right.val
                    && Self::mirrors(left.left.clone(), right.right.clone())
                    && Self::mirrors(left.right.clone(), right.left.clone())
            }
            _ => false,
        }
    }
}
