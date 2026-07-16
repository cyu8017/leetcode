// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

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
    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut best = i32::MAX;
        let mut previous: Option<i32> = None;

        fn inorder(
            node: Option<Rc<RefCell<TreeNode>>>,
            best: &mut i32,
            previous: &mut Option<i32>,
        ) {
            if let Some(current) = node {
                inorder(current.borrow().left.clone(), best, previous);
                let value = current.borrow().val;
                if let Some(prev) = *previous {
                    *best = (*best).min(value - prev);
                }
                *previous = Some(value);
                inorder(current.borrow().right.clone(), best, previous);
            }
        }

        inorder(root, &mut best, &mut previous);
        best
    }
}
