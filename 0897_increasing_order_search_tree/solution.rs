// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

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
    pub fn increasing_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        fn inorder(
            node: Option<Rc<RefCell<TreeNode>>>,
            tail: &mut Option<Rc<RefCell<TreeNode>>>,
        ) {
            if let Some(rc) = node {
                let right = {
                    let mut n = rc.borrow_mut();
                    inorder(n.left.take(), tail);
                    n.left = None;
                    n.right.take()
                };
                if let Some(cur) = tail {
                    cur.borrow_mut().right = Some(rc.clone());
                }
                *tail = Some(rc);
                inorder(right, tail);
            }
        }
        let dummy = Rc::new(RefCell::new(TreeNode::new(0)));
        let mut tail = Some(dummy.clone());
        inorder(root, &mut tail);
        dummy.borrow_mut().right.take()
    }
}
