struct Solution;

// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

impl Solution {
    pub fn find_minimum_time(mut tasks: Vec<Vec<i32>>) -> i32 {
        tasks.sort_by_key(|t| t[1]);
        let mut used = vec![false; 2001];
        let mut ans = 0;
        for t in tasks {
            let start = t[0] as usize;
            let end = t[1] as usize;
            let dur = t[2];
            let mut have = 0;
            for i in start..=end {
                if used[i] {
                    have += 1;
                }
            }
            let mut need = dur - have;
            for i in (start..=end).rev() {
                if need <= 0 {
                    break;
                }
                if !used[i] {
                    used[i] = true;
                    need -= 1;
                    ans += 1;
                }
            }
        }
        ans
    }
}

fn main() {}
