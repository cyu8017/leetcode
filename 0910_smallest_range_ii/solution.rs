// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

impl Solution {
    pub fn smallest_range_ii(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut ans = nums[nums.len() - 1] - nums[0];
        for i in 0..nums.len() - 1 {
            let lo = (nums[0] + k).min(nums[i + 1] - k);
            let hi = (nums[nums.len() - 1] - k).max(nums[i] + k);
            ans = ans.min(hi - lo);
        }
        ans
    }
}
