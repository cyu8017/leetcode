// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

impl Solution {
    pub fn minimum_effort(mut tasks: Vec<Vec<i32>>) -> i32 {
        tasks.sort_by(|a, b| (b[1] - b[0]).cmp(&(a[1] - a[0])));
        let mut energy = 0i32;
        let mut spent = 0i32;
        for t in tasks {
            energy = energy.max(spent + t[1]);
            spent += t[0];
        }
        energy
    }
}
