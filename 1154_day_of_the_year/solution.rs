// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

impl Solution {
    pub fn day_of_year(date: String) -> i32 {
        let year: i32 = date[0..4].parse().unwrap();
        let month: usize = date[5..7].parse().unwrap();
        let day: i32 = date[8..10].parse().unwrap();
        let leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
        let mut days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if leap {
            days[1] = 29;
        }
        let mut ans = day;
        for i in 0..month - 1 {
            ans += days[i];
        }
        ans
    }
}
