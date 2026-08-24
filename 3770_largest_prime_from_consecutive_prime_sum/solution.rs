// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

impl Solution {
    pub fn largest_prime(n: i32) -> i32 {
        const MX: usize = 500000;
        let mut is_prime = vec![true; MX + 1];
        is_prime[0] = false;
        is_prime[1] = false;
        let mut primes = Vec::new();
        for i in 2..=MX {
            if is_prime[i] {
                primes.push(i as i32);
                if (i as i64) * (i as i64) <= MX as i64 {
                    let mut j = i * i;
                    while j <= MX {
                        is_prime[j] = false;
                        j += i;
                    }
                }
            }
        }
        let mut s = vec![0i32];
        let mut t = 0i32;
        for x in primes {
            t += x;
            if t as usize > MX {
                break;
            }
            if is_prime[t as usize] {
                s.push(t);
            }
        }
        let it = s.partition_point(|&v| v <= n);
        s[it - 1]
    }
}
