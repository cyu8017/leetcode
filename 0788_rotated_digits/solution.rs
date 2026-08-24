// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

impl Solution {
    pub fn rotated_digits(n: i32) -> i32 {
        let mut count = 0;
        for num in 1..=n {
            let s = num.to_string();
            let mut ok = true;
            let mut changed = false;
            for ch in s.chars() {
                if ch == '3' || ch == '4' || ch == '7' {
                    ok = false;
                    break;
                }
                if ch == '2' || ch == '5' || ch == '6' || ch == '9' {
                    changed = true;
                }
            }
            if ok && changed {
                count += 1;
            }
        }
        count
    }
}
