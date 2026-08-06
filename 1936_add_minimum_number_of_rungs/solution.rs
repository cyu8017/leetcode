// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

impl Solution {
    pub fn add_rungs(rungs: Vec<i32>, dist: i32) -> i32 {
        let mut prev = 0;
        let mut ans = 0;
        for r in rungs {
            let gap = r - prev;
            if gap > dist {
                ans += (gap - 1) / dist;
            }
            prev = r;
        }
        ans
    }
}
