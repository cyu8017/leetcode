// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

impl Solution {
    pub fn reverse_subarrays(mut nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let m = n / k as usize;
        let mut i = 0;
        while i < n {
            nums[i..i + m].reverse();
            i += m;
        }
        nums
    }
}
