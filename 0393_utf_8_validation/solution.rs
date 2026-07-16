// LeetCode 0393 - UTF-8 Validation
// https://leetcode.com/problems/utf-8-validation/

impl Solution {
    pub fn valid_utf8(data: Vec<i32>) -> bool {
        let mut remaining = 0;

        for value in data {
            let byte = value & 0xFF;
            if remaining == 0 {
                if byte >> 7 == 0b0 {
                    continue;
                }
                if byte >> 5 == 0b110 {
                    remaining = 1;
                } else if byte >> 4 == 0b1110 {
                    remaining = 2;
                } else if byte >> 3 == 0b11110 {
                    remaining = 3;
                } else {
                    return false;
                }
            } else if byte >> 6 != 0b10 {
                return false;
            } else {
                remaining -= 1;
            }
        }

        remaining == 0
    }
}
