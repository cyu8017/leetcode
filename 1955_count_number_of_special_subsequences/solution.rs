// LeetCode 1955 - Count Number of Special Subsequences
// https://leetcode.com/problems/count-number-of-special-subsequences/

impl Solution {
    pub fn count_special_subsequences(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut a: i64 = 0;
        let mut b: i64 = 0;
        let mut c: i64 = 0;
        for x in nums {
            if x == 0 {
                a = (a * 2 + 1) % MOD;
            } else if x == 1 {
                b = (b * 2 + a) % MOD;
            } else {
                c = (c * 2 + b) % MOD;
            }
        }
        c as i32
    }
}
