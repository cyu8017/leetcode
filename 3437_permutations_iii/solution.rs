// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

impl Solution {
    pub fn permute(n: i32) -> Vec<Vec<i32>> {
        let mut ans = Vec::new();
        let mut used = vec![false; (n + 1) as usize];
        let mut cur = Vec::new();
        fn dfs(n: i32, used: &mut [bool], cur: &mut Vec<i32>, ans: &mut Vec<Vec<i32>>) {
            if cur.len() == n as usize {
                ans.push(cur.clone());
                return;
            }
            for i in 1..=n {
                if used[i as usize] {
                    continue;
                }
                if !cur.is_empty() && cur[cur.len() - 1] % 2 == i % 2 {
                    continue;
                }
                used[i as usize] = true;
                cur.push(i);
                dfs(n, used, cur, ans);
                cur.pop();
                used[i as usize] = false;
            }
        }
        dfs(n, &mut used, &mut cur, &mut ans);
        ans
    }
}
