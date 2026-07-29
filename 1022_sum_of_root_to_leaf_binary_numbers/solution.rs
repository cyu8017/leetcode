// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

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
    pub fn sum_root_to_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, value: i32) -> i32 {
            match node {
                None => 0,
                Some(rc) => {
                    let n = rc.borrow();
                    let value = value * 2 + n.val;
                    if n.left.is_none() && n.right.is_none() {
                        value
                    } else {
                        dfs(n.left.clone(), value) + dfs(n.right.clone(), value)
                    }
                }
            }
        }
        dfs(root, 0)
    }
}
