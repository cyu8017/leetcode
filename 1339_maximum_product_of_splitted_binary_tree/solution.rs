// LeetCode 1339 - Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

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
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut sums = Vec::new();
        fn total(node: Option<Rc<RefCell<TreeNode>>>, sums: &mut Vec<i64>) -> i64 {
            let Some(node) = node else { return 0 };
            let n = node.borrow();
            let value = n.val as i64 + total(n.left.clone(), sums) + total(n.right.clone(), sums);
            sums.push(value);
            value
        }
        let whole = total(root, &mut sums);
        (sums.iter().map(|&v| v * (whole - v)).max().unwrap_or(0) % 1_000_000_007) as i32
    }
}
