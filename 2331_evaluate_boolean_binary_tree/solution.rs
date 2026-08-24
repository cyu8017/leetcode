// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn evaluate_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let root = root.unwrap();
        let node = root.borrow();
        if node.left.is_none() && node.right.is_none() {
            return node.val == 1;
        }
        let l = Self::evaluate_tree(node.left.clone());
        let r = Self::evaluate_tree(node.right.clone());
        if node.val == 2 {
            l || r
        } else {
            l && r
        }
    }
}
