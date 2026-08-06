// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

impl Solution {
    pub fn min_time_to_type(word: String) -> i32 {
        let mut cur = b'a';
        let mut ans = 0;
        for ch in word.bytes() {
            let d = (ch as i32 - cur as i32).abs();
            ans += d.min(26 - d) + 1;
            cur = ch;
        }
        ans
    }
}
