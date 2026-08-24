// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

impl Solution {
    pub fn find_closest_number(nums: Vec<i32>) -> i32 {
        let mut ans = nums[0];
        for x in nums {
            if x.abs() < ans.abs() || (x.abs() == ans.abs() && x > ans) {
                ans = x;
            }
        }
        ans
    }
}
