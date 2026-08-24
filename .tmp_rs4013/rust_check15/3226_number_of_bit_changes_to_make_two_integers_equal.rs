struct Solution;
// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

impl Solution {
    pub fn min_changes(n: i32, k: i32) -> i32 {
        if (n & k) != k {
            return -1;
        }
        (n ^ k).count_ones() as i32
    }
}

fn main() {}
