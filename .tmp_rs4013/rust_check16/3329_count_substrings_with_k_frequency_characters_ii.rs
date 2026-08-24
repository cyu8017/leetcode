struct Solution;
// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

impl Solution {
    pub fn number_of_substrings(s: String, k: i32) -> i64 {
        let n = s.len();
        let sb = s.as_bytes();
        let mut ans = 0i64;
        for i in 0..n {
            let mut freq = [0i32; 26];
            for j in i..n {
                freq[(sb[j] - b'a') as usize] += 1;
                let ok = freq.iter().any(|&f| f >= k);
                if ok {
                    ans += (n - j) as i64;
                    break;
                }
            }
        }
        ans
    }
}

fn main() {}
