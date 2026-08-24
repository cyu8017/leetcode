struct Solution;
// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        const INF: i64 = i64::MIN / 4;
        let mut f = vec![[INF; 4]; n + 1];
        f[0][0] = 0;
        let mut ans = INF;
        for i in 1..=n {
            let x = nums[i - 1] as i64;
            f[i][0] = f[i - 1][0].max(0) + x;
            f[i][1] = f[i - 1][0].max(f[i - 1][1]).max(0) + x * k as i64;
            f[i][2] = f[i - 1][0].max(f[i - 1][2]).max(0) + x / k as i64;
            f[i][3] = f[i - 1][1].max(f[i - 1][2]).max(f[i - 1][3]) + x;
            ans = ans.max(f[i][0]).max(f[i][1]).max(f[i][2]).max(f[i][3]);
        }
        ans
    }
}

fn main() {}
