// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

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
    pub fn is_unival_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let Some(root) = root else {
            return true;
        };
        let v = root.borrow().val;
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, v: i32) -> bool {
            match node {
                None => true,
                Some(n) => {
                    let n = n.borrow();
                    n.val == v && dfs(n.left.clone(), v) && dfs(n.right.clone(), v)
                }
            }
        }
        dfs(Some(root), v)
    }
}
