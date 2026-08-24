struct Solution;
// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

use std::collections::VecDeque;

impl Solution {
    pub fn max_sum(nums: Vec<i32>, m: i32, l: i32, r: i32) -> i64 {
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }
        let mut dp = vec![0i64; n + 1];
        let mut best_selected = -(1i64 << 62);
        for _count in 1..=m {
            let mut next = dp.clone();
            let mut deque: VecDeque<usize> = VecDeque::new();
            for end in 1..=n {
                let add_index = end as i32 - l;
                if add_index >= 0 {
                    let add_index = add_index as usize;
                    let value = dp[add_index] - prefix[add_index];
                    while let Some(&last) = deque.back() {
                        if dp[last] - prefix[last] > value {
                            break;
                        }
                        deque.pop_back();
                    }
                    deque.push_back(add_index);
                }
                let min_index = end as i32 - r;
                while let Some(&front) = deque.front() {
                    if (front as i32) < min_index {
                        deque.pop_front();
                    } else {
                        break;
                    }
                }
                if let Some(&front) = deque.front() {
                    let candidate = prefix[end] + dp[front] - prefix[front];
                    if candidate > next[end] {
                        next[end] = candidate;
                    }
                    if candidate > best_selected {
                        best_selected = candidate;
                    }
                }
                if next[end - 1] > next[end] {
                    next[end] = next[end - 1];
                }
            }
            dp = next;
        }
        best_selected
    }
}

fn main() {}
