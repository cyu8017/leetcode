// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

impl Solution {
    pub fn count_winning_sequences(s: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = s.len();
        let sb = s.as_bytes();
        let mut mp = [0i32; 256];
        mp[b'F' as usize] = 0;
        mp[b'W' as usize] = 1;
        mp[b'E' as usize] = 2;
        let beat = [2, 0, 1];
        let mut score = [[0i32; 3]; 3];
        for a in 0..3 {
            for b in 0..3 {
                score[a][b] = if a == b {
                    0
                } else if beat[a] == b {
                    1
                } else {
                    -1
                };
            }
        }
        let offset = n as i32;
        let mut dp = vec![vec![0i32; 2 * n + 1]; 3];
        let b0 = mp[sb[0] as usize] as usize;
        for a in 0..3 {
            dp[a][(score[a][b0] + offset) as usize] = 1;
        }
        for i in 1..n {
            let mut ndp = vec![vec![0i32; 2 * n + 1]; 3];
            let b = mp[sb[i] as usize] as usize;
            for last in 0..3 {
                for d in 0..=2 * n {
                    if dp[last][d] == 0 {
                        continue;
                    }
                    for a in 0..3 {
                        if a == last {
                            continue;
                        }
                        let nd = d as i32 + score[a][b];
                        if nd < 0 || nd > 2 * n as i32 {
                            continue;
                        }
                        ndp[a][nd as usize] = (ndp[a][nd as usize] + dp[last][d]) % MOD;
                    }
                }
            }
            dp = ndp;
        }
        let mut ans = 0;
        for a in 0..3 {
            for d in (offset as usize + 1)..=2 * n {
                ans = (ans + dp[a][d]) % MOD;
            }
        }
        ans
    }
}
