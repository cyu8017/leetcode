struct Solution;
// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

impl Solution {
    pub fn minimize_xor(num1: i32, num2: i32) -> i32 {
        let mut bits = num2.count_ones() as i32;
        let mut ans = 0;
        for i in (0..32).rev() {
            if bits <= 0 {
                break;
            }
            if (num1 >> i) & 1 == 1 {
                ans |= 1 << i;
                bits -= 1;
            }
        }
        for i in 0..32 {
            if bits <= 0 {
                break;
            }
            if (ans >> i) & 1 == 0 {
                ans |= 1 << i;
                bits -= 1;
            }
        }
        ans
    }
}

fn main() {}
