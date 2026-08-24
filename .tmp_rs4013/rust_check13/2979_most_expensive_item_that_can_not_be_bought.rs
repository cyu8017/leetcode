#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2979 - Most Expensive Item That Can Not Be Bought
// https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

impl Solution {
    pub fn most_expensive_item(prime_one: i32, prime_two: i32) -> i32 {
        prime_one * prime_two - prime_one - prime_two
    }
}
