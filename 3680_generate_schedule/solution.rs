// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

impl Solution {
    pub fn generate_schedule(n: i32) -> Vec<Vec<i32>> {
        if n < 5 {
            return vec![];
        }
        let mut matches = Vec::new();
        for i in 0..n {
            for j in 0..n {
                if i != j {
                    matches.push(vec![i, j]);
                }
            }
        }
        let mut used = vec![false; matches.len()];
        let mut sched = Vec::new();
        fn dfs(
            matches: &[Vec<i32>],
            used: &mut [bool],
            sched: &mut Vec<Vec<i32>>,
            last0: i32,
            last1: i32,
        ) -> bool {
            if sched.len() == matches.len() {
                return true;
            }
            for i in 0..matches.len() {
                if used[i] {
                    continue;
                }
                let m = &matches[i];
                if m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1 {
                    continue;
                }
                used[i] = true;
                sched.push(m.clone());
                if dfs(matches, used, sched, m[0], m[1]) {
                    return true;
                }
                sched.pop();
                used[i] = false;
            }
            false
        }
        if dfs(&matches, &mut used, &mut sched, -1, -1) {
            sched
        } else {
            vec![]
        }
    }
}
