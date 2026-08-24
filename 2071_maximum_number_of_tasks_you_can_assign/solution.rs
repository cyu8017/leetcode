// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

use std::collections::BTreeMap;

impl Solution {
    pub fn max_task_assign(
        mut tasks: Vec<i32>,
        mut workers: Vec<i32>,
        pills: i32,
        strength: i32,
    ) -> i32 {
        tasks.sort_unstable();
        workers.sort_unstable();
        let can = |k: usize| -> bool {
            if k == 0 {
                return true;
            }
            let mut ws = BTreeMap::new();
            for &w in &workers[workers.len() - k..] {
                *ws.entry(w).or_insert(0) += 1;
            }
            let mut p = pills;
            for i in (0..k).rev() {
                let task = tasks[i];
                let last = *ws.iter().next_back().unwrap().0;
                if last >= task {
                    let e = ws.get_mut(&last).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        ws.remove(&last);
                    }
                    continue;
                }
                if p == 0 {
                    return false;
                }
                if let Some((&need, _)) = ws.range(task - strength..).next() {
                    let e = ws.get_mut(&need).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        ws.remove(&need);
                    }
                    p -= 1;
                } else {
                    return false;
                }
            }
            true
        };
        let mut lo = 0;
        let mut hi = tasks.len().min(workers.len());
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if can(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
