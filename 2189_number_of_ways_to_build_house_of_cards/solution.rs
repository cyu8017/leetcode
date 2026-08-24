// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

impl Solution {
    pub fn house_of_cards(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![0; n + 1];
        dp[0] = 1;
        let mut k = 1;
        while 3 * k - 1 <= n {
            let cost = 3 * k - 1;
            for j in (cost..=n).rev() {
                dp[j] += dp[j - cost];
            }
            k += 1;
        }
        dp[n]
    }
}
