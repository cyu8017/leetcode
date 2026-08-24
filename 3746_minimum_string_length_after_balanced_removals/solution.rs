// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

impl Solution {
    pub fn min_length_after_removals(s: String) -> i32 {
        let a = s.bytes().filter(|&c| c == b'a').count() as i32;
        let b = s.len() as i32 - a;
        (a - b).abs()
    }
}
