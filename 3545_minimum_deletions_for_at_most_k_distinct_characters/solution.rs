// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

impl Solution {
    pub fn min_deletion(s: String, k: i32) -> i32 {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        cnt.sort();
        let mut ans = 0;
        for i in 0..26 - k as usize {
            ans += cnt[i];
        }
        ans
    }
}
