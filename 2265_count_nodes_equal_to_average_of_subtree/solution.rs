// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

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
    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> (i32, i32) {
            let Some(node) = node else {
                return (0, 0);
            };
            let n = node.borrow();
            let (ls, lc) = dfs(n.left.clone(), ans);
            let (rs, rc) = dfs(n.right.clone(), ans);
            let sum = ls + rs + n.val;
            let cnt = lc + rc + 1;
            if sum / cnt == n.val {
                *ans += 1;
            }
            (sum, cnt)
        }
        let mut ans = 0;
        dfs(root, &mut ans);
        ans
    }
}
