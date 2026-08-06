// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

impl Solution {
    pub fn max_diff(num: i32) -> i32 {
        let s = num.to_string();
        let mut high = s.clone();
        for ch in s.chars() {
            if ch != '9' {
                high = s.replace(ch, "9");
                break;
            }
        }
        let mut low = s.clone();
        let chars: Vec<char> = s.chars().collect();
        if chars[0] != '1' {
            low = s.replace(chars[0], "1");
        } else {
            for &ch in &chars[1..] {
                if ch != '0' && ch != '1' {
                    low = s.replace(ch, "0");
                    break;
                }
            }
        }
        high.parse::<i32>().unwrap() - low.parse::<i32>().unwrap()
    }
}
