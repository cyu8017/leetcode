// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

impl Solution {
    pub fn date_range_generator(start: String, end: String, step: i32) -> Vec<String> {
        let parse = |s: &str| -> Option<(i32, i32, i32)> {
            let p: Vec<i32> = s.split('-').filter_map(|x| x.parse().ok()).collect();
            if p.len() == 3 {
                Some((p[0], p[1], p[2]))
            } else {
                None
            }
        };
        let Some((mut y, mut m, mut d)) = parse(&start) else {
            return vec![];
        };
        let Some((ey, em, ed)) = parse(&end) else {
            return vec![];
        };
        let is_leap = |yy: i32| (yy % 4 == 0 && yy % 100 != 0) || yy % 400 == 0;
        let add_days = |yy: &mut i32, mm: &mut i32, dd: &mut i32, days: i32| {
            let mut days = days;
            while days > 0 {
                let mut mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
                if is_leap(*yy) {
                    mdays[2] = 29;
                }
                *dd += 1;
                if *dd > mdays[*mm as usize] {
                    *dd = 1;
                    *mm += 1;
                }
                if *mm > 12 {
                    *mm = 1;
                    *yy += 1;
                }
                days -= 1;
            }
        };
        let mut ans = Vec::new();
        while y < ey || (y == ey && m < em) || (y == ey && m == em && d <= ed) {
            ans.push(format!("{:04}-{:02}-{:02}", y, m, d));
            add_days(&mut y, &mut m, &mut d, step);
        }
        ans
    }
}
