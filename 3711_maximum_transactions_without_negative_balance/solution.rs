// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

use std::collections::BTreeMap;

impl Solution {
    pub fn max_transactions(transactions: Vec<i32>) -> i32 {
        let mut tm: BTreeMap<i32, i32> = BTreeMap::new();
        let mut ans = transactions.len() as i32;
        let mut s = 0i64;
        for x in transactions {
            s += x as i64;
            *tm.entry(x).or_insert(0) += 1;
            while s < 0 {
                let y = *tm.keys().next().unwrap();
                s -= y as i64;
                ans -= 1;
                let e = tm.get_mut(&y).unwrap();
                *e -= 1;
                if *e == 0 {
                    tm.remove(&y);
                }
            }
        }
        ans
    }
}
