struct Solution;
fn main() {}

// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

impl Solution {
    pub fn longest_alternating_subarray(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            if nums[i] % 2 != 0 || nums[i] > threshold {
                continue;
            }
            let mut j = i;
            while j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2 {
                j += 1;
            }
            ans = ans.max((j - i + 1) as i32);
        }
        ans
    }
}
