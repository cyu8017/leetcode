// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

impl Solution {
    pub fn num_ways(words: Vec<String>, target: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = words[0].len();
        let target = target.as_bytes();
        let mut dp = vec![0i64; target.len() + 1];
        dp[0] = 1;
        for j in 0..m {
            let mut count = [0i64; 26];
            for word in &words {
                count[(word.as_bytes()[j] - b'a') as usize] += 1;
            }
            let lim = (j + 1).min(target.len());
            for i in (1..=lim).rev() {
                dp[i] = (dp[i] + dp[i - 1] * count[(target[i - 1] - b'a') as usize]) % MOD;
            }
        }
        dp[target.len()] as i32
    }
}
