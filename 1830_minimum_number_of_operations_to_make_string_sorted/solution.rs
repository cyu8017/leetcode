// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

impl Solution {
    pub fn make_string_sorted(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();

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

        let mut fact = vec![1i64; n + 1];
        for i in 2..=n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }

        let mut inv_fact = vec![1i64; n + 1];
        inv_fact[n] = pow_mod(fact[n], MOD - 2);
        for i in (0..n).rev() {
            inv_fact[i] = inv_fact[i + 1] * (i as i64 + 1) % MOD;
        }

        let mut freq = [0usize; 26];
        for &ch in bytes {
            freq[(ch - b'a') as usize] += 1;
        }

        let mut ans = 0i64;
        for (i, &ch) in bytes.iter().enumerate() {
            let c = (ch - b'a') as usize;
            for smaller in 0..c {
                if freq[smaller] == 0 {
                    continue;
                }
                freq[smaller] -= 1;
                let mut ways = fact[n - i - 1];
                for &count in &freq {
                    ways = ways * inv_fact[count] % MOD;
                }
                ans = (ans + ways) % MOD;
                freq[smaller] += 1;
            }
            freq[c] -= 1;
        }

        ans as i32
    }
}
