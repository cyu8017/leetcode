// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

impl Solution {
    pub fn gray_code(n: i32) -> Vec<i32> {
        let size = 1 << n;
        let mut result = Vec::with_capacity(size as usize);
        for i in 0..size {
            result.push(i ^ (i >> 1));
        }
        result
    }
}
