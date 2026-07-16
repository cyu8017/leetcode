// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn backtrack(
            candidates: &[i32],
            target: i32,
            start: usize,
            path: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            if target == 0 {
                result.push(path.clone());
                return;
            }
            if target < 0 {
                return;
            }

            for i in start..candidates.len() {
                path.push(candidates[i]);
                backtrack(candidates, target - candidates[i], i, path, result);
                path.pop();
            }
        }

        backtrack(&candidates, target, 0, &mut path, &mut result);
        result
    }
}
