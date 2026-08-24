// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

impl Solution {
    pub fn similar_rgb(color: String) -> String {
        fn closest(component: &str) -> String {
            let value = i32::from_str_radix(component, 16).unwrap();
            let rounded = (value + 8) / 17;
            format!("{rounded:x}{rounded:x}")
        }
        format!(
            "#{}{}{}",
            closest(&color[1..3]),
            closest(&color[3..5]),
            closest(&color[5..7])
        )
    }
}
