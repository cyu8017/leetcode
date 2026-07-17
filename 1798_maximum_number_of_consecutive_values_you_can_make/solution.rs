// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

impl Solution {
    pub fn get_maximum_consecutive(coins: Vec<i32>) -> i32 {
        let mut coins = coins;
        coins.sort_unstable();
        let mut reach: i64 = 0;
        for coin in coins {
            if coin as i64 > reach + 1 {
                break;
            }
            reach += coin as i64;
        }
        (reach + 1) as i32
    }
}
