// LeetCode 0951 - Flip Equivalent Binary Trees
// https://leetcode.com/problems/flip-equivalent-binary-trees/

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
    pub fn flip_equiv(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (root1, root2) {
            (None, None) => true,
            (Some(a), Some(b)) => {
                let a = a.borrow();
                let b = b.borrow();
                if a.val != b.val {
                    return false;
                }
                (Self::flip_equiv(a.left.clone(), b.left.clone())
                    && Self::flip_equiv(a.right.clone(), b.right.clone()))
                    || (Self::flip_equiv(a.left.clone(), b.right.clone())
                        && Self::flip_equiv(a.right.clone(), b.left.clone()))
            }
            _ => false,
        }
    }
}
