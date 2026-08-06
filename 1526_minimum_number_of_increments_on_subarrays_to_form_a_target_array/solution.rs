// LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

impl Solution {
    pub fn min_number_operations(target: Vec<i32>) -> i32 {
        let mut ans = target[0];
        for i in 1..target.len() {
            if target[i] > target[i - 1] {
                ans += target[i] - target[i - 1];
            }
        }
        ans
    }
}
