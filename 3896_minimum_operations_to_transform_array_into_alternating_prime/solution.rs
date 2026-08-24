// LeetCode 3896 - Minimum Operations to Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        const MX: usize = 200000;
        let mut is_prime = vec![true; MX + 1];
        is_prime[0] = false;
        is_prime[1] = false;
        let mut i = 2;
        while i * i <= MX {
            if is_prime[i] {
                let mut j = i * i;
                while j <= MX {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let primes: Vec<i32> = (2..=MX).filter(|&i| is_prime[i]).map(|i| i as i32).collect();
        let mut ans = 0;
        for (i, &x) in nums.iter().enumerate() {
            if i % 2 == 0 {
                let it = primes.partition_point(|&p| p < x);
                ans += primes[it] - x;
            } else if is_prime[x as usize] {
                ans += if x == 2 { 2 } else { 1 };
            }
        }
        ans
    }
}
