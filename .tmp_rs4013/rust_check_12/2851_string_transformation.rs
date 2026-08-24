struct Solution;
// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

impl Solution {
    pub fn number_of_ways(s: String, t: String, k: i64) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len();
        let ss = format!("{}{}", s, s);
        if !ss[..2 * n - 1].contains(&t) {
            return 0;
        }
        let mut cnt = 0i32;
        for i in 0..n {
            if &ss[i..i + n] == t {
                cnt += 1;
            }
        }
        fn mod_pow(mut a: i64, mut b: i64) -> i64 {
            const MOD: i64 = 1_000_000_007;
            let mut res = 1i64;
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
        let same = s == t;
        let pk = mod_pow((n as i64 - 1).rem_euclid(MOD), k);
        let invn = mod_pow(n as i64, MOD - 2);
        let sign = if k % 2 == 1 { MOD - 1 } else { 1 };
        let ways_same = ((pk + ((n as i64 - 1) % MOD) * sign % MOD) % MOD * invn % MOD) as i32;
        let ways_diff = ((pk - sign + MOD) % MOD * invn % MOD) as i32;
        if same {
            ways_same
        } else {
            (ways_diff as i64 * cnt as i64 % MOD) as i32
        }
    }
}

fn main() {}
