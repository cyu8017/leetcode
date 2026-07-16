// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::valid(root.as_ref(), i64::MIN, i64::MAX)
    }

    fn valid(node: Option<&Rc<RefCell<TreeNode>>>, low: i64, high: i64) -> bool {
        match node {
            None => true,
            Some(n) => {
                let n = n.borrow();
                let val = n.val as i64;
                if !(low < val && val < high) {
                    return false;
                }
                Self::valid(n.left.as_ref(), low, val) && Self::valid(n.right.as_ref(), val, high)
            }
        }
    }
}
