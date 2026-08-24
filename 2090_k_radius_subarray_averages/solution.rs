// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

impl Solution {
    pub fn get_averages(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut ans = vec![-1; n];
        if 2 * k + 1 > n {
            return ans;
        }
        let mut sum: i64 = nums[..2 * k + 1].iter().map(|&x| x as i64).sum();
        let len = (2 * k + 1) as i64;
        ans[k] = (sum / len) as i32;
        for i in (k + 1)..(n - k) {
            sum += nums[i + k] as i64 - nums[i - k - 1] as i64;
            ans[i] = (sum / len) as i32;
        }
        ans
    }
}
