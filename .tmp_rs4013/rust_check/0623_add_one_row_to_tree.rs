struct Solution;
// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

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
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, current: i32, val: i32, depth: i32) {
        let Some(node) = node else {
            return;
        };
        let mut node = node.borrow_mut();
        if current == depth - 1 {
            node.left = Some(Rc::new(RefCell::new(TreeNode {
                val,
                left: node.left.clone(),
                right: None,
            })));
            node.right = Some(Rc::new(RefCell::new(TreeNode {
                val,
                left: None,
                right: node.right.clone(),
            })));
            return;
        }
        Self::dfs(&node.left, current + 1, val, depth);
        Self::dfs(&node.right, current + 1, val, depth);
    }

    pub fn add_one_row(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
        depth: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if depth == 1 {
            return Some(Rc::new(RefCell::new(TreeNode {
                val,
                left: root,
                right: None,
            })));
        }
        Self::dfs(&root, 1, val, depth);
        root
    }
}

fn main() {}
