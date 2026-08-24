// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

impl Solution {
    pub fn minimum_cost(mut cost: Vec<i32>) -> i32 {
        cost.sort_unstable_by(|a, b| b.cmp(a));
        cost.iter()
            .enumerate()
            .filter(|(i, _)| i % 3 != 2)
            .map(|(_, &c)| c)
            .sum()
    }
}
