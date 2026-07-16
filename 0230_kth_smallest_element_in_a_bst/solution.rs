// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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
    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut current = root;
        let mut remaining = k;

        while current.is_some() || !stack.is_empty() {
            while let Some(node) = current {
                stack.push(node.clone());
                current = node.borrow().left.clone();
            }
            let node = stack.pop().unwrap();
            remaining -= 1;
            if remaining == 0 {
                return node.borrow().val;
            }
            current = node.borrow().right.clone();
        }

        -1
    }
}
