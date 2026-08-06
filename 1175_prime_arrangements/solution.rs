// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

impl Solution {
    pub fn num_prime_arrangements(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn is_prime(x: i32) -> bool {
            if x < 2 {
                return false;
            }
            let mut d = 2;
            while d * d <= x {
                if x % d == 0 {
                    return false;
                }
                d += 1;
            }
            true
        }
        let primes = (1..=n).filter(|&i| is_prime(i)).count() as i64;
        fn fact(x: i64) -> i64 {
            let mut res = 1i64;
            for i in 2..=x {
                res = res * i % MOD;
            }
            res
        }
        (fact(primes) * fact(n as i64 - primes) % MOD) as i32
    }
}
