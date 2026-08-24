// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let mut cnt = [0i32; 26];
        for c in word.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        cnt.sort_unstable();
        let mut ans = 0;
        for i in 0..26 {
            ans += (i as i32 / 8 + 1) * cnt[26 - i - 1];
        }
        ans
    }
}
