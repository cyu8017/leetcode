// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

impl Solution {
    pub fn number_of_substrings(s: String, k: i32) -> i32 {
        let n = s.len();
        let sb = s.as_bytes();
        let mut ans = 0;
        for i in 0..n {
            let mut freq = [0i32; 26];
            for j in i..n {
                freq[(sb[j] - b'a') as usize] += 1;
                let ok = freq.iter().any(|&f| f >= k);
                if ok {
                    ans += (n - j) as i32;
                    break;
                }
            }
        }
        ans
    }
}
