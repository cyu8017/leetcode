// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

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
    pub fn reverse_odd_levels(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(
            a: Option<Rc<RefCell<TreeNode>>>,
            b: Option<Rc<RefCell<TreeNode>>>,
            level: i32,
        ) {
            let (Some(a), Some(b)) = (a, b) else {
                return;
            };
            if level % 2 == 1 {
                let mut aa = a.borrow_mut();
                let mut bb = b.borrow_mut();
                std::mem::swap(&mut aa.val, &mut bb.val);
            }
            let (al, ar) = {
                let n = a.borrow();
                (n.left.clone(), n.right.clone())
            };
            let (bl, br) = {
                let n = b.borrow();
                (n.left.clone(), n.right.clone())
            };
            dfs(al, br, level + 1);
            dfs(ar, bl, level + 1);
        }
        if let Some(r) = &root {
            let (l, ri) = {
                let n = r.borrow();
                (n.left.clone(), n.right.clone())
            };
            dfs(l, ri, 1);
        }
        root
    }
}
