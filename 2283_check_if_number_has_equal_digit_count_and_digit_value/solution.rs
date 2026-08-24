// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

impl Solution {
    pub fn digit_count(num: String) -> bool {
        let bytes = num.as_bytes();
        let mut cnt = [0i32; 10];
        for &c in bytes {
            cnt[(c - b'0') as usize] += 1;
        }
        for (i, &c) in bytes.iter().enumerate() {
            if cnt[i] != (c - b'0') as i32 {
                return false;
            }
        }
        true
    }
}
