// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

impl Solution {
    pub fn max_value(n: String, x: i32) -> String {
        let neg = n.as_bytes()[0] == b'-';
        let start = if neg { 1 } else { 0 };
        let xch = (b'0' + x as u8) as char;
        for i in start..n.len() {
            let d = (n.as_bytes()[i] - b'0') as i32;
            if neg {
                if d > x {
                    return format!("{}{}{}", &n[..i], xch, &n[i..]);
                }
            } else if d < x {
                return format!("{}{}{}", &n[..i], xch, &n[i..]);
            }
        }
        format!("{}{}", n, xch)
    }
}
