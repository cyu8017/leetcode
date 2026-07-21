// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

impl Solution {
    pub fn sum_of_floored_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut count = vec![0i64; max_val + 1];
        for &num in &nums {
            count[num as usize] += 1;
        }
        let mut prefix = vec![0i64; max_val + 1];
        prefix[0] = count[0];
        for value in 1..=max_val {
            prefix[value] = prefix[value - 1] + count[value];
        }
        let mut answer = 0i64;
        for divisor in 1..=max_val {
            if count[divisor] == 0 {
                continue;
            }
            let mut quotient = 1usize;
            while quotient * divisor <= max_val {
                let low = quotient * divisor;
                let high = ((quotient + 1) * divisor - 1).min(max_val);
                let matches = prefix[high] - if low > 0 { prefix[low - 1] } else { 0 };
                answer = (answer + count[divisor] * matches * quotient as i64) % MOD;
                quotient += 1;
            }
        }
        answer as i32
    }
}
