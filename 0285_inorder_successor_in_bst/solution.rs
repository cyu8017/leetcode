// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn inorder_successor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let p = p.unwrap();
        let p_val = p.borrow().val;

        if p.borrow().right.is_some() {
            let mut current = p.borrow().right.clone();
            while let Some(node) = current.clone() {
                if node.borrow().left.is_some() {
                    current = node.borrow().left.clone();
                } else {
                    return current;
                }
            }
        }

        let mut successor = None;
        let mut current = root;
        while let Some(node) = current {
            let node_val = node.borrow().val;
            if p_val < node_val {
                successor = Some(node.clone());
                current = node.borrow().left.clone();
            } else {
                current = node.borrow().right.clone();
            }
        }
        successor
    }
}
