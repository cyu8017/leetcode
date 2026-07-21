// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn get_number_of_backlog_orders(orders: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut buy: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        let mut sell: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();

        for order in orders {
            let (price, amount, order_type) = (order[0], order[1], order[2]);
            if order_type == 0 {
                buy.push((price, amount));
            } else {
                sell.push(Reverse((price, amount)));
            }

            while let (Some(&(bp, _)), Some(&Reverse((sp, _)))) = (buy.peek(), sell.peek()) {
                if bp < sp {
                    break;
                }
                let (buy_price, mut buy_amount) = buy.pop().unwrap();
                let Reverse((sell_price, mut sell_amount)) = sell.pop().unwrap();
                let matched = buy_amount.min(sell_amount);
                buy_amount -= matched;
                sell_amount -= matched;
                if buy_amount > 0 {
                    buy.push((buy_price, buy_amount));
                }
                if sell_amount > 0 {
                    sell.push(Reverse((sell_price, sell_amount)));
                }
            }
        }

        let mut total: i64 = 0;
        for (_, amount) in buy {
            total = (total + amount as i64) % MOD;
        }
        for Reverse((_, amount)) in sell {
            total = (total + amount as i64) % MOD;
        }
        total as i32
    }
}
