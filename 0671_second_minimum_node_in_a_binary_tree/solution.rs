// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

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
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, root_val: i32, ans: &mut i32) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        if node.val > root_val {
            if *ans == -1 || node.val < *ans {
                *ans = node.val;
            }
            return;
        }
        Self::dfs(&node.left, root_val, ans);
        Self::dfs(&node.right, root_val, ans);
    }

    pub fn find_second_minimum_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(root_rc) = root else {
            return -1;
        };
        let root_val = root_rc.borrow().val;
        let mut ans = -1;
        Self::dfs(&Some(root_rc), root_val, &mut ans);
        ans
    }
}
