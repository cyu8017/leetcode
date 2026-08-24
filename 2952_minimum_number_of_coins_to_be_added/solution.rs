// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

impl Solution {
    pub fn minimum_added_coins(mut coins: Vec<i32>, target: i32) -> i32 {
        coins.sort_unstable();
        let mut ans = 0;
        let mut reach = 0;
        let mut i = 0;
        while reach < target {
            if i < coins.len() && coins[i] <= reach + 1 {
                reach += coins[i];
                i += 1;
            } else {
                reach += reach + 1;
                ans += 1;
            }
        }
        ans
    }
}
