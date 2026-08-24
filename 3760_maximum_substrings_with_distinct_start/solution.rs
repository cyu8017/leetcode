// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

impl Solution {
    pub fn max_distinct(s: String) -> i32 {
        let mut cnt = [0i32; 26];
        let mut ans = 0;
        for c in s.bytes() {
            let i = (c - b'a') as usize;
            cnt[i] += 1;
            if cnt[i] == 1 {
                ans += 1;
            }
        }
        ans
    }
}
