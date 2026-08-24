// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

use std::collections::HashSet;

impl Solution {
    fn is_prime(x: i64) -> bool {
        if x < 2 {
            return false;
        }
        let sqrt_x = (x as f64).sqrt() as i64;
        for i in 2..=sqrt_x {
            if x % i == 0 {
                return false;
            }
        }
        true
    }

    pub fn sum_of_largest_primes(s: String) -> i64 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut st = HashSet::new();
        for i in 0..n {
            let mut x = 0i64;
            for j in i..n {
                x = x * 10 + (bytes[j] - b'0') as i64;
                if Self::is_prime(x) {
                    st.insert(x);
                }
            }
        }
        let mut nums: Vec<i64> = st.into_iter().collect();
        nums.sort();
        let mut ans = 0i64;
        let mut taken = 0;
        for i in (0..nums.len()).rev() {
            ans += nums[i];
            taken += 1;
            if taken >= 3 {
                break;
            }
        }
        ans
    }
}
