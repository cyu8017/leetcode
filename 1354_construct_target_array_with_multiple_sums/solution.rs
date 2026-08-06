// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

use std::collections::BinaryHeap;

impl Solution {
    pub fn is_possible(target: Vec<i32>) -> bool {
        if target.len() == 1 {
            return target[0] == 1;
        }
        let mut total: i64 = target.iter().map(|&x| x as i64).sum();
        let mut heap: BinaryHeap<i64> = target.into_iter().map(|x| x as i64).collect();
        loop {
            let x = heap.pop().unwrap();
            let rest = total - x;
            if x == 1 || rest == 1 {
                return true;
            }
            if rest == 0 || x <= rest {
                return false;
            }
            let prev = x % rest;
            if prev == 0 {
                return false;
            }
            total = rest + prev;
            heap.push(prev);
        }
    }
}
