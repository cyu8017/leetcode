struct Solution;
// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

impl Solution {
    pub fn max_score(n: i32, k: i32, stay_score: Vec<Vec<i32>>, travel_score: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mut dp = vec![0i32; n];
        for day in 0..k {
            let mut ndp = vec![-(1 << 30); n];
            for dest in 0..n {
                let mut best = -(1 << 30);
                for src in 0..n {
                    let mut val = dp[src];
                    if src == dest {
                        val += stay_score[day][dest];
                    } else {
                        val += travel_score[src][dest];
                    }
                    if val > best {
                        best = val;
                    }
                }
                ndp[dest] = best;
            }
            dp = ndp;
        }
        *dp.iter().max().unwrap()
    }
}

fn main() {}
