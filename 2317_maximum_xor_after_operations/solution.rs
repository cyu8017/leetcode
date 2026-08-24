// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

impl Solution {
    pub fn maximum_xor(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for x in nums {
            ans |= x;
        }
        ans
    }
}
