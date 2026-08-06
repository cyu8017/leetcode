// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

impl Solution {
    pub fn contains_pattern(arr: Vec<i32>, m: i32, k: i32) -> bool {
        let m = m as usize;
        let mut run = 0;
        for i in m..arr.len() {
            run = if arr[i] == arr[i - m] { run + 1 } else { 0 };
            if run >= m as i32 * (k - 1) {
                return true;
            }
        }
        false
    }
}
