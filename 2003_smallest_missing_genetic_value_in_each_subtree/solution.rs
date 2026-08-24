// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

use std::collections::HashSet;

impl Solution {
    pub fn smallest_missing_value_subtree(parents: Vec<i32>, nums: Vec<i32>) -> Vec<i32> {
        let n = parents.len();
        let mut children = vec![Vec::new(); n];
        for i in 1..n {
            children[parents[i] as usize].push(i);
        }
        let mut ans = vec![1; n];
        let one = match nums.iter().position(|&x| x == 1) {
            Some(i) => i,
            None => return ans,
        };
        let mut seen = HashSet::new();
        fn collect(
            u: usize,
            children: &[Vec<usize>],
            nums: &[i32],
            seen: &mut HashSet<i32>,
        ) {
            if seen.contains(&nums[u]) {
                return;
            }
            seen.insert(nums[u]);
            for &v in &children[u] {
                collect(v, children, nums, seen);
            }
        }
        let mut miss = 1;
        let mut node = one as i32;
        let mut prev = -1i32;
        while node != -1 {
            let u = node as usize;
            for &v in &children[u] {
                if v as i32 != prev {
                    collect(v, &children, &nums, &mut seen);
                }
            }
            seen.insert(nums[u]);
            while seen.contains(&miss) {
                miss += 1;
            }
            ans[u] = miss;
            prev = node;
            node = parents[u];
        }
        ans
    }
}
