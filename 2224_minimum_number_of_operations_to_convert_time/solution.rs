// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

impl Solution {
    pub fn convert_time(current: String, correct: String) -> i32 {
        fn to_min(t: &str) -> i32 {
            let b = t.as_bytes();
            (b[0] - b'0') as i32 * 600
                + (b[1] - b'0') as i32 * 60
                + (b[3] - b'0') as i32 * 10
                + (b[4] - b'0') as i32
        }
        let mut diff = to_min(&correct) - to_min(&current);
        let mut ans = 0;
        for step in [60, 15, 5, 1] {
            ans += diff / step;
            diff %= step;
        }
        ans
    }
}
