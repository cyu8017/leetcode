// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

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
    pub fn count_dominant_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut ans = 0;
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {
            let Some(node) = node else {
                return i32::MIN;
            };
            let node = node.borrow();
            let l = dfs(&node.left, ans);
            let r = dfs(&node.right, ans);
            let mx = l.max(r).max(node.val);
            if mx == node.val {
                *ans += 1;
            }
            mx
        }
        dfs(&root, &mut ans);
        ans
    }
}
