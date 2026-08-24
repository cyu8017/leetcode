// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

impl Solution {
    pub fn count_no_zero_pairs(n: i64) -> i64 {
        let s = n.to_string();
        let m = s.len();
        let mut digits = vec![0i32; m + 1];
        let bytes = s.as_bytes();
        for i in 0..m {
            digits[i] = (bytes[m - 1 - i] - b'0') as i32;
        }
        let mut dp = [[[0i64; 2]; 2]; 2];
        dp[0][1][1] = 1;
        for pos in 0..=m {
            let mut ndp = [[[0i64; 2]; 2]; 2];
            let target = digits[pos];
            for carry in 0..2 {
                for alive_a in 0..2 {
                    for alive_b in 0..2 {
                        let ways = dp[carry][alive_a][alive_b];
                        if ways == 0 {
                            continue;
                        }
                        let mut a_opts = Vec::new();
                        if alive_a == 1 {
                            for d in 1..=9 {
                                a_opts.push((d, 1));
                            }
                            if pos > 0 {
                                a_opts.push((0, 0));
                            }
                        } else {
                            a_opts.push((0, 0));
                        }
                        let mut b_opts = Vec::new();
                        if alive_b == 1 {
                            for d in 1..=9 {
                                b_opts.push((d, 1));
                            }
                            if pos > 0 {
                                b_opts.push((0, 0));
                            }
                        } else {
                            b_opts.push((0, 0));
                        }
                        for &(da, na) in &a_opts {
                            for &(db, nb) in &b_opts {
                                let sum = da + db + carry as i32;
                                if sum % 10 != target {
                                    continue;
                                }
                                let ncarry = (sum / 10) as usize;
                                ndp[ncarry][na][nb] += ways;
                            }
                        }
                    }
                }
            }
            dp = ndp;
        }
        dp[0][0][0]
    }
}
