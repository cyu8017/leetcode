// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

use std::collections::HashMap;

impl Solution {
    pub fn sum_of_powers(mut nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        nums.sort_unstable();
        let n = nums.len();
        let mut f = HashMap::new();
        fn dfs(
            nums: &[i32],
            n: usize,
            i: usize,
            j: usize,
            kk: i32,
            mi: i32,
            f: &mut HashMap<i64, i32>,
        ) -> i32 {
            if i >= n {
                return if kk == 0 { mi } else { 0 };
            }
            if (n - i) as i32 < kk {
                return 0;
            }
            let key = ((mi as i64) << 18) | ((i as i64) << 12) | ((j as i64) << 6) | kk as i64;
            if let Some(&v) = f.get(&key) {
                return v;
            }
            let mut ans = dfs(nums, n, i + 1, j, kk, mi, f);
            if j == n {
                ans = (ans + dfs(nums, n, i + 1, i, kk - 1, mi, f)) % MOD;
            } else {
                ans = (ans + dfs(nums, n, i + 1, i, kk - 1, mi.min(nums[i] - nums[j]), f)) % MOD;
            }
            f.insert(key, ans);
            ans
        }
        dfs(&nums, n, 0, n, k, i32::MAX, &mut f)
    }
}
