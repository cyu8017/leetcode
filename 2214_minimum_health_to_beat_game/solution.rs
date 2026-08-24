// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

impl Solution {
    pub fn minimum_health(damage: Vec<i32>, armor: i32) -> i64 {
        let mut sum = 0i64;
        let mut mx = 0i32;
        for d in damage {
            sum += d as i64;
            mx = mx.max(d);
        }
        sum - armor.min(mx) as i64 + 1
    }
}
