// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, mut k: i32) -> i64 {
        let n = nums.len();
        let mut a = nums.clone();
        a.extend_from_slice(&nums);
        if k as usize > n {
            k = n as i32;
        }
        let mut best = 0i64;
        const NEG: i64 = -(1i64 << 60);
        for start in 0..n {
            let seg = &a[start..start + n];
            let mut dp = vec![vec![NEG; (k + 1) as usize]; n + 1];
            dp[0][0] = 0;
            for i in 1..=n {
                for j in 1..=k.min(i as i32) {
                    let ju = j as usize;
                    let mut mx = NEG;
                    for t in (ju..=i).rev() {
                        if seg[t - 1] as i64 > mx {
                            mx = seg[t - 1] as i64;
                        }
                        if dp[t - 1][ju - 1] > NEG {
                            let cand = dp[t - 1][ju - 1] + mx;
                            if cand > dp[i][ju] {
                                dp[i][ju] = cand;
                            }
                        }
                    }
                }
            }
            if dp[n][k as usize] > best {
                best = dp[n][k as usize];
            }
        }
        best
    }
}
