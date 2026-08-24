// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

use std::collections::BinaryHeap;

impl Solution {
    pub fn max_capacity(costs: Vec<i32>, capacity: Vec<i32>, budget: i32) -> i32 {
        let mut arr = Vec::new();
        for k in 0..costs.len() {
            if costs[k] < budget {
                arr.push((costs[k], capacity[k]));
            }
        }
        if arr.is_empty() {
            return 0;
        }
        arr.sort_unstable();
        let m = arr.len();
        let mut alive = vec![true; m];
        let mut h: BinaryHeap<(i32, usize)> = BinaryHeap::new();
        for i in 0..m {
            h.push((arr[i].1, i));
        }
        while let Some(&(_, i)) = h.peek() {
            if !alive[i] {
                h.pop();
            } else {
                break;
            }
        }
        let mut ans = h.peek().unwrap().0;
        let mut i = 0usize;
        let mut j = m - 1;
        while i < j {
            alive[i] = false;
            while i < j && arr[i].0 + arr[j].0 >= budget {
                alive[j] = false;
                j -= 1;
            }
            while let Some(&(_, idx)) = h.peek() {
                if !alive[idx] {
                    h.pop();
                } else {
                    break;
                }
            }
            if let Some(&(cap, _)) = h.peek() {
                ans = ans.max(arr[i].1 + cap);
            }
            i += 1;
        }
        ans
    }
}
