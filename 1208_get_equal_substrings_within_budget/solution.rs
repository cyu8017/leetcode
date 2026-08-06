// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

impl Solution {
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        let s = s.as_bytes();
        let t = t.as_bytes();
        let mut left = 0usize;
        let mut cost = 0;
        let mut answer = 0;
        for right in 0..s.len() {
            cost += (s[right] as i32 - t[right] as i32).abs();
            while cost > max_cost {
                cost -= (s[left] as i32 - t[left] as i32).abs();
                left += 1;
            }
            answer = answer.max(right - left + 1);
        }
        answer as i32
    }
}
