// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

impl Solution {
    pub fn maximum_score(scores: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = scores.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut top = vec![Vec::new(); n];
        for i in 0..n {
            for &v in &g[i] {
                top[i].push(v);
                let mut j = top[i].len() - 1;
                while j > 0 && scores[top[i][j]] > scores[top[i][j - 1]] {
                    top[i].swap(j, j - 1);
                    j -= 1;
                }
                if top[i].len() > 3 {
                    top[i].truncate(3);
                }
            }
        }
        let mut ans = -1;
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            for &c in &top[a] {
                if c == b {
                    continue;
                }
                for &d in &top[b] {
                    if d == a || d == c {
                        continue;
                    }
                    ans = ans.max(scores[a] + scores[b] + scores[c] + scores[d]);
                }
            }
        }
        ans
    }
}
