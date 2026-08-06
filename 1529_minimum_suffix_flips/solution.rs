// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

impl Solution {
    pub fn min_flips(target: String) -> i32 {
        let mut ans = 0;
        let mut prev = b'0';
        for ch in target.bytes() {
            if ch != prev {
                ans += 1;
                prev = ch;
            }
        }
        ans
    }
}
