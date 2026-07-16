// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn boundary_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        fn is_leaf(node: &Rc<RefCell<TreeNode>>) -> bool {
            let node = node.borrow();
            node.left.is_none() && node.right.is_none()
        }

        fn left_boundary(node: Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
            let Some(node) = node else {
                return;
            };
            if is_leaf(&node) {
                return;
            }
            result.push(node.borrow().val);
            let next = node.borrow().left.clone().or_else(|| node.borrow().right.clone());
            left_boundary(next, result);
        }

        fn right_boundary(node: Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
            let Some(node) = node else {
                return;
            };
            if is_leaf(&node) {
                return;
            }
            let next = node.borrow().right.clone().or_else(|| node.borrow().left.clone());
            right_boundary(next, result);
            result.push(node.borrow().val);
        }

        fn leaves(node: Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
            let Some(node) = node else {
                return;
            };
            if is_leaf(&node) {
                result.push(node.borrow().val);
                return;
            }
            leaves(node.borrow().left.clone(), result);
            leaves(node.borrow().right.clone(), result);
        }

        let Some(root) = root else {
            return Vec::new();
        };
        if is_leaf(&root) {
            return vec![root.borrow().val];
        }

        let mut result = vec![root.borrow().val];
        left_boundary(root.borrow().left.clone(), &mut result);
        leaves(Some(root.clone()), &mut result);
        right_boundary(root.borrow().right.clone(), &mut result);
        result
    }
}
