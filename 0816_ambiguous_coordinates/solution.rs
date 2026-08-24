// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

impl Solution {
    pub fn ambiguous_coordinates(s: String) -> Vec<String> {
        let digits = &s[1..s.len() - 1];
        fn candidates(frag: &str) -> Vec<String> {
            let mut options = Vec::new();
            if frag.is_empty()
                || (frag.len() > 1 && frag.starts_with('0') && frag.ends_with('0'))
            {
                return options;
            }
            if frag.starts_with('0') && frag.len() > 1 {
                if !frag.ends_with('0') {
                    options.push(format!("0.{}", &frag[1..]));
                }
                return options;
            }
            options.push(frag.to_string());
            if frag.ends_with('0') {
                return options;
            }
            for i in 1..frag.len() {
                options.push(format!("{}.{}", &frag[..i], &frag[i..]));
            }
            options
        }

        let mut answer = Vec::new();
        for i in 1..digits.len() {
            for left in candidates(&digits[..i]) {
                for right in candidates(&digits[i..]) {
                    answer.push(format!("({left}, {right})"));
                }
            }
        }
        answer
    }
}
