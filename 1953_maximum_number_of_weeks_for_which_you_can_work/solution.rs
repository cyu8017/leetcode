// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

impl Solution {
    pub fn number_of_weeks(milestones: Vec<i32>) -> i64 {
        let total: i64 = milestones.iter().map(|&x| x as i64).sum();
        let mx = *milestones.iter().max().unwrap() as i64;
        let rest = total - mx;
        if mx > rest + 1 {
            2 * rest + 1
        } else {
            total
        }
    }
}
