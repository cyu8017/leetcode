// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

impl Solution {
    pub fn reach_number(target: i32) -> i32 {
        let target = target.abs();
        let mut steps = 0;
        let mut total = 0;
        while total < target || (total - target) % 2 != 0 {
            steps += 1;
            total += steps;
        }
        steps
    }
}
