struct Solution;
// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

use std::collections::HashMap;

impl Solution {
    fn dfs(tree: &HashMap<(i32, i32), i32>, depth: i32, pos: i32, path: i32, total: &mut i32) {
        if !tree.contains_key(&(depth, pos)) {
            return;
        }
        let path = path + tree[&(depth, pos)];
        let left = (depth + 1, pos * 2 - 1);
        let right = (depth + 1, pos * 2);
        if !tree.contains_key(&left) && !tree.contains_key(&right) {
            *total += path;
            return;
        }
        Self::dfs(tree, depth + 1, pos * 2 - 1, path, total);
        Self::dfs(tree, depth + 1, pos * 2, path, total);
    }

    pub fn path_sum(nums: Vec<i32>) -> i32 {
        let mut tree = HashMap::new();
        for num in nums {
            tree.insert((num / 100, (num / 10) % 10), num % 10);
        }
        let mut total = 0;
        Self::dfs(&tree, 1, 1, 0, &mut total);
        total
    }
}

fn main() {}
