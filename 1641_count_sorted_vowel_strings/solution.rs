// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

impl Solution {
    pub fn count_vowel_strings(n: i32) -> i32 {
        Self::comb(n + 4, 4)
    }

    fn comb(n: i32, mut r: i32) -> i32 {
        if r > n - r {
            r = n - r;
        }
        let mut res = 1i64;
        for i in 0..r {
            res = res * (n - i) as i64 / (i + 1) as i64;
        }
        res as i32
    }
}
