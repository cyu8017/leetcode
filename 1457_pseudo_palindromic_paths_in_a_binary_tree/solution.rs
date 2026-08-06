// LeetCode 1457 - Pseudo-Palindromic Paths in a Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn pseudo_palindromic_paths(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, mut mask: i32) -> i32 {
            let Some(node) = node else { return 0 };
            let n = node.borrow();
            mask ^= 1 << n.val;
            if n.left.is_none() && n.right.is_none() {
                return i32::from(mask & (mask - 1) == 0);
            }
            dfs(n.left.clone(), mask) + dfs(n.right.clone(), mask)
        }
        dfs(root, 0)
    }
}
