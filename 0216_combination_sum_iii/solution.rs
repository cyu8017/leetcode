// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn backtrack(
            start: i32,
            k: i32,
            remaining: i32,
            path: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            if path.len() as i32 == k {
                if remaining == 0 {
                    result.push(path.clone());
                }
                return;
            }
            if remaining <= 0 || path.len() as i32 >= k {
                return;
            }

            for num in start..=9 {
                if num > remaining {
                    break;
                }
                path.push(num);
                backtrack(num + 1, k, remaining - num, path, result);
                path.pop();
            }
        }

        backtrack(1, k, n, &mut path, &mut result);
        result
    }
}
