struct Solution;
// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

impl Solution {
    pub fn min_cost(
        source: String,
        target: String,
        rules: Vec<Vec<String>>,
        costs: Vec<i32>,
    ) -> i32 {
        let source = source.as_bytes();
        let target = target.as_bytes();
        let n = source.len();
        if target.len() != n {
            return -1;
        }
        let mut dp = vec![i32::MAX; n + 1];
        dp[0] = 0;
        for i in 0..n {
            if dp[i] == i32::MAX {
                continue;
            }
            if source[i] == target[i] && dp[i] < dp[i + 1] {
                dp[i + 1] = dp[i];
            }
            for j in 0..rules.len() {
                let p = rules[j][0].as_bytes();
                let r = rules[j][1].as_bytes();
                let plen = p.len();
                if i + plen > n {
                    continue;
                }
                let mut c = costs[j];
                let mut ok = true;
                for k in 0..plen {
                    if r[k] != target[i + k] {
                        ok = false;
                        break;
                    }
                    if p[k] == b'*' {
                        c += 1;
                    } else if p[k] != source[i + k] {
                        ok = false;
                        break;
                    }
                }
                if ok && dp[i] <= i32::MAX - c && dp[i] + c < dp[i + plen] {
                    dp[i + plen] = dp[i] + c;
                }
            }
        }
        if dp[n] == i32::MAX {
            -1
        } else {
            dp[n]
        }
    }
}

fn main() {}
