struct Solution;
// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

use std::collections::HashMap;

impl Solution {
    fn dfs(
        state: Vec<i32>,
        price: &[i32],
        special: &[Vec<i32>],
        memo: &mut HashMap<Vec<i32>, i32>,
    ) -> i32 {
        if let Some(&cached) = memo.get(&state) {
            return cached;
        }
        let mut cost = 0;
        for i in 0..price.len() {
            cost += state[i] * price[i];
        }
        for offer in special {
            let mut nxt = state.clone();
            let mut valid = true;
            for i in 0..price.len() {
                if nxt[i] < offer[i] {
                    valid = false;
                    break;
                }
                nxt[i] -= offer[i];
            }
            if valid {
                cost = cost.min(offer[price.len()] + Self::dfs(nxt, price, special, memo));
            }
        }
        memo.insert(state, cost);
        cost
    }

    pub fn shopping_offers(price: Vec<i32>, special: Vec<Vec<i32>>, needs: Vec<i32>) -> i32 {
        let mut memo = HashMap::new();
        Self::dfs(needs, &price, &special, &mut memo)
    }
}

fn main() {}
