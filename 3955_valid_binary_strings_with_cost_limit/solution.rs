// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

impl Solution {
    pub fn generate_valid_strings(n: i32, k: i32) -> Vec<String> {
        let mut ans = Vec::new();
        let mut path = String::new();
        fn dfs(i: i32, tot: i32, n: i32, k: i32, path: &mut String, ans: &mut Vec<String>) {
            if i >= n {
                ans.push(path.clone());
                return;
            }
            path.push('0');
            dfs(i + 1, tot, n, k, path, ans);
            path.pop();
            if (path.is_empty() || path.ends_with('0')) && tot + i <= k {
                path.push('1');
                dfs(i + 1, tot + i, n, k, path, ans);
                path.pop();
            }
        }
        dfs(0, 0, n, k, &mut path, &mut ans);
        ans
    }
}
