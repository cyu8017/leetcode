// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

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
    pub fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        let mut result = Vec::new();
        Self::dfs(root, Vec::new(), &mut result);
        result
    }

    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
        mut path: Vec<String>,
        result: &mut Vec<String>,
    ) {
        let Some(node) = node else {
            return;
        };
        let (left, right, val) = {
            let borrowed = node.borrow();
            (
                borrowed.left.clone(),
                borrowed.right.clone(),
                borrowed.val,
            )
        };
        path.push(val.to_string());
        if left.is_none() && right.is_none() {
            result.push(path.join("->"));
            return;
        }
        Self::dfs(left, path.clone(), result);
        Self::dfs(right, path, result);
    }
}
