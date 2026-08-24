// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

impl Solution {
    fn primes() -> Vec<i32> {
        let mut primes = Vec::new();
        let mut x = 2;
        while primes.len() < 1000 {
            let mut is_prime = true;
            for &p in &primes {
                if p * p > x {
                    break;
                }
                if x % p == 0 {
                    is_prime = false;
                    break;
                }
            }
            if is_prime {
                primes.push(x);
            }
            x += 1;
        }
        primes
    }

    pub fn min_number_of_primes(n: i32, m: i32) -> i32 {
        let primes = Self::primes();
        let n = n as usize;
        let inf = i32::MAX / 2;
        let mut f = vec![inf; n + 1];
        f[0] = 0;
        for pi in 0..m as usize {
            let x = primes[pi] as usize;
            for i in x..=n {
                if f[i - x] + 1 < f[i] {
                    f[i] = f[i - x] + 1;
                }
            }
        }
        if f[n] < inf {
            f[n]
        } else {
            -1
        }
    }
}
