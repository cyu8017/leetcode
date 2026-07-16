// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

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
    pub fn generate_trees(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if n == 0 {
            return vec![];
        }
        Self::build(1, n)
    }

    fn build(start: i32, end: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if start > end {
            return vec![None];
        }
        let mut trees = Vec::new();
        for root_val in start..=end {
            let left_trees = Self::build(start, root_val - 1);
            let right_trees = Self::build(root_val + 1, end);
            for left in &left_trees {
                for right in &right_trees {
                    let mut root = TreeNode::new(root_val);
                    root.left = left.clone();
                    root.right = right.clone();
                    trees.push(Some(Rc::new(RefCell::new(root))));
                }
            }
        }
        trees
    }
}
