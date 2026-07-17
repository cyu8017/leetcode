// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_time_required(jobs: Vec<i32>, k: i32) -> i32 {
        fn backtrack(i: usize, jobs: &[i32], loads: &mut Vec<i32>, best: &mut i32) {
            if i == jobs.len() {
                *best = (*best).min(*loads.iter().max().unwrap());
                return;
            }
            let mut seen = HashSet::new();
            for worker in 0..loads.len() {
                if seen.contains(&loads[worker]) {
                    continue;
                }
                if loads[worker] + jobs[i] >= *best {
                    continue;
                }
                seen.insert(loads[worker]);
                loads[worker] += jobs[i];
                backtrack(i + 1, jobs, loads, best);
                loads[worker] -= jobs[i];
                if loads[worker] == 0 {
                    break;
                }
            }
        }

        let mut jobs = jobs;
        jobs.sort_unstable_by(|a, b| b.cmp(a));
        let mut loads = vec![0; k as usize];
        let mut best: i32 = jobs.iter().sum();
        backtrack(0, &jobs, &mut loads, &mut best);
        best
    }
}
