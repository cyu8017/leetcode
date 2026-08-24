// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

impl Solution {
    pub fn max_array_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut cur = nums[n - 1] as i64;
        let mut ans = cur;
        for i in (0..n - 1).rev() {
            if nums[i] as i64 <= cur {
                cur += nums[i] as i64;
            } else {
                cur = nums[i] as i64;
            }
            ans = ans.max(cur);
        }
        ans
    }
}
