// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

impl Solution {
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; nums.len()];
        let mut pos = 0;
        let mut neg = 1;
        for x in nums {
            if x > 0 {
                ans[pos] = x;
                pos += 2;
            } else {
                ans[neg] = x;
                neg += 2;
            }
        }
        ans
    }
}
