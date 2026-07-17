// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn eaten_apples(apples: Vec<i32>, days: Vec<i32>) -> i32 {
        let mut heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        let n = apples.len() as i32;
        let mut day = 0;
        let mut eaten = 0;
        while day < n || !heap.is_empty() {
            if day < n && apples[day as usize] > 0 {
                heap.push(Reverse((day + days[day as usize], apples[day as usize])));
            }
            while let Some(&Reverse((expire, _))) = heap.peek() {
                if expire <= day {
                    heap.pop();
                } else {
                    break;
                }
            }
            if let Some(Reverse((expire, count))) = heap.pop() {
                eaten += 1;
                if count > 1 {
                    heap.push(Reverse((expire, count - 1)));
                }
            }
            day += 1;
        }
        eaten
    }
}
