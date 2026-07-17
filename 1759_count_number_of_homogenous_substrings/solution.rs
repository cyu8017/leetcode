// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

impl Solution {
    pub fn count_homogenous(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans: i64 = 0;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && bytes[j] == bytes[i] {
                j += 1;
            }
            let length = (j - i) as i64;
            ans = (ans + length * (length + 1) / 2) % MOD;
            i = j;
        }
        ans as i32
    }
}
