// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 2 {
            return n as i32;
        }
        let mut x = n as u32;
        let mut len = 0;
        while x > 0 {
            len += 1;
            x >>= 1;
        }
        1 << len
    }
}
