// LeetCode 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn is_valid_sequence(root: Option<Rc<RefCell<TreeNode>>>, arr: Vec<i32>) -> bool {
        fn visit(node: Option<Rc<RefCell<TreeNode>>>, arr: &[i32], index: usize) -> bool {
            let Some(node) = node else { return false };
            if index == arr.len() {
                return false;
            }
            let n = node.borrow();
            if n.val != arr[index] {
                return false;
            }
            if n.left.is_none() && n.right.is_none() {
                return index == arr.len() - 1;
            }
            visit(n.left.clone(), arr, index + 1) || visit(n.right.clone(), arr, index + 1)
        }
        visit(root, &arr, 0)
    }
}
