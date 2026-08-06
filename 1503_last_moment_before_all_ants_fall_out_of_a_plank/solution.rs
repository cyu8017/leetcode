// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

impl Solution {
    pub fn get_last_moment(n: i32, left: Vec<i32>, right: Vec<i32>) -> i32 {
        let mut ans = 0;
        for x in left {
            ans = ans.max(x);
        }
        for x in right {
            ans = ans.max(n - x);
        }
        ans
    }
}
