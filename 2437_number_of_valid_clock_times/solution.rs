// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

impl Solution {
    pub fn count_time(time: String) -> i32 {
        let t = time.as_bytes();
        let mut ans = 0;
        for h in 0..24 {
            for m in 0..60 {
                let hs = [b'0' + (h / 10) as u8, b'0' + (h % 10) as u8];
                let ms = [b'0' + (m / 10) as u8, b'0' + (m % 10) as u8];
                if t[0] != b'?' && t[0] != hs[0] {
                    continue;
                }
                if t[1] != b'?' && t[1] != hs[1] {
                    continue;
                }
                if t[3] != b'?' && t[3] != ms[0] {
                    continue;
                }
                if t[4] != b'?' && t[4] != ms[1] {
                    continue;
                }
                ans += 1;
            }
        }
        ans
    }
}
