// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        nums.sort_unstable();
        nums.dedup();
        let mut ans = n;
        let mut j = 0;
        for i in 0..nums.len() {
            while j < nums.len() && nums[j] - nums[i] + 1 <= n {
                j += 1;
            }
            ans = ans.min(n - (j - i) as i32);
        }
        ans
    }
}
