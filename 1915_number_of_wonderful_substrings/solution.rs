// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

impl Solution {
    pub fn wonderful_substrings(word: String) -> i64 {
        let mut count = [0i64; 1024];
        count[0] = 1;
        let mut mask = 0usize;
        let mut ans = 0i64;
        for ch in word.bytes() {
            mask ^= 1 << (ch - b'a') as usize;
            ans += count[mask];
            for bit in 0..10 {
                ans += count[mask ^ (1 << bit)];
            }
            count[mask] += 1;
        }
        ans
    }
}
