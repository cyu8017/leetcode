struct Solution;
// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

impl Solution {
    pub fn min_array_sum(nums: Vec<i32>) -> i64 {
        let mut maximum = 0;
        let mut present = vec![false; 100001];
        for &value in &nums {
            present[value as usize] = true;
            if value > maximum {
                maximum = value;
            }
        }
        let mut best = vec![0; (maximum + 1) as usize];
        for divisor in 1..=maximum {
            if !present[divisor as usize] {
                continue;
            }
            let mut multiple = divisor;
            while multiple <= maximum {
                if best[multiple as usize] == 0 {
                    best[multiple as usize] = divisor;
                }
                multiple += divisor;
            }
        }
        let mut answer = 0i64;
        for &value in &nums {
            answer += best[value as usize] as i64;
        }
        answer
    }
}

fn main() {}
