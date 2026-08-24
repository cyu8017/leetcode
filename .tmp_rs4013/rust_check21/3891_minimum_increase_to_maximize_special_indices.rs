struct Solution;
// LeetCode 3891 - Minimum Increase to Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

impl Solution {
    pub fn min_increase(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut f = vec![[-1i64; 2]; n];
        fn dfs(i: usize, j: usize, nums: &[i32], f: &mut [[i64; 2]]) -> i64 {
            if i >= nums.len() - 1 {
                return 0;
            }
            if f[i][j] != -1 {
                return f[i][j];
            }
            let cost = 0.max(nums[i - 1].max(nums[i + 1]) + 1 - nums[i]);
            let mut ans = cost as i64 + dfs(i + 2, j, nums, f);
            if j > 0 {
                ans = ans.min(dfs(i + 1, 0, nums, f));
            }
            f[i][j] = ans;
            ans
        }
        dfs(1, ((n & 1) ^ 1), &nums, &mut f)
    }
}
