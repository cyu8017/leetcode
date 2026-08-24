// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut prev = 0;
        let mut cur = 1;
        let mut ans = 0;
        for i in 1..bytes.len() {
            if bytes[i] == bytes[i - 1] {
                cur += 1;
            } else {
                ans += prev.min(cur);
                prev = cur;
                cur = 1;
            }
        }
        ans + prev.min(cur)
    }
}
