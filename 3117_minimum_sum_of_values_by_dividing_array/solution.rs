// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_value_sum(nums: Vec<i32>, and_values: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = and_values.len();
        const INF: i32 = 1 << 29;
        let mut f = HashMap::new();
        fn dfs(
            nums: &[i32],
            and_values: &[i32],
            n: usize,
            m: usize,
            i: usize,
            j: usize,
            mut a: i32,
            f: &mut HashMap<i64, i32>,
        ) -> i32 {
            if n - i < m - j {
                return 1 << 29;
            }
            if j == m {
                return if i == n { 0 } else { 1 << 29 };
            }
            a &= nums[i];
            if a < and_values[j] {
                return 1 << 29;
            }
            let key = ((i as i64) << 36) | ((j as i64) << 32) | (a as u32 as i64);
            if let Some(&v) = f.get(&key) {
                return v;
            }
            let mut ans = dfs(nums, and_values, n, m, i + 1, j, a, f);
            if a == and_values[j] {
                ans = ans.min(dfs(nums, and_values, n, m, i + 1, j + 1, -1, f) + nums[i]);
            }
            f.insert(key, ans);
            ans
        }
        let ans = dfs(&nums, &and_values, n, m, 0, 0, -1, &mut f);
        if ans < INF { ans } else { -1 }
    }
}
