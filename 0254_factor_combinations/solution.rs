// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

impl Solution {
    pub fn get_factors(n: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn backtrack(remain: i32, start: i32, path: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
            if start > remain {
                if path.len() > 1 {
                    result.push(path.clone());
                }
                return;
            }

            let mut factor = start;
            while factor * factor <= remain {
                if remain % factor == 0 {
                    path.push(factor);
                    backtrack(remain / factor, factor, path, result);
                    path.pop();
                }
                factor += 1;
            }

            if !path.is_empty() {
                path.push(remain);
                if path.len() > 1 {
                    result.push(path.clone());
                }
                path.pop();
            }
        }

        backtrack(n, 2, &mut path, &mut result);
        result
    }
}
