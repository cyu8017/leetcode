// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

impl Solution {
    pub fn get_xor_sum(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let xor1 = arr1.into_iter().fold(0, |a, b| a ^ b);
        let xor2 = arr2.into_iter().fold(0, |a, b| a ^ b);
        xor1 & xor2
    }
}
