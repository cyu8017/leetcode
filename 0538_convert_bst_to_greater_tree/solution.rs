// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

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
    pub fn convert_bst(root: Option<Rc<RefCell<TreeNode>>>) {
        let mut running = 0;

        fn reverse_inorder(node: Option<Rc<RefCell<TreeNode>>>, running: &mut i32) {
            if let Some(current) = node {
                reverse_inorder(current.borrow().right.clone(), running);
                let mut borrowed = current.borrow_mut();
                *running += borrowed.val;
                borrowed.val = *running;
                let left = borrowed.left.clone();
                drop(borrowed);
                reverse_inorder(left, running);
            }
        }

        reverse_inorder(root, &mut running);
    }
}
