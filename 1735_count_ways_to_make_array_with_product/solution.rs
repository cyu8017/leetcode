// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

impl Solution {
    pub fn ways_to_fill_array(queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;

        fn pow_mod(mut base: i64, mut exp: i64) -> i64 {
            let mut result = 1;
            base %= MOD;
            while exp > 0 {
                if exp & 1 == 1 {
                    result = result * base % MOD;
                }
                base = base * base % MOD;
                exp >>= 1;
            }
            result
        }

        fn comb_mod(a: i64, b: i64) -> i64 {
            let mut num = 1;
            let mut den = 1;
            for i in 1..=b {
                num = num * ((a - b + i) % MOD) % MOD;
                den = den * (i % MOD) % MOD;
            }
            num * pow_mod(den, MOD - 2) % MOD
        }

        let mut ans = Vec::with_capacity(queries.len());
        for query in &queries {
            let n = query[0] as i64;
            let mut value = query[1] as i64;
            let mut ways: i64 = 1;
            let mut d: i64 = 2;
            while d * d <= value {
                if value % d == 0 {
                    let mut exp = 0;
                    while value % d == 0 {
                        value /= d;
                        exp += 1;
                    }
                    ways = ways * comb_mod(n + exp - 1, exp) % MOD;
                }
                d += if d == 2 { 1 } else { 2 };
            }
            if value > 1 {
                ways = ways * (n % MOD) % MOD;
            }
            ans.push(ways as i32);
        }
        ans
    }
}
