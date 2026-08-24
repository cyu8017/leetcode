// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

impl Solution {
    pub fn max_upgrades(count: Vec<i32>, upgrade: Vec<i32>, sell: Vec<i32>, money: Vec<i32>) -> Vec<i32> {
        count
            .iter()
            .enumerate()
            .map(|(i, &cnt)| {
                let cnt = cnt as i64;
                cnt.min((cnt * sell[i] as i64 + money[i] as i64) / (upgrade[i] as i64 + sell[i] as i64)) as i32
            })
            .collect()
    }
}
