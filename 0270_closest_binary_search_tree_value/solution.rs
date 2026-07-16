// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

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
    pub fn closest_value(root: Option<Rc<RefCell<TreeNode>>>, target: f64) -> i32 {
        let mut closest = root.as_ref().unwrap().borrow().val;
        let mut current = root;
        while let Some(node) = current {
            let (left, right, val) = {
                let borrowed = node.borrow();
                (
                    borrowed.left.clone(),
                    borrowed.right.clone(),
                    borrowed.val,
                )
            };
            if (closest as f64 - target).abs() > (val as f64 - target).abs() {
                closest = val;
            }
            if val as f64 == target {
                return val;
            }
            current = if target < val as f64 { left } else { right };
        }
        closest
    }
}
