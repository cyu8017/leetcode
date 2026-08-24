struct Solution;
fn main() {}

// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

impl Solution {
    pub fn longest_string(x: i32, y: i32, z: i32) -> i32 {
        if x < y {
            (2 * x + 1 + z) * 2
        } else if y < x {
            (2 * y + 1 + z) * 2
        } else {
            (x + y + z) * 2
        }
    }
}
