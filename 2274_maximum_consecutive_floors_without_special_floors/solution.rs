// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

impl Solution {
    pub fn max_consecutive(bottom: i32, top: i32, mut special: Vec<i32>) -> i32 {
        special.sort_unstable();
        let mut ans = special[0] - bottom;
        for i in 1..special.len() {
            ans = ans.max(special[i] - special[i - 1] - 1);
        }
        ans.max(top - *special.last().unwrap())
    }
}
