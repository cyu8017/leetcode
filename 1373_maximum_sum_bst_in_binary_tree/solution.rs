// LeetCode 1373 - Maximum Sum BST in Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn max_sum_bst(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> (bool, i32, i32, i32) {
            let Some(node) = node else {
                return (true, i32::MAX, i32::MIN, 0);
            };
            let n = node.borrow();
            let (a, lx, lh, ls) = dfs(n.left.clone(), ans);
            let (b, rx, rh, rs) = dfs(n.right.clone(), ans);
            if a && b && lh < n.val && n.val < rx {
                let s = ls + rs + n.val;
                *ans = (*ans).max(s);
                (true, lx.min(n.val), rh.max(n.val), s)
            } else {
                (false, 0, 0, 0)
            }
        }
        let mut ans = 0;
        dfs(root, &mut ans);
        ans
    }
}
