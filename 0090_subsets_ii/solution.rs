// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

impl Solution {
    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort_unstable();
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn backtrack(
            nums: &[i32],
            start: usize,
            path: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            result.push(path.clone());
            for i in start..nums.len() {
                if i > start && nums[i] == nums[i - 1] {
                    continue;
                }
                path.push(nums[i]);
                backtrack(nums, i + 1, path, result);
                path.pop();
            }
        }

        backtrack(&nums, 0, &mut path, &mut result);
        result
    }
}
