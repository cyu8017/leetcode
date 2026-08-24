struct Solution;
// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

impl Solution {
    pub fn average_value(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        let mut cnt = 0;
        for x in nums {
            if x % 6 == 0 {
                sum += x;
                cnt += 1;
            }
        }
        if cnt == 0 {
            0
        } else {
            sum / cnt
        }
    }
}

fn main() {}
