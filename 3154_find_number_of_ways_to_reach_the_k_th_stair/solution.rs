// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

use std::collections::HashMap;

impl Solution {
    pub fn ways_to_reach_stair(k: i32) -> i32 {
        let mut f = HashMap::new();
        fn dfs(i: i64, j: i32, jump: i32, k: i64, f: &mut HashMap<i64, i32>) -> i32 {
            if i > k + 1 {
                return 0;
            }
            let key = (i << 32) | ((jump as i64) << 1) | j as i64;
            if let Some(&v) = f.get(&key) {
                return v;
            }
            let mut ans = 0;
            if i == k {
                ans += 1;
            }
            if i > 0 && j == 0 {
                ans += dfs(i - 1, 1, jump, k, f);
            }
            ans += dfs(i + (1i64 << jump), 0, jump + 1, k, f);
            f.insert(key, ans);
            ans
        }
        dfs(1, 0, 0, k as i64, &mut f)
    }
}
