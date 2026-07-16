// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

use std::collections::HashMap;

impl Solution {
    fn dfs(index: usize, debts: &mut [i32]) -> i32 {
        let mut index = index;
        while index < debts.len() && debts[index] == 0 {
            index += 1;
        }
        if index == debts.len() {
            return 0;
        }

        let mut best = debts.len() as i32;
        for next_index in index + 1..debts.len() {
            if i64::from(debts[index]) * i64::from(debts[next_index]) < 0 {
                debts[next_index] += debts[index];
                best = best.min(1 + Self::dfs(index + 1, debts));
                debts[next_index] -= debts[index];
            }
        }
        best
    }

    pub fn min_transfers(transactions: Vec<Vec<i32>>) -> i32 {
        let mut balances: HashMap<i32, i32> = HashMap::new();
        for transaction in transactions {
            let source = transaction[0];
            let target = transaction[1];
            let amount = transaction[2];
            *balances.entry(source).or_insert(0) -= amount;
            *balances.entry(target).or_insert(0) += amount;
        }

        let mut debts: Vec<i32> = balances.into_values().filter(|balance| *balance != 0).collect();
        Self::dfs(0, &mut debts)
    }
}
