struct Solution;

// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

#[derive(Clone, Copy, Eq, PartialEq)]
struct Worker {
    idx: i32,
    efficiency: i32,
    left_to_right: i32,
    pick_old: i32,
    right_to_left: i32,
    put_new: i32,
}

impl Ord for Worker {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.efficiency
            .cmp(&other.efficiency)
            .then(self.idx.cmp(&other.idx))
    }
}

impl PartialOrd for Worker {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn find_crossing_time(n: i32, k: i32, time: Vec<Vec<i32>>) -> i32 {
        let mut left: BinaryHeap<Worker> = BinaryHeap::new();
        let mut right: BinaryHeap<Worker> = BinaryHeap::new();
        for i in 0..k {
            left.push(Worker {
                idx: i,
                efficiency: time[i as usize][0] + time[i as usize][2],
                left_to_right: time[i as usize][0],
                pick_old: time[i as usize][1],
                right_to_left: time[i as usize][2],
                put_new: time[i as usize][3],
            });
        }
        let mut events: BinaryHeap<Reverse<(i32, i32, Worker)>> = BinaryHeap::new();
        let mut cur = 0;
        let mut remain = n;
        let mut done = 0;
        let mut bridge_free = 0;
        while done < n {
            while let Some(Reverse((t, side, w))) = events.peek().copied() {
                if t > cur {
                    break;
                }
                events.pop();
                if side == 0 {
                    left.push(w);
                } else {
                    right.push(w);
                }
            }
            if cur < bridge_free {
                cur = bridge_free;
                continue;
            }
            if let Some(w) = right.pop() {
                cur += w.right_to_left;
                bridge_free = cur;
                events.push(Reverse((cur + w.put_new, 0, w)));
                done += 1;
                continue;
            }
            if remain > 0 {
                if let Some(w) = left.pop() {
                    cur += w.left_to_right;
                    bridge_free = cur;
                    remain -= 1;
                    events.push(Reverse((cur + w.pick_old, 1, w)));
                    continue;
                }
            }
            if let Some(Reverse((t, _, _))) = events.peek() {
                cur = *t;
            } else {
                break;
            }
        }
        cur
    }
}

fn main() {}
