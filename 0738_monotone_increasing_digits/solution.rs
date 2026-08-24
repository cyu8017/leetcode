// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

impl Solution {
    pub fn monotone_increasing_digits(n: i32) -> i32 {
        let mut digits: Vec<u8> = n.to_string().into_bytes();
        let mut mark = digits.len();
        for i in (1..digits.len()).rev() {
            if digits[i] < digits[i - 1] {
                digits[i - 1] -= 1;
                mark = i;
            }
        }
        for d in digits.iter_mut().skip(mark) {
            *d = b'9';
        }
        String::from_utf8(digits).unwrap().parse().unwrap()
    }
}
