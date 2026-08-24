// LeetCode 2236 - Root Equals Sum of Children
// https://leetcode.com/problems/root-equals-sum-of-children/

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
    pub fn check_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let root = root.unwrap();
        let n = root.borrow();
        let left = n.left.as_ref().unwrap().borrow().val;
        let right = n.right.as_ref().unwrap().borrow().val;
        n.val == left + right
    }
}
