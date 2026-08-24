// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

impl Solution {
    fn cost(start_at: i32, move_cost: i32, push_cost: i32, mins: i32, secs: i32) -> i32 {
        if mins < 0 || mins > 99 || secs < 0 || secs > 99 {
            return i32::MAX / 2;
        }
        let s = if mins > 0 {
            format!("{}{:02}", mins, secs)
        } else {
            secs.to_string()
        };
        let mut cur = (b'0' + start_at as u8) as char;
        let mut ans = 0;
        for c in s.chars() {
            if c != cur {
                ans += move_cost;
                cur = c;
            }
            ans += push_cost;
        }
        ans
    }

    pub fn min_cost_set_time(start_at: i32, move_cost: i32, push_cost: i32, target_seconds: i32) -> i32 {
        let mins = target_seconds / 60;
        let secs = target_seconds % 60;
        let mut ans = Self::cost(start_at, move_cost, push_cost, mins, secs);
        if mins > 0 {
            ans = ans.min(Self::cost(start_at, move_cost, push_cost, mins - 1, secs + 60));
        }
        ans
    }
}
