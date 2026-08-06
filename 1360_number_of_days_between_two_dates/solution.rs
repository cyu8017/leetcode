// LeetCode 1360 - Number of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

impl Solution {
    pub fn days_between_dates(date1: String, date2: String) -> i32 {
        fn to_days(s: &str) -> i32 {
            let parts: Vec<i32> = s.split('-').map(|x| x.parse().unwrap()).collect();
            let (y, m, d) = (parts[0], parts[1], parts[2]);
            let mut days = d;
            let month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
            for i in 1..m {
                days += month_days[(i - 1) as usize];
            }
            let leap = |y: i32| y % 4 == 0 && (y % 100 != 0 || y % 400 == 0);
            if m > 2 && leap(y) {
                days += 1;
            }
            for yy in 1971..y {
                days += if leap(yy) { 366 } else { 365 };
            }
            days
        }
        (to_days(&date1) - to_days(&date2)).abs()
    }
}
