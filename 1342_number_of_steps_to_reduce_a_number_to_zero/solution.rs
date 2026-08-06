// LeetCode 1342 - Number of Steps to Reduce a Number to Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

impl Solution {
    pub fn number_of_steps(mut num: i32) -> i32 {
        let mut steps = 0;
        while num != 0 {
            num = if num % 2 == 0 { num / 2 } else { num - 1 };
            steps += 1;
        }
        steps
    }
}
