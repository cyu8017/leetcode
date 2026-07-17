// LeetCode 1796 - Second Largest Digit in a String
// https://leetcode.com/problems/second-largest-digit-in-a-string/

impl Solution {
    pub fn second_highest(s: String) -> i32 {
        let mut largest = -1;
        let mut second = -1;
        for ch in s.chars() {
            if let Some(d) = ch.to_digit(10) {
                let d = d as i32;
                if d > largest {
                    second = largest;
                    largest = d;
                } else if d < largest && d > second {
                    second = d;
                }
            }
        }
        second
    }
}
