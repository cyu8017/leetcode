// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut ans = Vec::with_capacity(nums.len());
        let mut rem = 0;
        for bit in nums {
            rem = (rem * 2 + bit) % 5;
            ans.push(rem == 0);
        }
        ans
    }
}
