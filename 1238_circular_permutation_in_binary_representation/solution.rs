// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

impl Solution {
    pub fn circular_permutation(n: i32, start: i32) -> Vec<i32> {
        (0..1 << n).map(|i| start ^ i ^ (i >> 1)).collect()
    }
}
