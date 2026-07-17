// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

impl Solution {
    pub fn can_choose(groups: Vec<Vec<i32>>, nums: Vec<i32>) -> bool {
        fn dfs(groups: &[Vec<i32>], nums: &[i32], i: usize, start: usize) -> bool {
            let n = nums.len();
            if i == groups.len() {
                return start == n;
            }
            let g = &groups[i];
            let m = g.len();
            if m > n {
                return false;
            }
            for j in start..=(n - m) {
                if nums[j..j + m] == g[..] && dfs(groups, nums, i + 1, j + m) {
                    return true;
                }
            }
            false
        }
        dfs(&groups, &nums, 0, 0)
    }
}
