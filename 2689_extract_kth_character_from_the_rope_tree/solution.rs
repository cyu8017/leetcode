// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

use std::cell::RefCell;
use std::rc::Rc;

pub struct RopeTreeNode {
    pub len: i32,
    pub val: char,
    pub left: Option<Rc<RefCell<RopeTreeNode>>>,
    pub right: Option<Rc<RefCell<RopeTreeNode>>>,
}

impl Solution {
    pub fn get_kth_character(root: Option<Rc<RefCell<RopeTreeNode>>>, k: i32) -> char {
        fn dfs(node: &Rc<RefCell<RopeTreeNode>>, kk: i32) -> char {
            let n = node.borrow();
            if n.left.is_none() && n.right.is_none() {
                return n.val;
            }
            let left_len = if let Some(ref left) = n.left {
                let llen = left.borrow().len;
                if llen > 0 {
                    llen
                } else {
                    1
                }
            } else {
                0
            };
            if kk <= left_len {
                dfs(n.left.as_ref().unwrap(), kk)
            } else {
                dfs(n.right.as_ref().unwrap(), kk - left_len)
            }
        }
        dfs(root.as_ref().unwrap(), k)
    }
}
