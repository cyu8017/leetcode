// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn maximum_product(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut h: BinaryHeap<Reverse<i32>> = nums.into_iter().map(Reverse).collect();
        for _ in 0..k {
            let x = h.pop().unwrap().0 + 1;
            h.push(Reverse(x));
        }
        let mut ans = 1i64;
        while let Some(Reverse(x)) = h.pop() {
            ans = ans * x as i64 % MOD;
        }
        ans as i32
    }
}
