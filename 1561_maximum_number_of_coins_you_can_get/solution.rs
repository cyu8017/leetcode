// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

impl Solution {
    pub fn max_coins(mut piles: Vec<i32>) -> i32 {
        piles.sort_unstable();
        piles[piles.len() / 3..].iter().step_by(2).sum()
    }
}
