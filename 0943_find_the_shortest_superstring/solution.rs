// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

impl Solution {
    pub fn shortest_superstring(words: Vec<String>) -> String {
        let n = words.len();
        let mut overlap = vec![vec![0; n]; n];
        for i in 0..n {
            for j in 0..n {
                if i == j {
                    continue;
                }
                let a = words[i].as_bytes();
                let b = words[j].as_bytes();
                for k in (1..=a.len().min(b.len())).rev() {
                    if a[a.len() - k..] == b[..k] {
                        overlap[i][j] = k;
                        break;
                    }
                }
            }
        }
        let nmask = 1 << n;
        let mut dp = vec![vec![String::new(); n]; nmask];
        for i in 0..n {
            dp[1 << i][i] = words[i].clone();
        }
        for mask in 0..nmask {
            for last in 0..n {
                if mask & (1 << last) == 0 || dp[mask][last].is_empty() {
                    continue;
                }
                for nxt in 0..n {
                    if mask & (1 << nxt) != 0 {
                        continue;
                    }
                    let cand = format!(
                        "{}{}",
                        dp[mask][last],
                        &words[nxt][overlap[last][nxt]..]
                    );
                    let nm = mask | (1 << nxt);
                    if dp[nm][nxt].is_empty() || cand.len() < dp[nm][nxt].len() {
                        dp[nm][nxt] = cand;
                    }
                }
            }
        }
        let full = nmask - 1;
        let mut best = String::new();
        for i in 0..n {
            if !dp[full][i].is_empty() && (best.is_empty() || dp[full][i].len() < best.len()) {
                best = dp[full][i].clone();
            }
        }
        best
    }
}
