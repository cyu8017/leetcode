// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

impl Solution {
    pub fn reformat_date(date: String) -> String {
        let months = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
        ];
        let parts: Vec<&str> = date.split_whitespace().collect();
        let day: i32 = parts[0][..parts[0].len() - 2].parse().unwrap();
        let month = months.iter().position(|&m| m == parts[1]).unwrap() + 1;
        format!("{}-{:02}-{:02}", parts[2], month, day)
    }
}
