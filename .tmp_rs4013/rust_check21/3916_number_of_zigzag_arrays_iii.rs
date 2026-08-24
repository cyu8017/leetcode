struct Solution;
// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

impl Solution {
    pub fn zig_zag_arrays(n: i32, l: i32, r: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let points = n + 1;
        let mut values = vec![0i64; points + 1];
        for m in 1..=points {
            let mut up: Vec<i64> = (0..m).map(|v| v as i64).collect();
            let mut down: Vec<i64> = (0..m).map(|v| (m - 1 - v) as i64).collect();
            for _length in 3..=n {
                let mut next_up = vec![0i64; m];
                let mut next_down = vec![0i64; m];
                let mut prefix = 0i64;
                for value in 0..m {
                    next_up[value] = prefix;
                    prefix = (prefix + down[value]) % MOD;
                }
                let mut suffix = 0i64;
                for value in (0..m).rev() {
                    next_down[value] = suffix;
                    suffix = (suffix + up[value]) % MOD;
                }
                up = next_up;
                down = next_down;
            }
            for value in 0..m {
                values[m] = (values[m] + up[value] + down[value]) % MOD;
            }
        }
        let x = (r as i64 - l as i64 + 1).rem_euclid(MOD);
        if r - l + 1 <= points as i32 {
            return values[(r - l + 1) as usize] as i32;
        }
        let mut prefix = vec![0i64; points + 2];
        let mut suffix = vec![0i64; points + 2];
        prefix[0] = 1;
        for i in 1..=points {
            prefix[i] = prefix[i - 1] * ((x - i as i64 + MOD) % MOD) % MOD;
        }
        suffix[points + 1] = 1;
        for i in (1..=points).rev() {
            suffix[i] = suffix[i + 1] * ((x - i as i64 + MOD) % MOD) % MOD;
        }
        let mut factorial = vec![0i64; points + 1];
        factorial[0] = 1;
        for i in 1..=points {
            factorial[i] = factorial[i - 1] * i as i64 % MOD;
        }
        fn powm(mut a: i64, mut e: i64, m: i64) -> i64 {
            let mut res = 1;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % m;
                }
                a = a * a % m;
                e >>= 1;
            }
            res
        }
        let mut answer = 0i64;
        for i in 1..=points {
            let numerator = prefix[i - 1] * suffix[i + 1] % MOD;
            let denominator = factorial[i - 1] * factorial[points - i] % MOD;
            let term = values[i] * numerator % MOD * powm(denominator, MOD - 2, MOD) % MOD;
            if (points - i) % 2 == 1 {
                answer -= term;
            } else {
                answer += term;
            }
            answer %= MOD;
        }
        if answer < 0 {
            answer += MOD;
        }
        answer as i32
    }
}
