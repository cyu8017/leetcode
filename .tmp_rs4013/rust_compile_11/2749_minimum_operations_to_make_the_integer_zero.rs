struct Solution;
fn main() {}

// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

impl Solution {
    pub fn make_the_integer_zero(num1: i32, num2: i32) -> i32 {
        for k in 1..=60 {
            let rem = num1 as i64 - k as i64 * num2 as i64;
            if rem < k {
                continue;
            }
            if (rem as u64).count_ones() <= k as u32 {
                return k as i32;
            }
        }
        -1
    }
}
