// LeetCode 1304 - Find N Unique Integers Sum up to Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

impl Solution {
    pub fn sum_zero(n: i32) -> Vec<i32> {
        let mut answer = Vec::new();
        for value in 1..=n / 2 {
            answer.push(-value);
            answer.push(value);
        }
        if n % 2 != 0 {
            answer.push(0);
        }
        answer
    }
}
