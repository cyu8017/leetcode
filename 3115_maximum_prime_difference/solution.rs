// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

impl Solution {
    fn is_prime(n: i32) -> bool {
        if n < 2 {
            return false;
        }
        let mut i = 2;
        while i <= n / i {
            if n % i == 0 {
                return false;
            }
            i += 1;
        }
        true
    }

    pub fn maximum_prime_difference(nums: Vec<i32>) -> i32 {
        let mut i = 0;
        loop {
            if Self::is_prime(nums[i]) {
                let mut j = nums.len() - 1;
                loop {
                    if Self::is_prime(nums[j]) {
                        return (j - i) as i32;
                    }
                    j -= 1;
                }
            }
            i += 1;
        }
    }
}
