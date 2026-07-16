// LeetCode 0366 - Find Leaves of Binary Tree
// https://leetcode.com/problems/find-leaves-of-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    pub fn new(val: i32) -> Self {
        Self {
            val,
            left: None,
            right: None,
        }
    }
}

impl Solution {
    pub fn find_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut layers: Vec<Vec<i32>> = Vec::new();
        Self::dfs(root, &mut layers);
        layers
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, layers: &mut Vec<Vec<i32>>) -> i32 {
        let Some(node) = node else {
            return -1;
        };

        let node = node.borrow();
        let left = node.left.clone();
        let right = node.right.clone();
        let value = node.val;
        drop(node);

        let height = Self::dfs(left, layers).max(Self::dfs(right, layers)) + 1;
        while layers.len() <= height as usize {
            layers.push(Vec::new());
        }
        layers[height as usize].push(value);
        height
    }
}
