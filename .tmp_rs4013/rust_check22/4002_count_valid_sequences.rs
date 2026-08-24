struct Solution;
// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

use std::sync::OnceLock;

const MX: usize = 500001;
const MOD: i64 = 1_000_000_007;

fn mod_pow(mut a: i64, mut b: i64) -> i64 {
    let mut res = 1;
    a %= MOD;
    while b > 0 {
        if b & 1 == 1 {
            res = res * a % MOD;
        }
        a = a * a % MOD;
        b >>= 1;
    }
    res
}

fn tables() -> &'static (Vec<i64>, Vec<i64>) {
    static TABLES: OnceLock<(Vec<i64>, Vec<i64>)> = OnceLock::new();
    TABLES.get_or_init(|| {
        let mut f = vec![0i64; MX];
        let mut g = vec![0i64; MX];
        f[0] = 1;
        g[0] = 1;
        for i in 1..MX {
            f[i] = f[i - 1] * i as i64 % MOD;
            g[i] = mod_pow(f[i], MOD - 2);
        }
        (f, g)
    })
}

fn comb(n: i32, k: i32) -> i64 {
    if k < 0 || k > n {
        return 0;
    }
    let (f, g) = tables();
    f[n as usize] * g[k as usize] % MOD * g[(n - k) as usize] % MOD
}

impl Solution {
    pub fn count_valid_sequences(n: i32, k: i32) -> i32 {
        let mut ans = comb(n - 1, k - 1);
        if (n + k) % 2 == 0 {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD;
        }
        ans as i32
    }
}

fn main() {}
