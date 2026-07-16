// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn backtrack(n: i32, k: i32, start: i32, path: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
            if path.len() == k as usize {
                result.push(path.clone());
                return;
            }

            let remaining = k - path.len() as i32;
            for i in start..=(n - remaining + 1) {
                path.push(i);
                backtrack(n, k, i + 1, path, result);
                path.pop();
            }
        }

        backtrack(n, k, 1, &mut path, &mut result);
        result
    }
}
