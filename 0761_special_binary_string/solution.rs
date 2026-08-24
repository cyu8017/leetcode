// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

impl Solution {
    pub fn make_largest_special(s: String) -> String {
        let chars: Vec<char> = s.chars().collect();
        let mut parts = Vec::new();
        let mut balance = 0;
        let mut start = 0;
        for i in 0..chars.len() {
            balance += if chars[i] == '1' { 1 } else { -1 };
            if balance == 0 {
                let inner: String = chars[start + 1..i].iter().collect();
                parts.push(format!("1{}0", Self::make_largest_special(inner)));
                start = i + 1;
            }
        }
        parts.sort_by(|a, b| b.cmp(a));
        parts.concat()
    }
}
