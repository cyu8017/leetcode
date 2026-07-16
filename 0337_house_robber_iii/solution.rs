// LeetCode 0337 - House Robber III
// https://leetcode.com/problems/house-robber-iii/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn rob(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let (with_rob, without_rob) = Self::dfs(root);
        with_rob.max(without_rob)
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
        let Some(node) = node else {
            return (0, 0);
        };

        let (left, right, val) = {
            let borrowed = node.borrow();
            (
                borrowed.left.clone(),
                borrowed.right.clone(),
                borrowed.val,
            )
        };

        let (left_with, left_without) = Self::dfs(left);
        let (right_with, right_without) = Self::dfs(right);

        let with_rob = val + left_without + right_without;
        let without_rob = left_with.max(left_without) + right_with.max(right_without);
        (with_rob, without_rob)
    }
}
