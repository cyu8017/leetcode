// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn count_pairs(root: Option<Rc<RefCell<TreeNode>>>, distance: i32) -> i32 {
        let mut answer = 0;
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, distance: i32, answer: &mut i32) -> Vec<i32> {
            let Some(node) = node else {
                return Vec::new();
            };
            let node = node.borrow();
            if node.left.is_none() && node.right.is_none() {
                return vec![1];
            }
            let left = dfs(node.left.clone(), distance, answer);
            let right = dfs(node.right.clone(), distance, answer);
            for &a in &left {
                for &b in &right {
                    if a + b <= distance {
                        *answer += 1;
                    }
                }
            }
            let mut out = Vec::new();
            for depth in left.into_iter().chain(right) {
                if depth + 1 < distance {
                    out.push(depth + 1);
                }
            }
            out
        }
        dfs(root, distance, &mut answer);
        answer
    }
}
