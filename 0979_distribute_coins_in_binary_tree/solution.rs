// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

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
    pub fn distribute_coins(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {
            let Some(n) = node else { return 0 };
            let n = n.borrow();
            let left = dfs(&n.left, ans);
            let right = dfs(&n.right, ans);
            *ans += left.abs() + right.abs();
            n.val + left + right - 1
        }
        let mut ans = 0;
        dfs(&root, &mut ans);
        ans
    }
}
