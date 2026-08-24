struct Solution;
// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

impl Solution {
    pub fn maximum_coins(heroes: Vec<i32>, monsters: Vec<i32>, coins: Vec<i32>) -> Vec<i64> {
        let n = monsters.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_unstable_by_key(|&i| monsters[i]);
        let mut pref = vec![0i64; n + 1];
        let mut ms = vec![0i32; n];
        for i in 0..n {
            ms[i] = monsters[idx[i]];
            pref[i + 1] = pref[i] + coins[idx[i]] as i64;
        }
        heroes
            .into_iter()
            .map(|h| {
                let p = ms.partition_point(|&m| m <= h);
                pref[p]
            })
            .collect()
    }
}

fn main() {}
