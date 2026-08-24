// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut ans = -1;
        let mut mn = nums[0];
        for &x in nums.iter().skip(1) {
            if x > mn {
                ans = ans.max(x - mn);
            } else {
                mn = x;
            }
        }
        ans
    }
}
