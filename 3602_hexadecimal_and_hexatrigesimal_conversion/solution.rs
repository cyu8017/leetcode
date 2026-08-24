// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

impl Solution {
    fn f(mut x: i32, k: i32) -> String {
        let mut res = String::new();
        while x > 0 {
            let v = x % k;
            res.push(if v <= 9 {
                (b'0' + v as u8) as char
            } else {
                (b'A' + (v - 10) as u8) as char
            });
            x /= k;
        }
        res.chars().rev().collect()
    }

    pub fn concat_hex36(n: i32) -> String {
        format!("{}{}", Self::f(n * n, 16), Self::f(n * n * n, 36))
    }
}
