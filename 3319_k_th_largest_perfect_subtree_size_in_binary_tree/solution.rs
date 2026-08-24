// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

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
    pub fn kth_largest_perfect_subtree(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut sizes = Vec::new();
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, sizes: &mut Vec<i32>) -> (i32, i32, bool) {
            let Some(n) = node else {
                return (0, 0, true);
            };
            let n = n.borrow();
            let (lh, ls, lp) = dfs(&n.left, sizes);
            let (rh, rs, rp) = dfs(&n.right, sizes);
            let sz = ls + rs + 1;
            let perf = lp && rp && lh == rh;
            if perf {
                sizes.push(sz);
            }
            (lh.max(rh) + 1, sz, perf)
        }
        dfs(&root, &mut sizes);
        sizes.sort_unstable_by(|a, b| b.cmp(a));
        if k as usize > sizes.len() {
            -1
        } else {
            sizes[(k - 1) as usize]
        }
    }
}
