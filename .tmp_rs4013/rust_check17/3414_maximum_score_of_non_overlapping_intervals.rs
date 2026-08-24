struct Solution;
// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

impl Solution {
    fn better(a: &(i64, Vec<i32>), b: &(i64, Vec<i32>)) -> (i64, Vec<i32>) {
        if a.0 != b.0 {
            return if a.0 > b.0 { a.clone() } else { b.clone() };
        }
        let n = a.1.len().min(b.1.len());
        for i in 0..n {
            if a.1[i] != b.1[i] {
                return if a.1[i] < b.1[i] {
                    a.clone()
                } else {
                    b.clone()
                };
            }
        }
        if a.1.len() <= b.1.len() {
            a.clone()
        } else {
            b.clone()
        }
    }

    pub fn maximum_weight(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        let n = intervals.len();
        let mut arr: Vec<(i32, i32, i32, i32)> = intervals
            .iter()
            .enumerate()
            .map(|(i, v)| (v[0], v[1], v[2], i as i32))
            .collect();
        arr.sort_by_key(|a| a.1);
        let mut dp = vec![vec![(0i64, Vec::<i32>::new()); 5]; n + 1];
        for i in 1..=n {
            let cur = arr[i - 1];
            for t in 0..=4 {
                dp[i][t] = dp[i - 1][t].clone();
            }
            let p = arr[..i - 1].partition_point(|a| a.1 < cur.0);
            let prev = p;
            for t in 1..=4 {
                let prev_state = dp[prev][t - 1].clone();
                let mut cand_idx = prev_state.1;
                cand_idx.push(cur.3);
                cand_idx.sort_unstable();
                let cand = (prev_state.0 + cur.2 as i64, cand_idx);
                dp[i][t] = Self::better(&dp[i][t], &cand);
            }
        }
        let mut best = dp[n][0].clone();
        for t in 1..=4 {
            best = Self::better(&best, &dp[n][t]);
        }
        best.1
    }
}

fn main() {}
