struct Solution;
// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

impl Solution {
    pub fn count_visible_people(n: i32, pos: i32, k: i32) -> i32 {
        const N: usize = 100001;
        const MOD: i64 = 1_000_000_007;
        fn qmi(mut a: i64, mut k: i64, p: i64) -> i64 {
            let mut res = 1;
            while k > 0 {
                if k & 1 == 1 {
                    res = res * a % p;
                }
                k >>= 1;
                a = a * a % p;
            }
            res
        }
        let mut fact = vec![0i64; N];
        let mut inv_fact = vec![0i64; N];
        fact[0] = 1;
        inv_fact[0] = 1;
        for i in 1..N {
            fact[i] = fact[i - 1] * i as i64 % MOD;
            inv_fact[i] = qmi(fact[i], MOD - 2, MOD);
        }
        let comb = |nn: i32, kk: i32| fact[nn as usize] * inv_fact[kk as usize] % MOD * inv_fact[(nn - kk) as usize] % MOD;
        let l = pos;
        let r = n - pos - 1;
        let mut ans = 0i64;
        for a in 0..=k.min(l) {
            let b = k - a;
            if b <= r {
                ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD;
            }
        }
        ans as i32
    }
}
