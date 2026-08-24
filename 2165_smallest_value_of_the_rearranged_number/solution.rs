// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

impl Solution {
    pub fn smallest_number(mut num: i64) -> i64 {
        let neg = num < 0;
        if neg {
            num = -num;
        }
        if num == 0 {
            return 0;
        }
        let mut digits = Vec::new();
        while num > 0 {
            digits.push((b'0' + (num % 10) as u8) as char);
            num /= 10;
        }
        if neg {
            digits.sort_unstable_by(|a, b| b.cmp(a));
            let mut ans = 0i64;
            for d in digits {
                ans = ans * 10 + (d as u8 - b'0') as i64;
            }
            return -ans;
        }
        digits.sort_unstable();
        if digits[0] == '0' {
            for i in 1..digits.len() {
                if digits[i] != '0' {
                    digits.swap(0, i);
                    break;
                }
            }
        }
        let mut ans = 0i64;
        for d in digits {
            ans = ans * 10 + (d as u8 - b'0') as i64;
        }
        ans
    }
}
