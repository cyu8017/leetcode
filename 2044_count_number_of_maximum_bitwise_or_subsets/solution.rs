// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

impl Solution {
    pub fn count_max_or_subsets(nums: Vec<i32>) -> i32 {
        let max_or = nums.iter().fold(0, |a, &b| a | b);
        fn dfs(i: usize, cur: i32, nums: &[i32], max_or: i32, ans: &mut i32) {
            if i == nums.len() {
                if cur == max_or {
                    *ans += 1;
                }
                return;
            }
            dfs(i + 1, cur, nums, max_or, ans);
            dfs(i + 1, cur | nums[i], nums, max_or, ans);
        }
        let mut ans = 0;
        dfs(0, 0, &nums, max_or, &mut ans);
        ans
    }
}
