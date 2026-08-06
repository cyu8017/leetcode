// LeetCode 1404 - Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

impl Solution {
    pub fn num_steps(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut steps = 0;
        let mut carry = 0;
        for &bit in bytes[1..].iter().rev() {
            let value = (bit - b'0') as i32 + carry;
            if value == 1 {
                steps += 2;
                carry = 1;
            } else {
                steps += 1;
            }
        }
        steps + carry
    }
}
