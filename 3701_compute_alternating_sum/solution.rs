// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

impl Solution {
    pub fn alternating_sum(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for (i, &x) in nums.iter().enumerate() {
            if i % 2 == 0 {
                ans += x;
            } else {
                ans -= x;
            }
        }
        ans
    }
}
