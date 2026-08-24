// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

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
    pub fn smallest_from_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, path: &mut String, best: &mut String) {
            let Some(n) = node else { return };
            let n = n.borrow();
            path.insert(0, (b'a' + n.val as u8) as char);
            if n.left.is_none() && n.right.is_none() {
                if path.as_str() < best.as_str() {
                    *best = path.clone();
                }
            } else {
                dfs(&n.left, path, best);
                dfs(&n.right, path, best);
            }
            path.remove(0);
        }
        let mut best = "~".to_string();
        let mut path = String::new();
        dfs(&root, &mut path, &mut best);
        best
    }
}
