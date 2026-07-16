// LeetCode 0386 - Lexicographical Numbers
// https://leetcode.com/problems/lexicographical-numbers/

impl Solution {
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let mut result = Vec::new();

        fn dfs(current: i32, n: i32, result: &mut Vec<i32>) {
            if current > n {
                return;
            }
            result.push(current);
            dfs(current * 10, n, result);
            if current % 10 < 9 {
                dfs(current + 1, n, result);
            }
        }

        dfs(1, n, &mut result);
        result
    }
}
