// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

impl Solution {
    pub fn block_count(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut ans = 1;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                ans += 1;
            }
        }
        ans
    }
}
