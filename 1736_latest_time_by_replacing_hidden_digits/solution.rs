// LeetCode 1736 - Latest Time by Replacing Hidden Digits
// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

impl Solution {
    pub fn maximum_time(time: String) -> String {
        let mut chars: Vec<char> = time.chars().collect();
        if chars[0] == '?' {
            chars[0] = if "0123?".contains(chars[1]) { '2' } else { '1' };
        }
        if chars[1] == '?' {
            chars[1] = if chars[0] == '2' { '3' } else { '9' };
        }
        if chars[3] == '?' {
            chars[3] = '5';
        }
        if chars[4] == '?' {
            chars[4] = '9';
        }
        chars.into_iter().collect()
    }
}
