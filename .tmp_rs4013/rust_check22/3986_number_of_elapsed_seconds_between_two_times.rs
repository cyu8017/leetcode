struct Solution;
// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

fn to_seconds(s: &str) -> i32 {
    let b = s.as_bytes();
    let h = (b[0] - b'0') as i32 * 10 + (b[1] - b'0') as i32;
    let m = (b[3] - b'0') as i32 * 10 + (b[4] - b'0') as i32;
    let sec = (b[6] - b'0') as i32 * 10 + (b[7] - b'0') as i32;
    h * 3600 + m * 60 + sec
}

impl Solution {
    pub fn seconds_between_times(start_time: String, end_time: String) -> i32 {
        to_seconds(&end_time) - to_seconds(&start_time)
    }
}

fn main() {}
