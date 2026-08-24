// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

use std::collections::VecDeque;

#[derive(Clone, Copy)]
struct State {
    value: i64,
    count: i32,
}

fn better(a: State, b: State) -> bool {
    a.value > b.value || (a.value == b.value && a.count > b.count)
}

impl Solution {
    pub fn max_sum(nums: Vec<i32>, m: i32, l: i32, r: i32) -> i64 {
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }

        let run = |penalty: i64| -> State {
            let mut dp = vec![State { value: 0, count: 0 }; n + 1];
            let mut deque: VecDeque<usize> = VecDeque::new();
            let candidate_better = |dp: &[State], a: usize, b: usize| -> bool {
                let left = State {
                    value: dp[a].value - prefix[a],
                    count: dp[a].count,
                };
                let right = State {
                    value: dp[b].value - prefix[b],
                    count: dp[b].count,
                };
                better(left, right)
            };
            for end in 1..=n {
                let add_index = end as i32 - l;
                if add_index >= 0 {
                    let add_index = add_index as usize;
                    while let Some(&back) = deque.back() {
                        if candidate_better(&dp, add_index, back) {
                            deque.pop_back();
                        } else {
                            break;
                        }
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
                dp[end] = dp[end - 1];
                if let Some(&start) = deque.front() {
                    let take = State {
                        value: dp[start].value + prefix[end] - prefix[start] - penalty,
                        count: dp[start].count + 1,
                    };
                    if better(take, dp[end]) {
                        dp[end] = take;
                    }
                }
            }
            dp[n]
        };

        let unconstrained = run(0);
        if unconstrained.count > 0 && unconstrained.count <= m {
            return unconstrained.value;
        }
        if unconstrained.count > m {
            let mut bound = 0i64;
            for &value in &nums {
                bound += if value >= 0 { value as i64 } else { -(value as i64) };
            }
            let mut low = 0i64;
            let mut high = bound + 1;
            while low < high {
                let mid = low + (high - low + 1) / 2;
                if run(mid).count >= m {
                    low = mid;
                } else {
                    high = mid - 1;
                }
            }
            let state = run(low);
            return state.value + low * m as i64;
        }
        const INFINITY: i64 = 1 << 60;
        let mut best_single = -INFINITY;
        let mut deque: VecDeque<usize> = VecDeque::new();
        for end in 1..=n {
            let add_index = end as i32 - l;
            if add_index >= 0 {
                let add_index = add_index as usize;
                while let Some(&back) = deque.back() {
                    if prefix[back] >= prefix[add_index] {
                        deque.pop_back();
                    } else {
                        break;
                    }
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
                let sum = prefix[end] - prefix[front];
                if sum > best_single {
                    best_single = sum;
                }
            }
        }
        best_single
    }
}
