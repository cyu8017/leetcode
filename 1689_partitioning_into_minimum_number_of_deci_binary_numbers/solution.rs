// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        (n.bytes().max().unwrap() - b'0') as i32
    }
}
