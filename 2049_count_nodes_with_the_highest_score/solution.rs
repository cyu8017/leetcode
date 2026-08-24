// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

impl Solution {
    pub fn count_highest_score_nodes(parents: Vec<i32>) -> i32 {
        let n = parents.len();
        let mut children = vec![Vec::new(); n];
        for i in 1..n {
            children[parents[i] as usize].push(i);
        }
        let mut size = vec![0i32; n];
        fn dfs(u: usize, children: &[Vec<usize>], size: &mut [i32]) -> i32 {
            size[u] = 1;
            for &v in &children[u] {
                size[u] += dfs(v, children, size);
            }
            size[u]
        }
        dfs(0, &children, &mut size);
        let mut best = 0i64;
        let mut ans = 0;
        for u in 0..n {
            let mut score = 1i64;
            for &v in &children[u] {
                score *= size[v] as i64;
            }
            let up = n as i32 - size[u];
            if up > 0 {
                score *= up as i64;
            }
            if score > best {
                best = score;
                ans = 1;
            } else if score == best {
                ans += 1;
            }
        }
        ans
    }
}
