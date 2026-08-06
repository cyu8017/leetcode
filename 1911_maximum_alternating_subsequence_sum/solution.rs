// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

impl Solution {
    pub fn max_alternating_sum(nums: Vec<i32>) -> i64 {
        let mut even: i64 = 0;
        let mut odd: i64 = 0;
        for x in nums {
            let x = x as i64;
            let new_even = even.max(odd + x);
            let new_odd = odd.max(even - x);
            even = new_even;
            odd = new_odd;
        }
        even
    }
}
