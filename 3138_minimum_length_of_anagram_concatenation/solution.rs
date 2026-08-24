// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

impl Solution {
    pub fn min_anagram_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut cnt = [0i32; 26];
        for &c in b {
            cnt[(c - b'a') as usize] += 1;
        }
        let check = |k: usize| -> bool {
            let mut i = 0;
            while i < n {
                let mut cnt1 = [0i32; 26];
                for j in i..i + k {
                    cnt1[(b[j] - b'a') as usize] += 1;
                }
                for j in 0..26 {
                    if cnt1[j] * (n as i32 / k as i32) != cnt[j] {
                        return false;
                    }
                }
                i += k;
            }
            true
        };
        let mut i = 1;
        loop {
            if n % i == 0 && check(i) {
                return i as i32;
            }
            i += 1;
        }
    }
}
