// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

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
    pub fn height_of_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::dfs(root)
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(n) = node else {
            return -1;
        };
        let left = n.borrow().left.clone();
        let right = n.borrow().right.clone();
        if let Some(l) = &left {
            if let Some(lr) = l.borrow().right.clone() {
                if Rc::ptr_eq(&lr, &n) {
                    return Self::dfs(right) + 1;
                }
            }
        }
        if let Some(r) = &right {
            if let Some(rl) = r.borrow().left.clone() {
                if Rc::ptr_eq(&rl, &n) {
                    return Self::dfs(left) + 1;
                }
            }
        }
        Self::dfs(left).max(Self::dfs(right)) + 1
    }
}
