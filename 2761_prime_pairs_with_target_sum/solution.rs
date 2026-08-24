// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

impl Solution {
    pub fn find_prime_pairs(n: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut is_prime = vec![false; n + 1];
        for i in 2..=n {
            is_prime[i] = true;
        }
        let mut i = 2;
        while i * i <= n {
            if is_prime[i] {
                let mut j = i * i;
                while j <= n {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let mut ans = Vec::new();
        for x in 2..=n / 2 {
            let y = n - x;
            if is_prime[x] && is_prime[y] {
                ans.push(vec![x as i32, y as i32]);
            }
        }
        ans
    }
}
