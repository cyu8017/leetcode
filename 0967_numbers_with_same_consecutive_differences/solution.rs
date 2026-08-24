// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

use std::collections::HashSet;

impl Solution {
    pub fn nums_same_consec_diff(n: i32, k: i32) -> Vec<i32> {
        fn dfs(num: i32, length: i32, n: i32, k: i32, ans: &mut Vec<i32>) {
            if length == n {
                ans.push(num);
                return;
            }
            let last = num % 10;
            let nexts: HashSet<i32> = [last + k, last - k].into_iter().collect();
            for nxt in nexts {
                if nxt >= 0 && nxt <= 9 {
                    dfs(num * 10 + nxt, length + 1, n, k, ans);
                }
            }
        }
        let mut ans = Vec::new();
        for start in 1..=9 {
            dfs(start, 1, n, k, &mut ans);
        }
        ans
    }
}
