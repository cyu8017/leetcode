// LeetCode 1376 - Time Needed to Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

impl Solution {
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut children = vec![Vec::new(); n];
        for (i, &p) in manager.iter().enumerate() {
            if p != -1 {
                children[p as usize].push(i);
            }
        }
        fn dfs(u: usize, children: &[Vec<usize>], inform_time: &[i32]) -> i32 {
            inform_time[u]
                + children[u]
                    .iter()
                    .map(|&v| dfs(v, children, inform_time))
                    .max()
                    .unwrap_or(0)
        }
        dfs(head_id as usize, &children, &inform_time)
    }
}
