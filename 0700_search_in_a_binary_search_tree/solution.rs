// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

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
    pub fn search_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let mut current = root;
        while let Some(node) = current {
            let node_val = node.borrow().val;
            if node_val == val {
                return Some(node);
            }
            current = if val < node_val {
                node.borrow().left.clone()
            } else {
                node.borrow().right.clone()
            };
        }
        None
    }
}
