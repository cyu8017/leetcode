// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

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
    pub fn split_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
        target: i32,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let Some(node) = root else {
            return vec![None, None];
        };
        if node.borrow().val <= target {
            let right = node.borrow_mut().right.take();
            let mut parts = Self::split_bst(right, target);
            node.borrow_mut().right = parts[0].take();
            vec![Some(node), parts[1].take()]
        } else {
            let left = node.borrow_mut().left.take();
            let mut parts = Self::split_bst(left, target);
            node.borrow_mut().left = parts[1].take();
            vec![parts[0].take(), Some(node)]
        }
    }
}
