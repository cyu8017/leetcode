struct Solution;
// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

impl Solution {
    pub fn min_operations(s1: String, s2: String) -> i32 {
        const INFINITY: i32 = 1_000_000_000;
        let s1 = s1.into_bytes();
        let s2 = s2.into_bytes();
        let n = s1.len();
        let mut dp = [0, INFINITY];
        for i in 0..n {
            let mut next = [INFINITY, INFINITY];
            for forced_zero in 0..=1 {
                if dp[forced_zero] == INFINITY {
                    continue;
                }
                let mut current = s1[i];
                if forced_zero == 1 {
                    current = b'0';
                }
                let mut direct = dp[forced_zero];
                if current == b'0' && s2[i] == b'1' {
                    direct += 1;
                } else if current == b'1' && s2[i] == b'0' {
                    direct = INFINITY;
                }
                next[0] = next[0].min(direct);
                if i + 1 < n {
                    let mut cost = dp[forced_zero] + 1;
                    if current == b'0' {
                        cost += 1;
                    }
                    if s1[i + 1] == b'0' {
                        cost += 1;
                    }
                    if s2[i] == b'1' {
                        cost += 1;
                    }
                    next[1] = next[1].min(cost);
                }
            }
            dp = next;
        }
        if dp[0] == INFINITY {
            -1
        } else {
            dp[0]
        }
    }
}

fn main() {}
