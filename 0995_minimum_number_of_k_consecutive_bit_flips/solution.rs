// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

impl Solution {
    pub fn min_k_bit_flips(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut flip = vec![0; n];
        let mut ans = 0;
        let mut flipped = 0;
        for i in 0..n {
            if i >= k {
                flipped ^= flip[i - k];
            }
            if nums[i] == flipped {
                if i + k > n {
                    return -1;
                }
                ans += 1;
                flipped ^= 1;
                flip[i] = 1;
            }
        }
        ans
    }
}
