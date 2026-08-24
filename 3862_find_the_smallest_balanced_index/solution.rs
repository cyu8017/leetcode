// LeetCode 3862 - Find the Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

impl Solution {
    pub fn smallest_balanced_index(nums: Vec<i32>) -> i32 {
        let mut s: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut p = 1i64;
        for i in (0..nums.len()).rev() {
            s -= nums[i] as i64;
            if s == p {
                return i as i32;
            }
            p *= nums[i] as i64;
            if p >= s {
                break;
            }
        }
        -1
    }
}
