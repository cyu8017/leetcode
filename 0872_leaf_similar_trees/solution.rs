// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

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
    pub fn leaf_similar(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        Self::leaves(root1) == Self::leaves(root2)
    }

    fn leaves(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        Self::dfs(root, &mut result);
        result
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
        if let Some(node) = node {
            let node = node.borrow();
            if node.left.is_none() && node.right.is_none() {
                result.push(node.val);
                return;
            }
            Self::dfs(node.left.clone(), result);
            Self::dfs(node.right.clone(), result);
        }
    }
}
