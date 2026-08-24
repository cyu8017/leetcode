// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

use std::cell::RefCell;
use std::collections::VecDeque;
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
    pub fn is_complete_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut q = VecDeque::new();
        q.push_back(root);
        let mut end = false;
        while let Some(node) = q.pop_front() {
            match node {
                None => end = true,
                Some(n) => {
                    if end {
                        return false;
                    }
                    let n = n.borrow();
                    q.push_back(n.left.clone());
                    q.push_back(n.right.clone());
                }
            }
        }
        true
    }
}
