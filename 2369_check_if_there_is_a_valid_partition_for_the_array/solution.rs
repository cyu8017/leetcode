// LeetCode 2369 - Check if There is a Valid Partition For The Array
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

impl Solution {
    pub fn valid_partition(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;
        for i in 1..=n {
            if i >= 2 && nums[i - 1] == nums[i - 2] && dp[i - 2] {
                dp[i] = true;
            }
            if i >= 3 && nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3] && dp[i - 3] {
                dp[i] = true;
            }
            if i >= 3 && nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1 && dp[i - 3] {
                dp[i] = true;
            }
        }
        dp[n]
    }
}
