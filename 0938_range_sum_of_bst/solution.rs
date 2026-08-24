// LeetCode 0938 - Range Sum of BST
// https://leetcode.com/problems/range-sum-of-bst/

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
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        match root {
            None => 0,
            Some(node) => {
                let node = node.borrow();
                if node.val < low {
                    Self::range_sum_bst(node.right.clone(), low, high)
                } else if node.val > high {
                    Self::range_sum_bst(node.left.clone(), low, high)
                } else {
                    node.val
                        + Self::range_sum_bst(node.left.clone(), low, high)
                        + Self::range_sum_bst(node.right.clone(), low, high)
                }
            }
        }
    }
}
