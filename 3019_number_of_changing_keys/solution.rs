// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

impl Solution {
    pub fn count_key_changes(s: String) -> i32 {
        let s = s.to_ascii_lowercase();
        let b = s.as_bytes();
        let mut ans = 0;
        for i in 1..b.len() {
            if b[i] != b[i - 1] {
                ans += 1;
            }
        }
        ans
    }
}
