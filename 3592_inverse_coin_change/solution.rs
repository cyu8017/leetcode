// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

impl Solution {
    pub fn find_coins(num_ways: Vec<i32>) -> Vec<i32> {
        let n = num_ways.len();
        let mut dp = vec![0i32; n + 1];
        let mut coins = Vec::new();
        dp[0] = 1;
        for amt in 1..=n {
            let ways = num_ways[amt - 1];
            if dp[amt] == ways {
                continue;
            }
            if dp[amt] + 1 == ways {
                coins.push(amt as i32);
                for x in amt..=n {
                    dp[x] += dp[x - amt];
                }
                if dp[amt] != ways {
                    return vec![];
                }
                continue;
            }
            return vec![];
        }
        coins
    }
}
