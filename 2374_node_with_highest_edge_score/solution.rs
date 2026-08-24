// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

impl Solution {
    pub fn edge_score(edges: Vec<i32>) -> i32 {
        let n = edges.len();
        let mut score = vec![0i64; n];
        for i in 0..n {
            score[edges[i] as usize] += i as i64;
        }
        let mut ans = 0;
        for i in 1..n {
            if score[i] > score[ans] {
                ans = i;
            }
        }
        ans as i32
    }
}
