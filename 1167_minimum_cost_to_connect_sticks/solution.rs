// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn connect_sticks(sticks: Vec<i32>) -> i32 {
        let mut heap: BinaryHeap<Reverse<i32>> = sticks.into_iter().map(Reverse).collect();
        let mut ans = 0;
        while heap.len() > 1 {
            let a = heap.pop().unwrap().0;
            let b = heap.pop().unwrap().0;
            ans += a + b;
            heap.push(Reverse(a + b));
        }
        ans
    }
}
