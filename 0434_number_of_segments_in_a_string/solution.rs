// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

impl Solution {
    pub fn count_segments(s: String) -> i32 {
        let mut count = 0;
        let mut in_segment = false;
        for ch in s.chars() {
            if ch != ' ' {
                if !in_segment {
                    count += 1;
                    in_segment = true;
                }
            } else {
                in_segment = false;
            }
        }
        count
    }
}
