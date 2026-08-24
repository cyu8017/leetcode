// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

impl Solution {
    pub fn max_operations(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        let mut cnt = 0;
        for i in 0..b.len() {
            if b[i] == b'1' {
                cnt += 1;
            } else if i > 0 && b[i - 1] == b'1' {
                ans += cnt;
            }
        }
        ans
    }
}
