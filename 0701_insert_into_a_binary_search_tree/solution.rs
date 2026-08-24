// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
    pub fn insert_into_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            None => Some(Rc::new(RefCell::new(TreeNode::new(val)))),
            Some(node) => {
                {
                    let mut n = node.borrow_mut();
                    if val < n.val {
                        n.left = Self::insert_into_bst(n.left.take(), val);
                    } else {
                        n.right = Self::insert_into_bst(n.right.take(), val);
                    }
                }
                Some(node)
            }
        }
    }
}
