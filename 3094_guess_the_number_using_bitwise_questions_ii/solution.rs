// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

fn common_bits(num: i32) -> i32 {
    let _ = num;
    0
}

impl Solution {
    pub fn find_number() -> i32 {
        let mut n = 0i32;
        for i in 0..32 {
            let bit = 1i32.wrapping_shl(i);
            let count1 = common_bits(bit);
            let count2 = common_bits(bit);
            if count1 > count2 {
                n |= bit;
            }
        }
        n
    }
}
