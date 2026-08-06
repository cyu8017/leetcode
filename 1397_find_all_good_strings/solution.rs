// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

use std::collections::HashMap;

impl Solution {
    pub fn find_good_strings(n: i32, s1: String, s2: String, evil: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = n as usize;
        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let evil = evil.as_bytes();
        let m = evil.len();
        let mut pi = vec![0; m];
        for i in 1..m {
            let mut j = pi[i - 1];
            while j > 0 && evil[i] != evil[j] {
                j = pi[j - 1];
            }
            if evil[i] == evil[j] {
                j += 1;
            }
            pi[i] = j;
        }
        let mut trans = vec![vec![0; 26]; m];
        for j in 0..m {
            for x in 0..26 {
                let c = b'a' + x as u8;
                let mut k = j;
                while k > 0 && evil[k] != c {
                    k = pi[k - 1];
                }
                if evil[k] == c {
                    k += 1;
                }
                trans[j][x] = k;
            }
        }
        let mut memo: HashMap<(usize, usize, bool, bool), i32> = HashMap::new();
        fn dp(
            i: usize,
            j: usize,
            lo: bool,
            hi: bool,
            n: usize,
            m: usize,
            s1: &[u8],
            s2: &[u8],
            trans: &[Vec<usize>],
            memo: &mut HashMap<(usize, usize, bool, bool), i32>,
        ) -> i32 {
            if j == m {
                return 0;
            }
            if i == n {
                return 1;
            }
            if let Some(&v) = memo.get(&(i, j, lo, hi)) {
                return v;
            }
            let a = if lo { (s1[i] - b'a') as usize } else { 0 };
            let b = if hi { (s2[i] - b'a') as usize } else { 25 };
            let mut ans = 0i32;
            for x in a..=b {
                ans = (ans
                    + dp(
                        i + 1,
                        trans[j][x],
                        lo && x == a,
                        hi && x == b,
                        n,
                        m,
                        s1,
                        s2,
                        trans,
                        memo,
                    ))
                    % MOD;
            }
            memo.insert((i, j, lo, hi), ans);
            ans
        }
        dp(0, 0, true, true, n, m, s1, s2, &trans, &mut memo)
    }
}
