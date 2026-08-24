// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

use std::cell::RefCell;
use std::collections::BTreeMap;
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
    pub fn vertical_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut nodes = Vec::new();
        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            row: i32,
            col: i32,
            nodes: &mut Vec<(i32, i32, i32)>,
        ) {
            let Some(n) = node else { return };
            let n = n.borrow();
            nodes.push((col, row, n.val));
            dfs(&n.left, row + 1, col - 1, nodes);
            dfs(&n.right, row + 1, col + 1, nodes);
        }
        dfs(&root, 0, 0, &mut nodes);
        nodes.sort_unstable();
        let mut by_col: BTreeMap<i32, Vec<i32>> = BTreeMap::new();
        for (col, _, val) in nodes {
            by_col.entry(col).or_default().push(val);
        }
        by_col.into_values().collect()
    }
}
