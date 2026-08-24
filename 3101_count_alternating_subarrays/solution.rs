// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

impl Solution {
    pub fn count_alternating_subarrays(nums: Vec<i32>) -> i64 {
        let mut ans = 1i64;
        let mut s = 1i64;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                s += 1;
            } else {
                s = 1;
            }
            ans += s;
        }
        ans
    }
}
