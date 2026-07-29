// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

impl Solution {
    pub fn base_neg2(mut n: i32) -> String {
        if n == 0 {
            return "0".to_string();
        }
        let mut ans = Vec::new();
        while n != 0 {
            let mut rem = n % -2;
            n /= -2;
            if rem < 0 {
                n += 1;
                rem += 2;
            }
            ans.push((b'0' + rem as u8) as char);
        }
        ans.into_iter().rev().collect()
    }
}
