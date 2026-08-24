// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

impl Solution {
    pub fn minimum_deletions(word: String, k: i32) -> i32 {
        let mut freq = [0i32; 26];
        for c in word.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let nums: Vec<i32> = freq.iter().copied().filter(|&v| v > 0).collect();
        let f = |v: i32| -> i32 {
            let mut ans = 0;
            for &x in &nums {
                if x < v {
                    ans += x;
                } else if x > v + k {
                    ans += x - v - k;
                }
            }
            ans
        };
        let mut ans = word.len() as i32;
        for i in 0..=word.len() as i32 {
            ans = ans.min(f(i));
        }
        ans
    }
}
