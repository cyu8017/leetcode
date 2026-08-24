// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut f = vec![0; n];
        fn dfs(i: usize, nums: &[i32], f: &mut [i32]) -> i32 {
            if f[i] > 0 {
                return f[i];
            }
            for j in i + 1..nums.len() {
                f[i] = f[i].max((j - i) as i32 * nums[j] + dfs(j, nums, f));
            }
            f[i]
        }
        dfs(0, &nums, &mut f)
    }
}
