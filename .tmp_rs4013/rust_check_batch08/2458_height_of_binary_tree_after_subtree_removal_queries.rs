struct Solution;
// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

use std::collections::HashMap;
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
    pub fn tree_queries(
        root: Option<Rc<RefCell<TreeNode>>>,
        queries: Vec<i32>,
    ) -> Vec<i32> {
        let mut height: HashMap<i32, i32> = HashMap::new();
        let mut level: HashMap<i32, i32> = HashMap::new();
        let mut level_max: HashMap<i32, Vec<i32>> = HashMap::new();
        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            d: i32,
            height: &mut HashMap<i32, i32>,
            level: &mut HashMap<i32, i32>,
            level_max: &mut HashMap<i32, Vec<i32>>,
        ) -> i32 {
            let Some(n) = node else {
                return -1;
            };
            let n = n.borrow();
            level.insert(n.val, d);
            let h = 1
                + dfs(&n.left, d + 1, height, level, level_max)
                    .max(dfs(&n.right, d + 1, height, level, level_max));
            height.insert(n.val, h);
            let arr = level_max.entry(d).or_default();
            if arr.is_empty() {
                *arr = vec![h];
            } else if h >= arr[0] {
                *arr = vec![h, arr[0]];
            } else if arr.len() == 1 || h > arr[1] {
                *arr = vec![arr[0], h];
            }
            h
        }
        dfs(&root, 0, &mut height, &mut level, &mut level_max);
        let mut ans = vec![0; queries.len()];
        for (i, &q) in queries.iter().enumerate() {
            let d = level[&q];
            let h = height[&q];
            let top = &level_max[&d];
            if top[0] == h {
                if top.len() > 1 {
                    ans[i] = d + top[1];
                } else {
                    ans[i] = d - 1;
                }
            } else {
                ans[i] = d + top[0];
            }
        }
        ans
    }
}

fn main() {}
