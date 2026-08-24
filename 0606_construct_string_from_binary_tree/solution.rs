// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

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
    pub fn tree2str(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        let Some(root) = root else {
            return String::new();
        };
        let node = root.borrow();
        let mut result = node.val.to_string();
        if node.left.is_some() || node.right.is_some() {
            result.push('(');
            result.push_str(&Self::tree2str(node.left.clone()));
            result.push(')');
        }
        if node.right.is_some() {
            result.push('(');
            result.push_str(&Self::tree2str(node.right.clone()));
            result.push(')');
        }
        result
    }
}
