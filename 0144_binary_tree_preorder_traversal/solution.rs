// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut stack = Vec::new();
        if let Some(root) = root {
            stack.push(root);
        }

        while let Some(node) = stack.pop() {
            let node = node.borrow();
            result.push(node.val);
            if let Some(right) = node.right.clone() {
                stack.push(right);
            }
            if let Some(left) = node.left.clone() {
                stack.push(left);
            }
        }
        result
    }
}