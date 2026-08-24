// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

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
    pub fn is_cousins(root: Option<Rc<RefCell<TreeNode>>>, x: i32, y: i32) -> bool {
        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            parent_val: Option<i32>,
            depth: i32,
            x: i32,
            y: i32,
            info: &mut [(i32, Option<i32>); 2],
        ) {
            let Some(n) = node else { return };
            let n = n.borrow();
            if n.val == x {
                info[0] = (depth, parent_val);
            }
            if n.val == y {
                info[1] = (depth, parent_val);
            }
            dfs(&n.left, Some(n.val), depth + 1, x, y, info);
            dfs(&n.right, Some(n.val), depth + 1, x, y, info);
        }
        let mut info = [(0, None), (0, None)];
        dfs(&root, None, 0, x, y, &mut info);
        info[0].0 == info[1].0 && info[0].1 != info[1].1
    }
}
