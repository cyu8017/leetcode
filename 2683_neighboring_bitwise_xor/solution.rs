// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

impl Solution {
    pub fn does_valid_array_exist(derived: Vec<i32>) -> bool {
        let mut x = 0;
        for v in derived {
            x ^= v;
        }
        x == 0
    }
}
