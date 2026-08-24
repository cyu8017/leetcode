struct Solution;
// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

impl Solution {
    pub fn maximum_total_cost(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        const NEG: i64 = -1_000_000_000_000_000_000;
        let mut memo = vec![[NEG, NEG]; n];
        fn dfs(i: usize, j: usize, nums: &[i32], memo: &mut [[i64; 2]]) -> i64 {
            if i >= nums.len() {
                return 0;
            }
            if memo[i][j] != -1_000_000_000_000_000_000 {
                return memo[i][j];
            }
            let mut res = nums[i] as i64 + dfs(i + 1, 1, nums, memo);
            if j > 0 {
                res = res.max(-(nums[i] as i64) + dfs(i + 1, 0, nums, memo));
            }
            memo[i][j] = res;
            res
        }
        dfs(0, 0, &nums, &mut memo)
    }
}

fn main() {}
