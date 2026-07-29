// LeetCode 1015 - Smallest Integer Divisible by K
// https://leetcode.com/problems/smallest-integer-divisible-by-k/

impl Solution {
    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {
        if k % 2 == 0 || k % 5 == 0 {
            return -1;
        }
        let mut rem = 0;
        for length in 1..=k {
            rem = (rem * 10 + 1) % k;
            if rem == 0 {
                return length;
            }
        }
        -1
    }
}
