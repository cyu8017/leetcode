// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

impl Solution {
    pub fn count_stable_subsequences(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut a1 = 0;
        let mut a2 = 0;
        let mut b1 = 0;
        let mut b2 = 0;
        for x in nums {
            if x % 2 == 1 {
                let na1 = (1 + b1 + b2) % MOD;
                let na2 = a1;
                a1 = (a1 + na1) % MOD;
                a2 = (a2 + na2) % MOD;
            } else {
                let nb1 = (1 + a1 + a2) % MOD;
                let nb2 = b1;
                b1 = (b1 + nb1) % MOD;
                b2 = (b2 + nb2) % MOD;
            }
        }
        (((a1 + a2) % MOD + b1) % MOD + b2) % MOD
    }
}
