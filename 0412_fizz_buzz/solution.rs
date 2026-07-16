// LeetCode 0412 - Fizz Buzz
// https://leetcode.com/problems/fizz-buzz/

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut result = Vec::with_capacity(n as usize);
        for value in 1..=n {
            let text = if value % 15 == 0 {
                "FizzBuzz".to_string()
            } else if value % 3 == 0 {
                "Fizz".to_string()
            } else if value % 5 == 0 {
                "Buzz".to_string()
            } else {
                value.to_string()
            };
            result.push(text);
        }
        result
    }
}
