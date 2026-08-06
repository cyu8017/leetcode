// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn smallest_chair(times: Vec<Vec<i32>>, target_friend: i32) -> i32 {
        let mut order: Vec<usize> = (0..times.len()).collect();
        order.sort_by_key(|&i| times[i][0]);
        let mut free: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut next_chair = 0i32;
        let mut leaving: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        for &i in &order {
            let arr = times[i][0];
            let leave = times[i][1];
            while let Some(&Reverse((lt, _))) = leaving.peek() {
                if lt <= arr {
                    let Reverse((_, chair)) = leaving.pop().unwrap();
                    free.push(Reverse(chair));
                } else {
                    break;
                }
            }
            let chair = if let Some(Reverse(c)) = free.pop() {
                c
            } else {
                let c = next_chair;
                next_chair += 1;
                c
            };
            if i as i32 == target_friend {
                return chair;
            }
            leaving.push(Reverse((leave, chair)));
        }
        -1
    }
}
