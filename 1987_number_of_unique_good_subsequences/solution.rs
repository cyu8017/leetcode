// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

impl Solution {
    pub fn number_of_unique_good_subsequences(binary: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut ends0 = 0i32;
        let mut ends1 = 0i32;
        let mut has0 = false;
        for ch in binary.bytes() {
            if ch == b'0' {
                has0 = true;
                ends0 = (ends0 + ends1) % MOD;
            } else {
                ends1 = (ends0 + ends1 + 1) % MOD;
            }
        }
        (ends0 + ends1 + if has0 { 1 } else { 0 }) % MOD
    }
}
