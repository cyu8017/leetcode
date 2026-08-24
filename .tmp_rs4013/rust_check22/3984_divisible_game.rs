struct Solution;
// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

use std::collections::HashSet;

impl Solution {
    pub fn divisible_game(nums: Vec<i32>) -> i32 {
        let mut candidates: HashSet<i32> = HashSet::new();
        candidates.insert(2);
        for &value in &nums {
            let mut divisor = 2;
            while divisor * divisor <= value {
                if value % divisor == 0 {
                    candidates.insert(divisor);
                    candidates.insert(value / divisor);
                }
                divisor += 1;
            }
            if value > 1 {
                candidates.insert(value);
            }
        }
        let mut best_score = -(1i64 << 62);
        let mut best_k = 0;
        for &k in &candidates {
            let mut ending = 0i64;
            let mut score = 0i64;
            for (i, &value) in nums.iter().enumerate() {
                let mut contribution = -(value as i64);
                if value % k == 0 {
                    contribution = value as i64;
                }
                if i == 0 || ending + contribution < contribution {
                    ending = contribution;
                } else {
                    ending += contribution;
                }
                if i == 0 || ending > score {
                    score = ending;
                }
            }
            if score > best_score || (score == best_score && k < best_k) {
                best_score = score;
                best_k = k;
            }
        }
        const MOD: i64 = 1_000_000_007;
        let mut answer = (best_score % MOD) * best_k as i64 % MOD;
        if answer < 0 {
            answer += MOD;
        }
        answer as i32
    }
}

fn main() {}
