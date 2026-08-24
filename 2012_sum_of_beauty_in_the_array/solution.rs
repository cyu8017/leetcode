// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

impl Solution {
    pub fn sum_of_beauties(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut prefix_max = vec![0; n];
        let mut suffix_min = vec![0; n];
        prefix_max[0] = nums[0];
        for i in 1..n {
            prefix_max[i] = prefix_max[i - 1].max(nums[i]);
        }
        suffix_min[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            suffix_min[i] = suffix_min[i + 1].min(nums[i]);
        }
        let mut ans = 0;
        for i in 1..n - 1 {
            if prefix_max[i - 1] < nums[i] && nums[i] < suffix_min[i + 1] {
                ans += 2;
            } else if nums[i - 1] < nums[i] && nums[i] < nums[i + 1] {
                ans += 1;
            }
        }
        ans
    }
}
