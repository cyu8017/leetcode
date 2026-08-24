struct Solution;
// LeetCode 3918 - Sum of Primes Between Number and Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

impl Solution {
    pub fn sum_of_primes_in_range(n: i32) -> i32 {
        let mut is_prime = [true; 1001];
        is_prime[0] = false;
        is_prime[1] = false;
        let mut i = 2;
        while i * i <= 1000 {
            if is_prime[i] {
                let mut j = i * i;
                while j <= 1000 {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let mut r = 0;
        let mut x = n;
        while x > 0 {
            r = r * 10 + x % 10;
            x /= 10;
        }
        let low = n.min(r);
        let high = n.max(r);
        let mut ans = 0;
        for x in low..=high {
            if is_prime[x as usize] {
                ans += x;
            }
        }
        ans
    }
}
