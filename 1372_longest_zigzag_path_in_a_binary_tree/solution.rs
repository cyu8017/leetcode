// LeetCode 1372 - Longest ZigZag Path in a Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn longest_zig_zag(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> (i32, i32) {
            let Some(node) = node else { return (-1, -1) };
            let n = node.borrow();
            let l = dfs(n.left.clone(), ans);
            let r = dfs(n.right.clone(), ans);
            let a = l.1 + 1;
            let b = r.0 + 1;
            *ans = (*ans).max(a).max(b);
            (a, b)
        }
        let mut ans = 0;
        dfs(root, &mut ans);
        ans
    }
}
