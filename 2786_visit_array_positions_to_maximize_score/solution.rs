// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

impl Solution {
    pub fn max_score(nums: Vec<i32>, x: i32) -> i64 {
        let neg = -(1i64 << 60);
        let mut even = nums[0] as i64;
        let mut odd = nums[0] as i64;
        if nums[0] % 2 == 0 {
            odd = neg;
        } else {
            even = neg;
        }
        for i in 1..nums.len() {
            let v = nums[i] as i64;
            if nums[i] % 2 == 0 {
                even = (even + v).max(odd + v - x as i64);
            } else {
                odd = (odd + v).max(even + v - x as i64);
            }
        }
        even.max(odd)
    }
}
