// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

impl Solution {
    pub fn subarrays_with_xor_at_least_k(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            let mut x = 0;
            for j in i..n {
                x ^= nums[j];
                if x >= k {
                    ans += 1;
                }
            }
        }
        ans
    }
}
