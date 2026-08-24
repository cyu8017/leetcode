struct Solution;
// LeetCode 3831 - Median of a Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn level_median(root: Option<Rc<RefCell<TreeNode>>>, level: i32) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, i: i32, level: i32, nums: &mut Vec<i32>) {
            let Some(node) = node else {
                return;
            };
            let node = node.borrow();
            dfs(node.left.clone(), i + 1, level, nums);
            if i == level {
                nums.push(node.val);
            }
            dfs(node.right.clone(), i + 1, level, nums);
        }
        let mut nums = Vec::new();
        dfs(root, 0, level, &mut nums);
        if nums.is_empty() {
            return -1;
        }
        nums[nums.len() / 2]
    }
}
