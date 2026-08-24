struct Solution;
// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

impl Solution {
    pub fn count_valid_subarrays(nums: Vec<i32>, x: i32) -> i64 {
        let mut by_remainder = vec![Vec::new(); 10];
        by_remainder[0].push(0i64);
        let mut prefix = 0i64;
        let mut answer = 0i64;
        for &value in &nums {
            prefix += value as i64;
            let required = ((prefix - x as i64) % 10 + 10) % 10;
            let values = &by_remainder[required as usize];
            let mut power = 1i64;
            while x as i64 * power <= prefix {
                let low = x as i64 * power;
                let high = (x as i64 + 1) * power - 1;
                let min_prefix = prefix - high;
                let max_prefix = prefix - low;
                let left = values.partition_point(|&v| v < min_prefix);
                let right = values.partition_point(|&v| v <= max_prefix);
                answer += (right - left) as i64;
                if power > prefix / 10 {
                    break;
                }
                power *= 10;
            }
            by_remainder[(prefix % 10) as usize].push(prefix);
        }
        answer
    }
}

fn main() {}
