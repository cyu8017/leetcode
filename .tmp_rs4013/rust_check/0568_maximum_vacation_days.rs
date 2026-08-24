struct Solution;
// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

impl Solution {
    pub fn max_vacation_days(flights: Vec<Vec<i32>>, days: Vec<Vec<i32>>) -> i32 {
        let cities = flights.len();
        let weeks = days[0].len();
        const NEG: i32 = -1_000_000_000;
        let mut dp = vec![NEG; cities];
        dp[0] = 0;
        for week in 0..weeks {
            let mut nxt = vec![NEG; cities];
            for city in 0..cities {
                if dp[city] == NEG {
                    continue;
                }
                for dest in 0..cities {
                    if dest == city || flights[city][dest] == 1 {
                        nxt[dest] = nxt[dest].max(dp[city] + days[dest][week]);
                    }
                }
            }
            dp = nxt;
        }
        *dp.iter().max().unwrap()
    }
}

fn main() {}
