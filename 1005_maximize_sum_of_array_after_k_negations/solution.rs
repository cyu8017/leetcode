// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

impl Solution {
    pub fn largest_sum_after_k_negations(mut nums: Vec<i32>, mut k: i32) -> i32 {
        nums.sort_unstable();
        for i in 0..nums.len() {
            if k > 0 && nums[i] < 0 {
                nums[i] = -nums[i];
                k -= 1;
            }
        }
        if k % 2 == 1 {
            nums.sort_unstable();
            nums[0] = -nums[0];
        }
        nums.iter().sum()
    }
}
