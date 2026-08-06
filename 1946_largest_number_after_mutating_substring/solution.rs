// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

impl Solution {
    pub fn maximum_number(num: String, change: Vec<i32>) -> String {
        let mut chars: Vec<char> = num.chars().collect();
        let mut started = false;
        for ch in chars.iter_mut() {
            let d = ch.to_digit(10).unwrap() as i32;
            let mapped = change[d as usize];
            if mapped > d {
                *ch = char::from_digit(mapped as u32, 10).unwrap();
                started = true;
            } else if mapped < d && started {
                break;
            }
        }
        chars.into_iter().collect()
    }
}
