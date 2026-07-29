// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

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
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, lo: i32, hi: i32) -> i32 {
            match node {
                None => hi - lo,
                Some(rc) => {
                    let n = rc.borrow();
                    let lo = lo.min(n.val);
                    let hi = hi.max(n.val);
                    dfs(n.left.clone(), lo, hi).max(dfs(n.right.clone(), lo, hi))
                }
            }
        }
        let root = root.unwrap();
        let val = root.borrow().val;
        dfs(Some(root), val, val)
    }
}
