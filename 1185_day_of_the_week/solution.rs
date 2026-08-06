// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

impl Solution {
    pub fn day_of_the_week(day: i32, month: i32, year: i32) -> String {
        let t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
        let mut y = year;
        if month < 3 {
            y -= 1;
        }
        let w = (y + y / 4 - y / 100 + y / 400 + t[(month - 1) as usize] + day) % 7;
        let days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ];
        days[w as usize].to_string()
    }
}
