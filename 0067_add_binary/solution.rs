// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let ba = a.as_bytes();
        let bb = b.as_bytes();
        let mut i = ba.len() as i32 - 1;
        let mut j = bb.len() as i32 - 1;
        let mut carry = 0;
        let mut result = Vec::new();

        while i >= 0 || j >= 0 || carry != 0 {
            let mut total = carry;
            if i >= 0 {
                total += (ba[i as usize] - b'0') as i32;
                i -= 1;
            }
            if j >= 0 {
                total += (bb[j as usize] - b'0') as i32;
                j -= 1;
            }
            result.push(b'0' + (total % 2) as u8);
            carry = total / 2;
        }

        result.reverse();
        String::from_utf8(result).unwrap()
    }
}
