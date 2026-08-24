struct Solution;
// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

impl Solution {
    pub fn check_record(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut dp = [[0i64; 3]; 2];
        dp[0][0] = 1;
        for _ in 0..n {
            let mut nxt = [[0i64; 3]; 2];
            for absences in 0..2 {
                for lates in 0..3 {
                    let ways = dp[absences][lates];
                    if ways == 0 {
                        continue;
                    }
                    nxt[absences][0] = (nxt[absences][0] + ways) % MOD;
                    if absences == 0 {
                        nxt[1][0] = (nxt[1][0] + ways) % MOD;
                    }
                    if lates < 2 {
                        nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % MOD;
                    }
                }
            }
            dp = nxt;
        }
        let mut total = 0;
        for absences in 0..2 {
            for lates in 0..3 {
                total = (total + dp[absences][lates]) % MOD;
            }
        }
        total as i32
    }
}

fn main() {}
