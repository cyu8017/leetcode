// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

impl Solution {
    pub fn next_day(date: String) -> String {
        let parts: Vec<i32> = date.split('-').filter_map(|p| p.parse().ok()).collect();
        if parts.len() != 3 {
            return date;
        }
        let (mut y, mut m, mut d) = (parts[0], parts[1], parts[2]);
        let is_leap = |yy: i32| (yy % 4 == 0 && yy % 100 != 0) || yy % 400 == 0;
        let mut mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if is_leap(y) {
            mdays[2] = 29;
        }
        d += 1;
        if d > mdays[m as usize] {
            d = 1;
            m += 1;
        }
        if m > 12 {
            m = 1;
            y += 1;
        }
        format!("{:04}-{:02}-{:02}", y, m, d)
    }
}
