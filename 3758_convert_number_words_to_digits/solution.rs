// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

impl Solution {
    pub fn convert_number(s: String) -> String {
        const D: [&str; 10] = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        ];
        let n = s.len();
        let mut ans = String::new();
        let mut i = 0;
        while i < n {
            for j in 0..10 {
                let m = D[j].len();
                if i + m <= n && &s[i..i + m] == D[j] {
                    ans.push(char::from(b'0' + j as u8));
                    i += m - 1;
                    break;
                }
            }
            i += 1;
        }
        ans
    }
}
