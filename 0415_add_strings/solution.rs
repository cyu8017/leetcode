// LeetCode 0415 - Add Strings
// https://leetcode.com/problems/add-strings/

impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let chars1: Vec<u8> = num1.bytes().collect();
        let chars2: Vec<u8> = num2.bytes().collect();
        let mut index1 = chars1.len() as i32 - 1;
        let mut index2 = chars2.len() as i32 - 1;
        let mut carry = 0;
        let mut digits = Vec::new();

        while index1 >= 0 || index2 >= 0 || carry > 0 {
            if index1 >= 0 {
                carry += (chars1[index1 as usize] - b'0') as i32;
                index1 -= 1;
            }
            if index2 >= 0 {
                carry += (chars2[index2 as usize] - b'0') as i32;
                index2 -= 1;
            }
            digits.push((b'0' + (carry % 10) as u8) as char);
            carry /= 10;
        }

        digits.iter().rev().collect()
    }
}
