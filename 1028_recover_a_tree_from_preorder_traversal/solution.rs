// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

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
    pub fn recover_from_preorder(traversal: String) -> Option<Rc<RefCell<TreeNode>>> {
        let bytes = traversal.as_bytes();
        let n = bytes.len();
        let mut i = 0;
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        while i < n {
            let mut depth = 0;
            while i < n && bytes[i] == b'-' {
                depth += 1;
                i += 1;
            }
            let start = i;
            while i < n && bytes[i].is_ascii_digit() {
                i += 1;
            }
            let val: i32 = std::str::from_utf8(&bytes[start..i])
                .unwrap()
                .parse()
                .unwrap();
            let node = Rc::new(RefCell::new(TreeNode::new(val)));
            while stack.len() > depth {
                stack.pop();
            }
            if let Some(parent) = stack.last() {
                let mut p = parent.borrow_mut();
                if p.left.is_none() {
                    p.left = Some(node.clone());
                } else {
                    p.right = Some(node.clone());
                }
            }
            stack.push(node);
        }
        stack.first().cloned()
    }
}
