// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

impl Solution {
    fn mod_pow_p(mut a: i32, mut e: i32, p: i32) -> i32 {
        let mut r = 1;
        while e > 0 {
            if e & 1 == 1 {
                r = r * a % p;
            }
            a = a * a % p;
            e >>= 1;
        }
        r
    }

    fn mod_inv_prime(a: i32, p: i32) -> i32 {
        Self::mod_pow_p(a, p - 2, p)
    }

    fn binom_mod(n: i32, k: i32, p: i32) -> i32 {
        if k < 0 || k > n {
            return 0;
        }
        let mut num = 1;
        let mut den = 1;
        for i in 0..k {
            num = num * (n - i) % p;
            den = den * (i + 1) % p;
        }
        num * Self::mod_inv_prime(den, p) % p
    }

    fn crt(a1: i32, m1: i32, a2: i32, m2: i32) -> i32 {
        for x in 0..m1 * m2 {
            if x % m1 == a1 && x % m2 == a2 {
                return x;
            }
        }
        0
    }

    fn binom_mod10(n: i32, k: i32) -> i32 {
        Self::crt(Self::binom_mod(n, k, 2), 2, Self::binom_mod(n, k, 5), 5)
    }

    fn combine_digit(s: &[u8], n: i32, offset: usize) -> i32 {
        let mut sum = 0;
        for i in 0..=n - 2 {
            sum = (sum + Self::binom_mod10(n - 2, i) * (s[i as usize + offset] - b'0') as i32) % 10;
        }
        sum
    }

    pub fn has_same_digits(s: String) -> bool {
        let n = s.len() as i32;
        let b = s.as_bytes();
        Self::combine_digit(b, n, 0) == Self::combine_digit(b, n, 1)
    }
}
