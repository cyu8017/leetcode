// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

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
    pub fn find_nearest_right_node(
        root: Option<Rc<RefCell<TreeNode>>>,
        u: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let (root, u) = match (root, u) {
            (Some(r), Some(u)) => (r, u),
            _ => return None,
        };
        let target = u.borrow().val;
        let mut q = vec![root];
        while !q.is_empty() {
            let mut nxt = Vec::new();
            for i in 0..q.len() {
                if q[i].borrow().val == target {
                    return if i + 1 < q.len() { Some(q[i + 1].clone()) } else { None };
                }
                let node = q[i].borrow();
                if let Some(l) = node.left.clone() {
                    nxt.push(l);
                }
                if let Some(r) = node.right.clone() {
                    nxt.push(r);
                }
            }
            q = nxt;
        }
        None
    }
}
