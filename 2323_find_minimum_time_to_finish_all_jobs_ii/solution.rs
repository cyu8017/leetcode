// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

impl Solution {
    pub fn minimum_time(mut jobs: Vec<i32>, mut workers: Vec<i32>) -> i32 {
        jobs.sort_unstable();
        workers.sort_unstable();
        let mut ans = 0;
        for i in 0..jobs.len() {
            ans = ans.max((jobs[i] + workers[i] - 1) / workers[i]);
        }
        ans
    }
}
