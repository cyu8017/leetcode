struct Solution;
// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

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
    pub fn closest_nodes(
        root: Option<Rc<RefCell<TreeNode>>>,
        queries: Vec<i32>,
    ) -> Vec<Vec<i32>> {
        let mut vals = Vec::new();
        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, vals: &mut Vec<i32>) {
            if let Some(n) = node {
                let n = n.borrow();
                inorder(&n.left, vals);
                vals.push(n.val);
                inorder(&n.right, vals);
            }
        }
        inorder(&root, &mut vals);
        let mut ans = vec![vec![0; 2]; queries.len()];
        for (i, &q) in queries.iter().enumerate() {
            let j = vals.partition_point(|&x| x < q);
            let mx = if j < vals.len() { vals[j] } else { -1 };
            let mn = if j < vals.len() && vals[j] == q {
                q
            } else if j > 0 {
                vals[j - 1]
            } else {
                -1
            };
            ans[i] = vec![mn, mx];
        }
        ans
    }
}

fn main() {}
