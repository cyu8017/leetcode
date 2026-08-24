// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

fn common_set_bits(num: i32) -> i32 {
    let _ = num;
    0
}

impl Solution {
    pub fn find_number() -> i32 {
        let mut n = 0i32;
        for i in 0..32 {
            let bit = 1i32.wrapping_shl(i);
            if common_set_bits(bit) > 0 {
                n |= bit;
            }
        }
        n
    }
}
