// LeetCode 1356 - Sort Integers by The Number of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

impl Solution {
    pub fn sort_by_bits(mut arr: Vec<i32>) -> Vec<i32> {
        arr.sort_by_key(|&x| (x.count_ones(), x));
        arr
    }
}
