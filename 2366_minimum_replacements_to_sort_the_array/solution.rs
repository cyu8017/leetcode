// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

impl Solution {
    pub fn minimum_replacement(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let n = nums.len();
        let mut prev = nums[n - 1];
        for i in (0..n - 1).rev() {
            if nums[i] <= prev {
                prev = nums[i];
                continue;
            }
            let parts = (nums[i] + prev - 1) / prev;
            ans += parts as i64 - 1;
            prev = nums[i] / parts;
        }
        ans
    }
}
