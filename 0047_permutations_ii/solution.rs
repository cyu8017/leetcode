// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort_unstable();
        let mut result = Vec::new();
        let mut path = Vec::new();
        let mut used = vec![false; nums.len()];

        fn backtrack(
            nums: &[i32],
            path: &mut Vec<i32>,
            used: &mut [bool],
            result: &mut Vec<Vec<i32>>,
        ) {
            if path.len() == nums.len() {
                result.push(path.clone());
                return;
            }
            for i in 0..nums.len() {
                if used[i] {
                    continue;
                }
                if i > 0 && nums[i] == nums[i - 1] && !used[i - 1] {
                    continue;
                }
                used[i] = true;
                path.push(nums[i]);
                backtrack(nums, path, used, result);
                path.pop();
                used[i] = false;
            }
        }

        backtrack(&nums, &mut path, &mut used, &mut result);
        result
    }
}
