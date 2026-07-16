// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn delete_node(root: Option<Rc<RefCell<TreeNode>>>, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
        let Some(root) = root else {
            return None;
        };

        if key < root.borrow().val {
            let left = Self::delete_node(root.borrow_mut().left.take(), key);
            root.borrow_mut().left = left;
            return Some(root);
        }
        if key > root.borrow().val {
            let right = Self::delete_node(root.borrow_mut().right.take(), key);
            root.borrow_mut().right = right;
            return Some(root);
        }

        if root.borrow().left.is_none() {
            return root.borrow_mut().right.take();
        }
        if root.borrow().right.is_none() {
            return root.borrow_mut().left.take();
        }

        let mut successor = root.borrow().right.clone().unwrap();
        while let Some(left) = successor.borrow().left.clone() {
            successor = left;
        }
        let successor_val = successor.borrow().val;
        root.borrow_mut().val = successor_val;
        root.borrow_mut().right = Self::delete_node(root.borrow_mut().right.take(), successor_val);
        Some(root)
    }
}
