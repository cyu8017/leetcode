// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

impl Solution {
    pub fn count_palindromes(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let b = s.as_bytes();
        let n = b.len();
        let mut pref = vec![[[0i64; 10]; 10]; n];
        let mut suf = vec![[[0i64; 10]; 10]; n];
        let mut cnt = [0i64; 10];
        for i in 0..n {
            if i > 0 {
                pref[i] = pref[i - 1];
            }
            let d = (b[i] - b'0') as usize;
            for a in 0..10 {
                pref[i][a][d] += cnt[a];
            }
            cnt[d] += 1;
        }
        cnt = [0; 10];
        for i in (0..n).rev() {
            if i + 1 < n {
                suf[i] = suf[i + 1];
            }
            let d = (b[i] - b'0') as usize;
            for a in 0..10 {
                suf[i][a][d] += cnt[a];
            }
            cnt[d] += 1;
        }
        let mut ans = 0i64;
        for i in 2..n.saturating_sub(2) {
            for a in 0..10 {
                for bb in 0..10 {
                    ans = (ans + pref[i - 1][a][bb] * suf[i + 1][a][bb]) % MOD;
                }
            }
        }
        ans as i32
    }
}
