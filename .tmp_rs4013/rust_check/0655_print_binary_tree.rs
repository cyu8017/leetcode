struct Solution;
// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

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
    fn height(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(node) = node else {
            return -1;
        };
        let node = node.borrow();
        1 + Self::height(&node.left).max(Self::height(&node.right))
    }

    fn place(
        node: &Option<Rc<RefCell<TreeNode>>>,
        r: usize,
        c: usize,
        h: i32,
        res: &mut Vec<Vec<String>>,
    ) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        res[r][c] = node.val.to_string();
        if r as i32 == h {
            return;
        }
        let offset = 1 << (h - r as i32 - 1);
        Self::place(&node.left, r + 1, c - offset as usize, h, res);
        Self::place(&node.right, r + 1, c + offset as usize, h, res);
    }

    pub fn print_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<String>> {
        let h = Self::height(&root);
        let rows = (h + 1) as usize;
        let cols = (1 << (h + 1)) - 1;
        let mut res = vec![vec![String::new(); cols as usize]; rows];
        Self::place(&root, 0, (cols as usize - 1) / 2, h, &mut res);
        res
    }
}

fn main() {}
