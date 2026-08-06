// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn lca_deepest_leaves(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        Self::dfs(root).0
    }

    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
    ) -> (Option<Rc<RefCell<TreeNode>>>, i32) {
        let node = match node {
            Some(n) => n,
            None => return (None, 0),
        };
        let (left, right) = {
            let b = node.borrow();
            (b.left.clone(), b.right.clone())
        };
        let (ln, ld) = Self::dfs(left);
        let (rn, rd) = Self::dfs(right);
        if ld > rd {
            (ln, ld + 1)
        } else if rd > ld {
            (rn, rd + 1)
        } else {
            (Some(node), ld + 1)
        }
    }
}
