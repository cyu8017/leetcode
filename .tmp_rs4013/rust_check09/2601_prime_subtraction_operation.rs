struct Solution;

// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

impl Solution {
    pub fn prime_sub_operation(nums: Vec<i32>) -> bool {
        let max_v = *nums.iter().max().unwrap() as usize;
        let mut is_p = vec![true; max_v + 1];
        if max_v >= 0 {
            is_p[0] = false;
        }
        if max_v >= 1 {
            is_p[1] = false;
        }
        let mut i = 2;
        while i * i <= max_v {
            if is_p[i] {
                let mut j = i * i;
                while j <= max_v {
                    is_p[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let primes: Vec<i32> = (2..=max_v).filter(|&i| is_p[i]).map(|i| i as i32).collect();
        let mut prev = 0;
        for x in nums {
            if x <= prev {
                return false;
            }
            let mut best = x;
            for &p in &primes {
                if p >= x {
                    break;
                }
                if x - p > prev {
                    best = x - p;
                }
            }
            prev = best;
        }
        true
    }
}

fn main() {}
