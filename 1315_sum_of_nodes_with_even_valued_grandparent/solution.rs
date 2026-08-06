// LeetCode 1315 - Sum of Nodes with Even-Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

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
        TreeNode { val, left: None, right: None }
    }
}

impl Solution {
    pub fn sum_even_grandparent(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(
            node: Option<Rc<RefCell<TreeNode>>>,
            parent: Option<i32>,
            grandparent: Option<i32>,
        ) -> i32 {
            let Some(node) = node else { return 0 };
            let n = node.borrow();
            let add = if grandparent.map(|v| v % 2 == 0).unwrap_or(false) {
                n.val
            } else {
                0
            };
            add + dfs(n.left.clone(), Some(n.val), parent)
                + dfs(n.right.clone(), Some(n.val), parent)
        }
        dfs(root, None, None)
    }
}
