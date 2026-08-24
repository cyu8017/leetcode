// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

impl Solution {
    pub fn max_k_distinct(mut nums: Vec<i32>, mut k: i32) -> Vec<i32> {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = Vec::new();
        for i in (0..n).rev() {
            if i + 1 < n && nums[i] == nums[i + 1] {
                continue;
            }
            ans.push(nums[i]);
            k -= 1;
            if k == 0 {
                break;
            }
        }
        ans
    }
}
