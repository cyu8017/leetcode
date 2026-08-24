// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

impl Solution {
    pub fn factorial_generator(n: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut cur = 1;
        for i in 1..=n {
            cur *= i;
            ans.push(cur);
        }
        ans
    }
}
